# AIR10 / MIGL — TRI-REPO 10-SCHEDULE FEDERATION V2

Status: CANONICAL_OVERLAY_V2_ON_MERGE
Date: 2026-09-11
Scope: two authorized ChatGPT Plus accounts, 5 scheduled workers each (10 total), three public product repositories, one shared control plane.

## 0. PURPOSE — EXTEND, DO NOT REBUILD

This is an overlay on the existing AIR10/MIGL coordination fabric. It does **not** create a second bus or replace existing Drive/cortex receipts, leases, watermarks, task files, or founder directives.

Three maintained product repositories:

- REPO_A = `rajon369963-del/sovereign-study-commons-india` — study-data commons, learner/data/provenance/adoption surface.
- REPO_B = `rajon369963-del/civex-progressive-bridge` — progressive tool disclosure, routing, packaging, benchmark/reliability surface.
- REPO_C = `rajon369963-del/sovereign-quant-os` — failure-oriented trading execution kernel, idempotency, reproducibility, quant reliability surface.

Shared control plane / knowledge-skill-schedule registry:

- CONTROL = `rajon369963-del/gemini-spark-cortex`.

The three product repos remain separate because their code, safety boundaries, release semantics and users differ. Share **mechanisms, skills, tests, workflow patterns, evidence schemas and learnings**, not blind code copies.

Authorized multi-account use is allowed only within each account's normal permissions and provider terms. Never use account switching to bypass quotas, rate limits, safety gates, billing, identity, or access controls. Never share account credentials/tokens between schedules.

## 1. FEDERATION INVARIANT

Every worker follows this order:

`FRESH HEADS -> ACK RECEIPTS -> LEASE CHECK -> PICK ONE EFFECT -> ISOLATED CHANGE -> TEST -> READBACK -> RECEIPT -> CROSS-REPO KNOWLEDGE ATOM`

Each run must minimally fresh-read HEAD/default branch and critical health signal for A, B and C, plus the newest relevant CONTROL receipt. Then choose **one primary mutation target**. A second repo may be inspected/read-only for transfer evidence. Do not spray writes across all repos in one run.

Default productive budget over a rolling window:

- ~20% REPO_A
- ~20% REPO_B
- ~20% REPO_C
- ~40% worker's original mission

This is a fairness target, not a per-run quota. Highest verified severity wins. Over any rolling 3 productive runs, each repo should receive at least one meaningful fresh inspection unless frozen/blocked/explicitly deprioritized.

## 2. CURRENT REPO-SPECIFIC ADAPTERS

### A — Sovereign Study Commons India

Treat learner value, provenance, licensing, semantic identity, remote HF/Drive parity and public endpoint health as separate evidence gates. Existing data/checksum success must not be promoted into learner-value proof. Prefer commit-bound dataset manifests and bounded public-surface checks. Current governance is protected but historically may have privileged-bypass/trigger-coverage seams; verify current branch/rules state before each governance claim.

High-value transfer consumers from B/C: causal state readback, fail-closed negative fixtures, idempotent receipts, circuit-breaker thinking, reproducible release/capsule discipline, fault-injection mentality.

High-value exports to B/C: provenance/license court, truth-labelled status vocabulary, real-user/adoption boundary, evidence-linked issue templates, negative-test discipline.

### B — CIVEX Progressive Bridge

Treat routing latency, context reduction and routing quality as separate metrics. Internal catalog benchmarks are not independent comparative proof. Prioritize deterministic routing-recall fixtures, host-isolated built-wheel tests, API/docs parity, package provenance, clean CI matrices and branch governance. Verify current branch protection because it may differ from A/C.

High-value transfer consumers from A/C: provenance labels, deterministic answer-key fixtures, failure injection, restart/concurrency tests, forensic capsule/manifest discipline.

High-value exports to A/C: progressive disclosure, shadow-schema/JIT hydration, causal pre/post hash verification, circuit breaker, headroom/log compression, large-tool-catalog ergonomics.

