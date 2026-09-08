# ⚡ Gemini Spark Autonomous Swarm Cortex

> **Central Nerve Center for rajon369963-del's Autonomous Gemini Spark Swarm & ChatGPT Schedules**

This repository acts as the **State Machine & Coordination Blackboard** between:
1. **10 Gemini Spark Web Accounts** (Running via scheduled Tasks on `gemini.google.com`)
2. **10 ChatGPT Scheduled Automation Crons**
3. **Antigravity Local Execution Kernel** (Running on Rajon's Mac)

---

## 📂 Repository Architecture

```text
gemini-spark-cortex/
├── .github/
│   └── workflows/
│       └── auto-verify.yml         # CI verification on Spark commits/PRs
├── tasks/
│   ├── queue/                     # Tasks dispatched by ChatGPT or Developer
│   ├── in_progress/               # Claimed by active Gemini Spark accounts
│   └── completed/                 # Verified results and code commits
├── prompts/
│   ├── spark_account_1_prompt.md  # Scheduled prompt for Account 1 (rajon369963-del)
│   └── conventional_commit_rule.md
└── research/
    └── interconnections/          # Synthesized hyper-graph connections & notes
```

---

## 🚀 How Gemini Spark Account 1 Operates Autonomously

1. **Schedule**: Configured in Gemini Web **"Tasks"** tab to run every hour at `:00`.
2. **Action**:
   - Inspects `tasks/queue/`.
   - Reads the task specification.
   - Performs deep web research & code synthesis using Gemini Spark's 2M token context.
   - Creates a new branch: `spark-1/task-<id>`.
   - Applies changes and commits with Conventional Commit (`feat: ...`).
   - Opens a Pull Request into `main`.
3. **Verification**: Antigravity locally verifies the PR and merges.
