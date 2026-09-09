#!/usr/bin/env python3
"""
Multi-Account Workspace Quota & Failover Pool (10 Accounts)
Provides autonomous round-robin rotation, sliding-window RPM rate-limit detection (429),
and automatic circuit breaking across 10 Google Workspace accounts.
"""
import sqlite3
import time
import os
import json
import logging
from typing import Optional, Dict, List, Any

DB_PATH = os.path.expanduser("~/.air1/state/MULTI_ACCOUNT_WORKSPACE_POOL.sqlite")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("MultiAccountPool")

DEFAULT_ACCOUNTS = [
    {"slot": 1, "email": "lakhidas168@gmail.com", "profile": "default", "status": "ACTIVE_AUTHENTICATED", "is_primary": 1, "rpm": 60},
    {"slot": 2, "email": "migl.spark.node02@gmail.com", "profile": "node02", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 3, "email": "migl.spark.node03@gmail.com", "profile": "node03", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 4, "email": "migl.spark.node04@gmail.com", "profile": "node04", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 5, "email": "migl.spark.node05@gmail.com", "profile": "node05", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 6, "email": "migl.spark.node06@gmail.com", "profile": "node06", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 7, "email": "migl.spark.node07@gmail.com", "profile": "node07", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 8, "email": "migl.spark.node08@gmail.com", "profile": "node08", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 9, "email": "migl.spark.node09@gmail.com", "profile": "node09", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
    {"slot": 10, "email": "migl.spark.node10@gmail.com", "profile": "node10", "status": "STANDBY_READY", "is_primary": 0, "rpm": 60},
]

class MultiAccountPool:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    slot_number INTEGER UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    profile_name TEXT NOT NULL,
                    auth_status TEXT NOT NULL,
                    quota_rpm INTEGER DEFAULT 60,
                    current_rpm_used INTEGER DEFAULT 0,
                    last_used_timestamp REAL DEFAULT 0.0,
                    backoff_until REAL DEFAULT 0.0,
                    total_requests_served INTEGER DEFAULT 0,
                    is_primary INTEGER DEFAULT 0
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS account_audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL NOT NULL,
                    account_id INTEGER,
                    action TEXT NOT NULL,
                    status_code INTEGER,
                    latency_ms REAL,
                    notes TEXT
                )
            """)
            conn.commit()

            # Seed default 10 accounts if empty
            cursor.execute("SELECT COUNT(*) as cnt FROM accounts")
            if cursor.fetchone()["cnt"] == 0:
                for acc in DEFAULT_ACCOUNTS:
                    cursor.execute("""
                        INSERT INTO accounts (slot_number, email, profile_name, auth_status, quota_rpm, is_primary)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (acc["slot"], acc["email"], acc["profile"], acc["status"], acc["rpm"], acc["is_primary"]))
                conn.commit()
                logger.info(f"Initialized 10-account workspace quota pool in {self.db_path}")

    def get_next_available_account(self) -> Dict[str, Any]:
        """
        Selects the optimal account using health, active backoff, and lowest load.
        Prefers Primary account if available and not rate limited.
        """
        now = time.time()
        with self._get_conn() as conn:
            cursor = conn.cursor()
            
            # Reset expired backoffs
            cursor.execute("""
                UPDATE accounts 
                SET auth_status = CASE WHEN is_primary = 1 THEN 'ACTIVE_AUTHENTICATED' ELSE 'STANDBY_READY' END,
                    backoff_until = 0.0
                WHERE backoff_until > 0 AND backoff_until <= ?
            """, (now,))
            conn.commit()

            # 1. Try primary account first if healthy and not in backoff
            cursor.execute("""
                SELECT * FROM accounts 
                WHERE is_primary = 1 AND backoff_until <= ? AND auth_status = 'ACTIVE_AUTHENTICATED'
            """, (now,))
            primary = cursor.fetchone()
            if primary and primary["current_rpm_used"] < primary["quota_rpm"]:
                return dict(primary)

            # 2. Otherwise, select healthiest non-rate-limited account with lowest current load
            cursor.execute("""
                SELECT * FROM accounts
                WHERE backoff_until <= ? AND auth_status IN ('ACTIVE_AUTHENTICATED', 'STANDBY_READY')
                ORDER BY current_rpm_used ASC, last_used_timestamp ASC
                LIMIT 1
            """, (now,))
            candidate = cursor.fetchone()
            if candidate:
                return dict(candidate)

            # 3. If all accounts are rate-limited, find the one with shortest remaining backoff
            cursor.execute("""
                SELECT * FROM accounts
                ORDER BY backoff_until ASC
                LIMIT 1
            """)
            fallback = cursor.fetchone()
            return dict(fallback) if fallback else {}

    def record_request(self, account_id: int, status_code: int = 200, latency_ms: float = 0.0, notes: str = ""):
        now = time.time()
        with self._get_conn() as conn:
            cursor = conn.cursor()
            if status_code == 429:
                # Rate limit encountered - apply 60s circuit breaker backoff
                backoff_time = now + 60.0
                cursor.execute("""
                    UPDATE accounts 
                    SET auth_status = 'RATE_LIMITED',
                        backoff_until = ?,
                        current_rpm_used = current_rpm_used + 1,
                        last_used_timestamp = ?
                    WHERE id = ?
                """, (backoff_time, now, account_id))
                logger.warning(f"Account ID {account_id} hit 429 RATE_LIMIT. Circuit breaker backoff applied until {backoff_time}")
            else:
                cursor.execute("""
                    UPDATE accounts
                    SET total_requests_served = total_requests_served + 1,
                        current_rpm_used = current_rpm_used + 1,
                        last_used_timestamp = ?
                    WHERE id = ?
                """, (now, account_id))

            cursor.execute("""
                INSERT INTO account_audit_log (timestamp, account_id, action, status_code, latency_ms, notes)
                VALUES (?, ?, 'REQUEST_EXEC', ?, ?, ?)
            """, (now, account_id, status_code, latency_ms, notes))
            conn.commit()

    def report_rate_limit(self, account_id: int, backoff_seconds: float = 60.0):
        now = time.time()
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE accounts
                SET auth_status = 'RATE_LIMITED',
                    backoff_until = ?
                WHERE id = ?
            """, (now + backoff_seconds, account_id))
            cursor.execute("""
                INSERT INTO account_audit_log (timestamp, account_id, action, status_code, notes)
                VALUES (?, ?, 'RATE_LIMIT_CIRCUIT_BREAK', 429, ?)
            """, (now, account_id, f"Backoff for {backoff_seconds}s"))
            conn.commit()

    def reset_sliding_windows(self):
        """Reset RPM counters every 60 seconds."""
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE accounts SET current_rpm_used = 0")
            conn.commit()

    def get_pool_status(self) -> List[Dict[str, Any]]:
        with self._get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM accounts ORDER BY slot_number ASC")
            return [dict(row) for row in cursor.fetchall()]

    def print_health_dashboard(self):
        now = time.time()
        rows = self.get_pool_status()
        print("================================================================================")
        print("⚡ 10-ACCOUNT GOOGLE WORKSPACE SOVEREIGN QUOTA POOL (AIR10 / MIGL)")
        print("================================================================================")
        print(f"{'SLOT':<6} {'EMAIL':<30} {'STATUS':<20} {'RPM USAGE':<12} {'SERVED':<8} {'BACKOFF'}")
        print("--------------------------------------------------------------------------------")
        for r in rows:
            bo = max(0.0, r['backoff_until'] - now)
            bo_str = f"{bo:.1f}s remaining" if bo > 0 else "None"
            rpm_str = f"{r['current_rpm_used']}/{r['quota_rpm']}"
            print(f"[{r['slot_number']:02d}]  {r['email']:<30} {r['auth_status']:<20} {rpm_str:<12} {r['total_requests_served']:<8} {bo_str}")
        print("================================================================================")

if __name__ == "__main__":
    pool = MultiAccountPool()
    pool.print_health_dashboard()