### C — Sovereign Quant OS

Position as failure-oriented execution infrastructure. Keep simulation/test evidence separate from real-money venue behavior and PnL. Never call basis carry risk-free. Preserve exact benchmark hardware/environment/methodology. Protect idempotency, WAL, watchdog, recovery, portability and claim hygiene. Old cached GitHub SHA views may remain distinct from active-DAG privacy state; report them separately.

High-value transfer consumers from A/B: provenance/status vocabulary, progressive tool disclosure, benchmark answer keys, contributor/adoption discipline, data truth labels.

High-value exports to A/B: concurrency race tests, WAL/idempotency patterns, watchdog/dead-man thinking, crash/restart/orphan recovery, portable forensic capsule + SHA ledger, adversarial multi-court verification.

## 3. TEN-LANE COMPLEMENTARY ROLE MAP

Do not rename a user's existing schedule merely to match this table. Preserve its original mission and apply the nearest overlay lane. Account A currently maps AIR10-01..05 directly. Account B's five existing schedules should map to lanes 06..10 by closest function; if a role conflicts, preserve the original role and add only the federation duties.

1. **Truth Radar / Canonical Controller** — detect README/API/workflow/release/blackboard truth drift across all three repos; maintain bounded truth ledger.
2. **Pain Hunter / Problem Market** — latest-first learner/developer/trader/maintainer pain; turn verified recurring pain into issue candidates and regression fixtures.
3. **Interconnection² Forge** — discover causal A<->B<->C transfers; smallest adapter + compatibility test + kill condition; reject analogy-only transfers.
4. **Venture Builder / Maintainer** — implement highest-Pareto reversible fixes, contributor surfaces and product-value improvements; reuse wheels first.
5. **Independent Reality Court** — producer != verifier; falsify claims, rerun tests, inspect actual Actions/release/Drive evidence; no self-report PASS.
6. **Release & Supply-Chain Steward** — CI/reusable workflows, dependency pinning, package/release provenance, artifact attestations/SBOM where useful, branch/ruleset hygiene.
7. **Community & Adoption Steward** — contributor docs, good-first-issues, reproducible demos, external clone/run evidence, issue/PR quality, zero spam/fake stars.
8. **Security & Privacy Court** — least privilege, secret exposure, workflow injection, OIDC opportunities, dependency/action provenance, cached-history disclosures, unsafe public data.
9. **Repro & Benchmark Court** — clean sandbox, OS/Python matrix, benchmark methodology, answer-key/negative fixtures, performance distributions, release asset digest readback.
10. **Federation Steward / Arbitration Court** — dedupe ownership, leases, cross-repo skill/schedule version drift, unresolved conflicts, final cross-repo receipt consistency.

## 4. TOP-30 2026 FORUM/PRACTITIONER UPGRADES — APPLY AS HYPOTHESES, VERIFY BEFORE MUTATION

These are operating rules synthesized from current GitHub Community / Reddit DevOps / AI-agent practitioner discussions. They are **not authority by themselves**; verify current GitHub documentation/tool behavior and test locally/CI before promotion.

