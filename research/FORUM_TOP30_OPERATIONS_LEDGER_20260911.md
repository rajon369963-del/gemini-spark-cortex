# Forum / Practitioner Top-30 Operations Ledger — 2026-09-11

Purpose: evidence-aware operating hypotheses for TRI_REPO_FEDERATION_V2. Forum posts are **discovery signals**, not authoritative truth. Current GitHub Docs and direct repo/CI readback must verify any platform-specific rule before mutation.

## Top 30 hacks / tips / tricks / insights

1. **Centralize truly common CI as reusable workflows**; keep product repos as thin callers to reduce copy-paste drift.
2. **Use composite actions for shared step bundles and reusable workflows for job/pipeline orchestration**; do not emulate GitLab YAML include hierarchies blindly.
3. **Pass configuration explicitly through documented inputs/secrets**; do not assume reusable workflow environment/secrets behave like textual YAML inclusion.
4. **Pin critical third-party Actions to full immutable commit SHAs** and verify the SHA belongs to the intended upstream repository.
5. **Pin/release critical cross-repo reusable workflow versions deliberately**; do not let production gates float silently on `@main`.
6. **Treat shared workflow changes like product releases**: consumer list, compatibility test, migration note and rollback SHA.
7. **A reusable workflow is not itself a standalone required status check**; enforcement belongs to the caller workflow/check or supported required-workflow mechanism.
8. **Test skipped-job semantics explicitly**: optional/skipped internal jobs in reusable workflows can unexpectedly propagate into downstream `needs` and gate behavior.
9. **Start GitHub Actions permissions from least privilege** (`permissions: {}` where practical) and grant only the scopes each job needs.
10. **Prefer OIDC/short-lived federated credentials over long-lived cloud secrets** when the target provider supports it; constrain the trust policy.
11. **Treat `.github/workflows/**` and release automation as production/security code**; use independent review/CODEOWNERS where practical.
12. **Use an existing workflow security analyzer (for example zizmor) as a candidate wheel before inventing a custom scanner**; validate it on the repo first.
13. **Artifact attestations prove build provenance/integrity, not software correctness**; consumers must actually verify attestations for them to add value.
14. **Dependency review belongs near dependency submission/order-sensitive steps**; bounded retry/backoff is better than racing incomplete dependency snapshots.
15. **One stable aggregate required gate can reduce matrix/check-name drift**, but it must fail if any required dependency failed or was unexpectedly skipped.
16. **Do not assume `cancel-in-progress: true` means active processes terminate instantly**; runner/process cleanup behavior needs empirical tests, especially for long/self-hosted jobs.
17. **Namespace concurrency groups by workflow/ref/effect**; GitHub concurrency group names can otherwise cancel unrelated workflows.
18. **Queued/concurrency systems can themselves stall**; treat a queued/pending status as a state to observe and escalate, not proof that work will eventually run.
19. **Manual dispatch buttons depend on a valid dispatchable workflow on the default branch**; reusable `workflow_call` templates do not become standalone UI workflows automatically.
20. **New Actions `parallel`/background-step features are candidates, not universal defaults**; run small compatibility canaries before putting them into agent setup/release-critical workflows.
21. **Recent Copilot-agent reports show new parallel-step syntax can break agent setup flows**; do not adopt freshly shipped Actions features in critical automation without canary evidence.
22. **Multiple coding agents should not edit one working tree**; separate branch + git worktree materially reduces file-level collisions and accidental reversions.
23. **Worktrees isolate files, not databases/ports/env/services**; parallel runtime tests need separate service resources or serialization too.
24. **Multi-repo agent work is more reliable when decomposed by repository** with contract/interface first, repo-specific sub-effects, dependency order, then final integration testing.
25. **Use a coordinator/arbitration lane for cross-repo integration** rather than allowing every worker to become its own multi-repo supervisor.
26. **Every incoming agent must ACK current HEAD/diff/lease before write**; stale transcript context never overrides live Git state.
27. **One primary mutation effect per scheduled run** reduces collision surface; cross-repo knowledge discovery can remain read-only until the effect is selected and leased.
28. **Every external effect needs an idempotency key + read-after-write verification**; command exit code or schedule firing is not physical effect proof.
29. **External clean reproduction beats repeated internal self-seals**: optimize public repos for clone -> run -> understand -> useful issue/PR.
30. **No vanity automation**: no fake stars, spam outreach, fabricated users, inflated count claims or forum anecdotes promoted as consensus. Growth should follow useful, reproducible engineering.

