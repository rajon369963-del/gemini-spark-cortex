#!/usr/bin/env python3
"""
Unit and Dry Test Suite for 10-Account Workspace Quota & Failover Pool
"""
import sys
import os
import unittest
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.multi_account_pool import MultiAccountPool

class TestMultiAccountPool(unittest.TestCase):
    def setUp(self):
        # Use isolated test database
        self.test_db = f"/tmp/test_account_pool_{int(time.time()*1000)}.sqlite"
        self.pool = MultiAccountPool(db_path=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_pool_initialization_ten_accounts(self):
        status = self.pool.get_pool_status()
        self.assertEqual(len(status), 10, "Pool must have exactly 10 account slots")
        primary = [acc for acc in status if acc["is_primary"] == 1]
        self.assertEqual(len(primary), 1, "Exactly one primary account must exist")
        self.assertEqual(primary[0]["email"], "lakhidas168@gmail.com")
        self.assertEqual(primary[0]["auth_status"], "ACTIVE_AUTHENTICATED")

    def test_round_robin_selection(self):
        acc1 = self.pool.get_next_available_account()
        self.assertEqual(acc1["email"], "lakhidas168@gmail.com")
        self.pool.record_request(acc1["id"], status_code=200, latency_ms=45.0)

    def test_429_circuit_breaker_and_auto_failover(self):
        # Simulate primary account hitting 429 rate limit
        primary = self.pool.get_next_available_account()
        self.assertEqual(primary["email"], "lakhidas168@gmail.com")
        
        self.pool.report_rate_limit(primary["id"], backoff_seconds=30.0)
        
        # Next account selected must be slot 2 (migl.spark.node02@gmail.com)
        failover = self.pool.get_next_available_account()
        self.assertNotEqual(failover["email"], "lakhidas168@gmail.com", "Primary should be circuit-broken")
        self.assertEqual(failover["email"], "migl.spark.node02@gmail.com", "Failover should shift to node02")
        print(f"PASS: 429 Circuit breaker triggered. Failover shifted cleanly to {failover['email']}.")

if __name__ == "__main__":
    unittest.main()