1. **Central reusable workflows, thin repo callers** — avoid copy-paste CI drift across repos; central logic belongs in a controlled repo when semantics truly match.
2. **Pin cross-repo reusable workflows/actions to immutable commit SHA** for reproducibility; avoid floating `@main` for critical gates.
3. **Treat shared-workflow updates as releases** — version, changelog, compatibility test, consumers list, rollback SHA.
4. **Do not assume reusable workflow environment/secrets semantics** — explicitly pass documented inputs/secrets; test caller/callee boundaries.
5. **Least-privilege `GITHUB_TOKEN` per job** — start from `permissions: {}` when practical and grant only required scopes.
6. **Prefer OIDC/short-lived credentials to long-lived cloud secrets** where the target service supports it.
7. **Pin third-party Actions to trusted full SHAs**; record upstream repo/version/license and refresh deliberately.
8. **Security-review workflow changes like production code** — CODEOWNERS or explicit independent review for `.github/workflows/**`, reusable workflows and release automation.
9. **Run a workflow linter/security analyzer (e.g. zizmor) as a candidate wheel** before custom security logic; test compatibility first.
10. **One required aggregator/gate check** can reduce branch-protection check-name drift when many matrix jobs exist; gate must fail if any required dependency fails/skips unexpectedly.
11. **Strict required checks / up-to-date branches for high-risk repos**; do not infer merge safety from a green stale branch.
12. **Merge queue only when repo traffic justifies it**; verify initial-branch/bypass behavior because rules can create lockouts.
13. **Know concurrency semantics** — `cancel-in-progress` is scheduling intent, not proof every process terminated instantly; verify runner cleanup for long/self-hosted jobs.
14. **Avoid multiple AI agents sharing one working directory** — one effect -> one branch/worktree/lease. Parallel read-only research is safer than parallel edits.
15. **Incoming agent ACKs current HEAD/diff/lease before writing**; stale context never overrides live Git state.
16. **Read-before-mutate + read-after-write** — success exit code is insufficient; verify target state/hash/status after mutation.
17. **Idempotency key every external effect** — issue creation, comments, releases, uploads, dispatches and Drive writes need a stable effect ID/dedupe check.
18. **Bound retries with jitter/backoff and rate-limit awareness**; persistent failure becomes a typed blocker/dead-letter, not an infinite retry storm.
19. **Do not use schedule firing as effect proof** — scheduled event -> workflow started -> required job completed -> target readback are distinct receipts.
20. **Prefer event-driven/webhook/repository-dispatch fan-in only when necessary**; scheduled workers should not build another always-on custom control service if GitHub-native mechanisms suffice.
21. **Share knowledge as typed atoms, not raw chat dumps** — mechanism, source SHA, evidence, target, compatibility test, expiry/freshness, rollback.
22. **Progressive context disclosure** — schedules first read compact health/index/receipt, hydrate full files only for selected effect; borrow CIVEX's shadow-schema/JIT principle.
23. **Negative tests are mandatory for truth gates** — deliberately broken fixture must fail; a test suite that cannot detect a known bad state is not a court.
24. **Build once / verify immutable artifact** — release consumers should verify exact digest rather than rebuilding different bytes at each stage.
25. **Artifact provenance/attestation is separate from correctness** — provenance proves origin/build identity, not semantic quality; use both when useful.
26. **Dependency updates need grouping + bounded review** — reduce bot PR noise while preserving security urgency; never blind-auto-merge broad dependency changes.
27. **Exact check names/sources matter** — required checks can drift or be spoofable; where supported bind required status to expected GitHub App/source and verify names after workflow changes.
28. **Benchmark speed + quality + budget together** — latency-only optimization can silently reduce routing accuracy, correctness or safety; track recall/error/false-positive metrics.
29. **External reproduction beats self-certification** — prioritize unrelated clean clone/run, issue/PR evidence and reproducible public demos over more internal “100%” seals.
30. **No vanity automation** — no fake stars, mass unsolicited outreach, issue spam, fabricated users, inflated “100x” counts, or unverified competitor generalizations. Community growth must come from useful evidence-backed work.

## 5. CROSS-REPO KNOWLEDGE ATOM CONTRACT

Every accepted transfer emits a compact durable atom in the existing CONTROL/bus surface:

```text
KNOWLEDGE_ATOM_ID:
CREATED_AT:
SOURCE_REPO:
SOURCE_SHA:
SOURCE_MECHANISM:
SOURCE_EVIDENCE:
TARGET_REPO:
TARGET_PROBLEM:
TRANSFER=ADOPT|ADAPT|REJECT:
SMALLEST_ADAPTER:
COMPATIBILITY_TEST:
NO_REGRESSION_TEST:
ROLLBACK:
OWNER:
VERIFIER:
FRESH_UNTIL / RECHECK_TRIGGER:
STATUS:
```

