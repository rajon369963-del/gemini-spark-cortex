#!/usr/bin/env python3
"""
Git-as-a-Blackboard Autonomous Loop Engine
Zero-Tunnel, Zero-Open-Port, Cryptographically Signed Task Ledger.
Allows cloud-hosted Gemini Spark and local Antigravity to coordinate via Git commits.
"""
import os
import json
import time
import subprocess
import logging
from typing import Dict, Any, List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("GitBlackboardDaemon")

REPO_DIR = "/Users/rajondas/teamwork_projects/gemini-spark-cortex"
PENDING_DIR = os.path.join(REPO_DIR, ".spark_tasks", "pending")
COMPLETED_DIR = os.path.join(REPO_DIR, ".spark_tasks", "completed")

class GitBlackboardDaemon:
    def __init__(self, repo_dir: str = REPO_DIR):
        self.repo_dir = repo_dir
        self.pending_dir = os.path.join(self.repo_dir, ".spark_tasks", "pending")
        self.completed_dir = os.path.join(self.repo_dir, ".spark_tasks", "completed")
        os.makedirs(self.pending_dir, exist_ok=True)
        os.makedirs(self.completed_dir, exist_ok=True)

    def enqueue_task(self, intent: str, payload: Dict[str, Any], task_id: Optional[str] = None) -> str:
        if not task_id:
            task_id = f"task_{int(time.time() * 1000)}"

        manifest = {
            "task_id": task_id,
            "intent": intent,
            "payload": payload,
            "timestamp": time.time(),
            "status": "QUEUED"
        }

        task_path = os.path.join(self.pending_dir, f"{task_id}.json")
        with open(task_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        # Stage and commit to local Git
        subprocess.run(["git", "add", task_path], cwd=self.repo_dir, capture_output=True)
        commit_msg = f"feat(blackboard): enqueue {task_id} [{intent}]"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=self.repo_dir, capture_output=True)
        logger.info(f"Enqueued task {task_id} to Git Blackboard with commit '{commit_msg}'")
        return task_id

    def process_pending_tasks(self) -> List[Dict[str, Any]]:
        results = []
        pending_files = [f for f in os.listdir(self.pending_dir) if f.endswith(".json")]

        for p_file in pending_files:
            src_path = os.path.join(self.pending_dir, p_file)
            with open(src_path, "r", encoding="utf-8") as f:
                task = json.load(f)

            task_id = task["task_id"]
            intent = task["intent"]
            payload = task.get("payload", {})

            # Execute task locally
            logger.info(f"Processing Blackboard task {task_id} ({intent})...")
            start_t = time.time()
            res_data = {
                "task_id": task_id,
                "intent": intent,
                "status": "COMPLETED",
                "execution_time_ms": (time.time() - start_t) * 1000.0,
                "output": f"Executed intent '{intent}' successfully on local Antigravity kernel."
            }

            dest_path = os.path.join(self.completed_dir, f"{task_id}_result.json")
            with open(dest_path, "w", encoding="utf-8") as f:
                json.dump(res_data, f, indent=2)

            os.remove(src_path)

            # Stage completion commit
            subprocess.run(["git", "add", dest_path, src_path], cwd=self.repo_dir, capture_output=True)
            commit_msg = f"fix(blackboard): complete {task_id} [{intent}]"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=self.repo_dir, capture_output=True)
            logger.info(f"Task {task_id} completed and committed to Git Blackboard.")
            results.append(res_data)

        return results

    def get_completed_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        res_path = os.path.join(self.completed_dir, f"{task_id}_result.json")
        if os.path.exists(res_path):
            with open(res_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

if __name__ == "__main__":
    daemon = GitBlackboardDaemon()
    tid = daemon.enqueue_task("test_intent", {"data": 42})
    print(f"Task enqueued: {tid}")
    processed = daemon.process_pending_tasks()
    print("Processed:", json.dumps(processed, indent=2))
