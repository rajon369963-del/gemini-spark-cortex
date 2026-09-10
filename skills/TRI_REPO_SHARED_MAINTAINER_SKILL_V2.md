# TRI-REPO SHARED MAINTAINER SKILL V2

Canonical control plane: `rajon369963-del/gemini-spark-cortex`
Consumers: ChatGPT schedules 01-10, Gemini Spark, Hermes, Antigravity, Integrity when authorized.
Product repos: Commons=A, CIVEX=B, Sovereign Quant OS=C.

## Skill contract

Use this skill to share **mechanisms, evidence schemas, workflow patterns, acceptance tests, failure modes and learnings** across the three repos without blindly copying implementation.

Every use begins with live-state hydration:

`CONTROL policy/version -> A/B/C HEAD -> relevant issue/PR/workflow/release -> newest receipt/lease -> selected effect`

Then execute only one primary mutation target per run. Read-only cross-repo comparison is allowed. Use branch/worktree isolation, stable EFFECT_ID, bounded retries, read-after-write and independent verification for material claims.

## Shared primitives

1. `TRUTH_LABELS`: OBSERVED, REPRODUCED, TESTED_BOUNDED, CI_VERIFIED, INDEPENDENTLY_REPRODUCED, RELEASE_VERIFIED, REAL_EXTERNAL_USER/CONSUMER, REPEATABLE_VALUE.
2. `KNOWLEDGE_ATOM`: source repo+SHA+mechanism+evidence -> target problem -> ADOPT/ADAPT/REJECT -> smallest adapter -> compatibility/no-regression test -> rollback -> owner/verifier -> freshness trigger.
3. `EFFECT_IDEMPOTENCY`: every external mutation gets stable EFFECT_ID and preflight dedupe.
4. `LEASE`: one active owner per mutation effect with TTL/resume pointer.
5. `READBACK`: command success is not effect success; inspect exact target state/hash/status after mutation.
6. `NEGATIVE_FIXTURE`: every important truth/reliability gate must prove it can reject at least one known-bad state.
7. `ARTIFACT_IDENTITY`: build/freeze once, publish digest/provenance, verify downloaded bytes; do not silently rebuild different bytes in later stages.
8. `CLAIM_CEILING`: test evidence cannot be promoted to deployment, external value or profitability without separate proof.
9. `PRODUCER_NE_VERIFIER`: final material verification comes from an independent lane/court.
10. `PROGRESSIVE_DISCLOSURE`: first read compact health/receipt/index metadata, hydrate full content only for selected effect.

## Repo adapters

### A — sovereign-study-commons-india
Focus: learner/data/provenance/adoption truth. Import reliability patterns from B/C only when they improve data integrity, release reproducibility, ingestion idempotency, scheduled-sync safety or contributor evidence. Never infer learner value from CI or synthetic fixtures.

### B — civex-progressive-bridge
Focus: tool disclosure/routing/package/reliability. Import A's provenance/status discipline and C's fault-injection/recovery patterns. Pair speed/context metrics with routing recall/error/false positives. Internal catalog results are not independent comparative claims.

### C — sovereign-quant-os
Focus: failure-oriented execution reliability. Import A's evidence/status vocabulary and B's progressive tool/context disclosure. Preserve simulation/testnet/live/PnL boundaries. `delta≈0 under tested assumptions` is not risk-free; in-memory latency is not end-to-end exchange latency.

## Shared GitHub Actions discipline

- Prefer central reusable workflows for genuinely identical orchestration; use thin callers per repo.
- Critical third-party/reusable refs should be pinned to immutable full SHAs where practical.
- Reusable workflows are templates: enforce the caller workflow/check or a ruleset-required workflow run, not an imaginary standalone reusable-workflow check.
- Beware optional/skipped internal reusable-workflow jobs propagating skip semantics into downstream `needs` chains; test the aggregate gate.
- Start with least-privilege `permissions`; grant only required job scopes.
- Prefer short-lived OIDC federation over long-lived cloud credentials when supported.
- Security-review workflow changes; CODEOWNERS/independent review is preferred for `.github/workflows/**` and release automation.
- Do not assume `cancel-in-progress` instantly terminates active processes; long/self-hosted jobs need cleanup/cooperative cancellation tests.
- New parallel/background step features are candidates, not defaults; run compatibility canaries before use in agent setup or release gates.

## Shared multi-agent discipline

- Worktree/branch isolation solves file collisions, not database/port/service collisions. If a task needs runtime services, isolate those resources too or serialize the effect.
- Multi-repo changes should be contract-first and decomposed into repo-specific sub-effects with dependency order; do not let one agent mutate three repos as one opaque transaction.
- Incoming agent must ACK HEAD/diff/lease and current acceptance contract before write.
- Integration court runs after repo-specific effects and checks interface/version compatibility.

## Skill promotion

A candidate shared skill becomes canonical only after >=2 independent successful uses, explicit inputs/outputs, failure/kill conditions, repo-specific adapter tests, verifier readback, version, consumer list, migration note and rollback SHA. Experimental patterns remain `CANDIDATE`.

## Security / privacy / community boundaries

No quota evasion, credential sharing, fake stars, synthetic users, unsolicited spam, fabricated forum consensus, secrets in receipts, or unreviewed sensitive-data publication. Forum anecdotes are discovery signals; official docs and live repo/CI/Drive readback are verification sources.

## Required receipt

`SKILL_VERSION=V2 | LANE | CONTROL_HEAD | A_HEAD | B_HEAD | C_HEAD | EFFECT_ID | PRIMARY_REPO | SOURCE_SHA | TRANSFER | TEST | READBACK | CLAIM_CEILING | OWN_RECEIPT_ID | NEXT_OWNER | EXACT_RESUME`