A shared mechanism may be reused by all three repos only if each target passes its own compatibility test. “Works in C” never implies “safe in A/B.”

## 6. SHARED SKILL CONTRACT

Canonical skills live in CONTROL; product repos consume pinned/versioned knowledge rather than maintain divergent copies. A schedule may promote a repeated successful pattern into a shared skill only after:

`>=2 independent successful uses -> documented inputs/outputs -> failure/kill conditions -> target repo adapters -> verifier readback -> version tag/commit SHA`

Skill updates must include `SKILL_VERSION`, `SOURCE_SHA`, `CONSUMERS`, `BREAKING_CHANGE`, `MIGRATION`, `ROLLBACK_SHA`. If a skill is merely experimental, mark `CANDIDATE`, not `CANONICAL`.

Do not auto-copy a skill file into three repos. Prefer one canonical skill plus tiny repo-specific adapters/pointers. This prevents drift.

## 7. SHARED SCHEDULE CONTRACT

Schedules share **policy and state**, not credentials or quota. Every schedule reads the current federation version from CONTROL before selecting work. Store only non-secret schedule metadata: schedule ID/title/lane/account alias (non-sensitive), cadence, last evidence receipt, repo watermark, capability, status.

A schedule mutation must be versioned and reversible. Never silently change acceptance criteria or role identity. If a schedule prompt is stale relative to CONTROL, newest verified CONTROL policy wins unless it conflicts with a higher-priority founder directive or safety/platform rule.

Second Plus account limitation: one ChatGPT session cannot directly mutate automations belonging to another account. Therefore CONTROL is the handoff surface. Account B workers must ingest this overlay from CONTROL or be updated while logged into that account. Do not claim cross-account schedule mutation without direct readback from that account.

## 8. COLLISION / LEASE / OWNERSHIP LAW

Before mutation:

1. Read repo HEAD + target file/issue/PR current state.
2. Read newest relevant receipt and lease.
3. Claim one `EFFECT_ID` with TTL/owner.
4. Use branch/worktree isolation for code/docs mutation.
5. Re-read diff before push/PR.
6. Producer runs tests; independent lane verifies before promotion when risk is material.
7. On `write_uncertain`, inspect target state before retrying.
8. On conflict, do not overwrite; rebase/reconcile or handoff.

Work-steal only unowned/unleased effects. Never duplicate an in-flight sibling effect merely because another repo appears idle.

## 9. TRI-REPO TRANSFER GRAPH — HIGH-VALUE STARTING EDGES

- B `progressive disclosure/JIT hydration` -> A/C schedule context reduction and tool discovery.
- B `CIVeX pre/post hash + circuit breaker` -> A ingestion/sync and C external adapter verification.
- A `provenance/license/status vocabulary` -> B benchmark claims and C market-data/research provenance.
- A `real-user/adoption ceiling` -> B/C public claim discipline; external reproduction is a separate promotion gate.
- C `WAL/idempotency/in-flight event barrier` -> A ingestion dedupe and B concurrent hydration/cache mutation safety where causal fit exists.
- C `watchdog/restart/orphan recovery` -> A scheduled sync and B tool-execution daemon resilience.
- C `forensic capsule + SHA ledger` -> A dataset releases and B package/benchmark releases.
- A/B `answer-key negative fixtures` -> C scenario/venue-model regression quality.
- A/C `failure-oriented postmortem` -> B routing-quality regressions and contributor docs.

Each edge is a candidate, not automatic authorization.

## 10. REPO-SPECIFIC PRIORITY QUEUES

### REPO_A queue
1. Current truth drift / stale scheduled Pages freshness.
2. Governance trigger coverage and privileged-bypass truth.
3. Provenance/license UNKNOWN assets.
4. First reproducible commit-bound dataset snapshot contract.
5. Real external learner/contributor evidence without spam or private data.

