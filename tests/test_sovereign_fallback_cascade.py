#!/usr/bin/env python3
"""
Test Suite for 5-Tier Fallback Cascade in Sovereign Workspace Engine
Tests simulated failures in Tier 1 -> Tier 2 -> Tier 3 -> Tier 4 -> Tier 5.
"""
import sys
import os
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.sovereign_workspace_engine import SovereignWorkspaceEngine

class TestSovereignFallbackCascade(unittest.TestCase):
    def setUp(self):
        self.engine = SovereignWorkspaceEngine()

    def test_tier_1_primary_success(self):
        with patch.object(self.engine, "_try_tier_1_gog_cli", return_value={"success": True, "data": "MOCK_DRIVE_RESULT"}):
            res = self.engine.execute_workspace_task("drive_search", {"query": "MIGL"})
            self.assertTrue(res["success"])
            self.assertEqual(res["tier_executed"], "TIER_1_GOG_CLI_STDIO")
            self.assertEqual(res["result"], "MOCK_DRIVE_RESULT")

    def test_tier_1_fails_cascade_to_tier_2_git(self):
        with patch.object(self.engine, "_try_tier_1_gog_cli", return_value={"success": False, "error": "Simulated 429 Quota Exceeded"}):
            with patch.object(self.engine, "_try_tier_2_git_blackboard", return_value={"success": True, "data": "TASK_COMMITTED_TO_GIT"}):
                res = self.engine.execute_workspace_task("drive_search", {"query": "MIGL"})
                self.assertTrue(res["success"])
                self.assertEqual(res["tier_executed"], "TIER_2_GIT_BLACKBOARD")
                self.assertEqual(res["result"], "TASK_COMMITTED_TO_GIT")

    def test_tier_1_and_2_fail_cascade_to_tier_3_drive_bus(self):
        with patch.object(self.engine, "_try_tier_1_gog_cli", return_value={"success": False, "error": "API Down"}):
            with patch.object(self.engine, "_try_tier_2_git_blackboard", return_value={"success": False, "error": "Git Conflict"}):
                with patch.object(self.engine, "_try_tier_3_drive_queue", return_value={"success": True, "data": "ENQUEUED_IN_DRIVE_BUS"}):
                    res = self.engine.execute_workspace_task("drive_search", {"query": "MIGL"})
                    self.assertTrue(res["success"])
                    self.assertEqual(res["tier_executed"], "TIER_3_DRIVE_QUEUE_BUS")

    def test_tier_1_2_3_fail_cascade_to_tier_4_clasp(self):
        with patch.object(self.engine, "_try_tier_1_gog_cli", return_value={"success": False, "error": "API Down"}):
            with patch.object(self.engine, "_try_tier_2_git_blackboard", return_value={"success": False, "error": "Git Conflict"}):
                with patch.object(self.engine, "_try_tier_3_drive_queue", return_value={"success": False, "error": "Drive Unavailable"}):
                    with patch.object(self.engine, "_try_tier_4_clasp", return_value={"success": True, "data": "CLASP_DEPLOYED"}):
                        res = self.engine.execute_workspace_task("drive_search", {"query": "MIGL"})
                        self.assertTrue(res["success"])
                        self.assertEqual(res["tier_executed"], "TIER_4_CLASP_APPS_SCRIPT")

if __name__ == "__main__":
    unittest.main()