## Fresh practitioner/forum evidence sampled

- Reddit r/devops, 2026-07-28, “github actions central repo” — reusable workflows/composite actions as central-pipeline patterns; community warns about env/secrets/input differences: https://www.reddit.com/r/devops/comments/1v8wshu/github_actions_central_repo/
- GitHub Community #170628 — reusable workflow cannot independently be selected/run as a required check; caller/check is the enforceable surface: https://github.com/orgs/community/discussions/170628
- GitHub Community #189172 — skipped internal reusable-workflow jobs can auto-skip dependents: https://github.com/orgs/community/discussions/189172
- GitHub Community #202297, 2026-07 — `cancel-in-progress` and actual process termination/resource release can diverge: https://github.com/orgs/community/discussions/202297
- GitHub Community #206259, 2026-08-30 — concurrency queue/pending jobs can stall in real deployments: https://github.com/orgs/community/discussions/206259
- Reddit r/devops, 2026-09-01 — practitioner concern about static CI secrets; move toward runtime/short-lived identity: https://www.reddit.com/r/devops/comments/1w4h8lc/how_do_you_handle_cicd_credentials_using_github/
- Reddit r/ClaudeAI, 2026-02-08 — multi-agent same-repo collision experience; separate git worktrees/branches: https://www.reddit.com/r/ClaudeAI/comments/1qzduim/stop_running_multiple_claude_code_agents_in_the/
- Reddit r/ClaudeAI, 2026-07-31 — isolation reported as more important than raw parallelism during multi-agent audits: https://www.reddit.com/r/ClaudeAI/comments/1vbyw1w/ran_3_claude_code_agents_in_3_separate_git/
- Reddit r/AI_Agents, 2026-07-08 — worktrees alone do not isolate databases, ports, env or services: https://www.reddit.com/r/AI_Agents/comments/1ur1lhq/i_solved_parallel_multi_agents_workflows/
- GitHub Community #186469, 2026-02 — GitHub architect/community guidance: multi-repo background-agent work is best decomposed into repo-specific tasks with clear interfaces/versioning and final integration: https://github.com/orgs/community/discussions/186469
- GitHub Community #206612, 2026-09-02 — recent compatibility failure report involving newly shipped parallel steps and Copilot agent setup: https://github.com/orgs/community/discussions/206612
- Reddit r/devops, 2026-06 — post-supply-chain-incident hardening discussion: SHA pins, OIDC, least privilege, workflow review, zizmor candidate: https://hr.reddit.com/r/devops/comments/1tw4p08/after_the_tjactions_supply_chain_attack_i_wrote/

## Current GitHub documentation cross-checks

- Secure use: least privilege, full-SHA action pinning, OIDC guidance: https://docs.github.com/en/actions/reference/security/secure-use
- Artifact attestations: provenance/integrity and verification boundary: https://docs.github.com/en/actions/concepts/security/artifact-attestations
- Dependency review: ordering, snapshot warnings, bounded/exponential retry guidance: https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review
- Workflow concurrency: group/cancel/queue semantics: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
- OIDC for cloud providers/reusable workflows: https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments

## Promotion rule

No item above becomes a mandatory repo mutation solely because it appears here. Required path:

`FORUM_SIGNAL -> CURRENT_DOC_CHECK -> CURRENT_REPO_FIT -> SMALLEST_CANARY -> NEGATIVE/NO_REGRESSION TEST -> INDEPENDENT READBACK -> ADOPT/ADAPT/REJECT KNOWLEDGE_ATOM`