### REPO_B queue
1. Branch/rules protection and signed/reviewed main governance.
2. Routing-quality/context-budget deterministic benchmark (not latency only).
3. Built-wheel host-isolated install/import/CLI matrix.
4. API/docs/package provenance and release attestation hygiene.
5. External clean-install reproduction / contributor path.

### REPO_C queue
1. Keep release-engineering baseline frozen unless new evidence/regression appears.
2. Correct remaining bounded claim wording when evidence warrants; simulation != live PnL.
3. External independent clone/run and issue/PR evidence.
4. Venue/testnet adapter semantics: PostOnly, partial fills, precision/min lot, reconnect/retry, actual-filled-qty neutrality.
5. Quant reliability tooling wedge: reusable failure-injection harness before any profitability claim.

## 11. EVERY-RUN FRESHNESS / RESEARCH LAW

For changing public facts or tool/platform behavior:

`TODAY/24h -> 72h -> 7d -> 30d -> 90d`, then older canonical docs only for stable background.

Forums/Reddit/GitHub Discussions are pain/hypothesis sources. Official docs, actual repository state, workflow logs, release assets and direct readback are verification sources. Never promote a forum anecdote directly to implementation truth.

## 12. MUTATION SAFETY

Default mutation path: `issue/design -> isolated branch -> tests -> PR -> required checks -> merge -> post-merge readback -> receipt`.

No direct-main writes simply because a repo is unprotected. REPO_B being unprotected is a risk signal, not permission to bypass PR discipline.

Do not publish/tag/release/PyPI/HF/production broker operations, rotate/delete secrets, rewrite history, alter destructive governance, spend money, or perform irreversible external actions without the existing explicit authorization gates.

## 13. EVIDENCE AND PROMOTION VOCABULARY

Use bounded statuses:

`OBSERVED -> REPRODUCED -> TESTED_BOUNDED -> CI_VERIFIED -> INDEPENDENTLY_REPRODUCED -> RELEASE_VERIFIED -> REAL_EXTERNAL_USER/CONSUMER -> REPEATABLE_VALUE`

Never skip directly from unit test to production/value/profitability.

For REPO_C specifically:

- `SIMULATION_PASS` != `TESTNET_PASS` != `LIVE_BROKER_PASS` != `PROFITABLE`.
- `DELTA≈0 in tested model` != risk-free.
- low in-memory latency != end-to-end exchange latency.

## 14. OUTPUT / RECEIPT CONTRACT

Every worker ends compactly with:

```text
FEDERATION_VERSION=V2
LANE=
ACKED_RECEIPT_ID=
REPO_A_HEAD=
REPO_B_HEAD=
REPO_C_HEAD=
CONTROL_HEAD=
PRIMARY_EFFECT_REPO=
EFFECT_ID=
LEASE=
RESULT=
FILES_ISSUES_PRS_TOUCHED=
TEST_PROOF=
READBACK_PROOF=
CROSS_REPO_KNOWLEDGE_ATOM=
TRANSFER_SOURCE=
TRANSFER_TARGET=
TRANSFER_VERDICT=
CLAIM_CEILING=
SECURITY_PRIVACY_DELTA=
OWN_RECEIPT_ID=
NEXT_OWNER=
NEXT_EXPECTED_EFFECT=
EXACT_RESUME=
```

## 15. FOUNDER PROTECTION / CONTINUOUS EXECUTION

Do not interrupt Rajon for routine status. Batch only real legal/payment/MFA/CAPTCHA/irreversible/explicit-authorization gates. Persist exact blocker and continue another safe unowned same-spine effect. No audio/TTS from scheduled maintenance workers unless separately requested.

The goal is not maximum activity. The goal is **maximum verified shared progress with minimum duplicated work and minimum truth drift across A, B, C and CONTROL**.
