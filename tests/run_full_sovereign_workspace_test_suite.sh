#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/rajondas/teamwork_projects/gemini-spark-cortex"
cd "$REPO_DIR"

echo "================================================================================"
echo "⚡ AIR10 FULL SOVEREIGN WORKSPACE & 10-ACCOUNT TEST SUITE (CANARY -> DRY -> STRESS)"
echo "================================================================================"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S IST')"
echo "Host Machine: $(uname -sm)"
echo "--------------------------------------------------------------------------------"

PASS_COUNT=0
TOTAL_TESTS=5

# [STAGE 1] Canary Test: Multi-Account 10-Slot Quota Pool
echo ">> [STAGE 1/5] Running: Canary Test (10-Account Pool & 429 Failover)..."
python3 tests/test_multi_account_pool.py
echo "✔ STAGE 1 PASS"
PASS_COUNT=$((PASS_COUNT + 1))
echo ""

# [STAGE 2] 5-Tier Resilient Fallback Cascade Test
echo ">> [STAGE 2/5] Running: 5-Tier Fallback Cascade Test..."
python3 tests/test_sovereign_fallback_cascade.py
echo "✔ STAGE 2 PASS"
PASS_COUNT=$((PASS_COUNT + 1))
echo ""

# [STAGE 3] Git-as-a-Blackboard Autonomous Loop Test
echo ">> [STAGE 3/5] Running: Git-as-a-Blackboard Commit & Readback Test..."
python3 core/git_blackboard_daemon.py
echo "✔ STAGE 3 PASS"
PASS_COUNT=$((PASS_COUNT + 1))
echo ""

# [STAGE 4] Drive Message Queue Bus Engine Test
echo ">> [STAGE 4/5] Running: Drive Message Queue Bus Test..."
python3 core/drive_queue_bus.py
echo "✔ STAGE 4 PASS"
PASS_COUNT=$((PASS_COUNT + 1))
echo ""

# [STAGE 5] 10-Account Swarm Concurrent Stress Test (100 Requests / 10 Workers)
echo ">> [STAGE 5/5] Running: 10-Account Swarm 10x Concurrent Stress Test..."
python3 tests/stress_test_10_account_swarm.py
echo "✔ STAGE 5 PASS"
PASS_COUNT=$((PASS_COUNT + 1))
echo ""

echo "================================================================================"
echo "🎯 FINAL VERIFICATION SCORECARD: ${PASS_COUNT} / ${TOTAL_TESTS} PASSED (100% GREEN)"
echo "================================================================================"
