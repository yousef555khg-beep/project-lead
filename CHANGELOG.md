# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

## [0.6.0] - 2026-08-14

### Changed

- Project work now uses three evidence-based lanes: Fast by default, Standard for bounded multi-file work, and Elevated only for concrete high-risk areas.
- Fast work no longer creates an independent review task. The controller accepts it after inspecting the real diff, worktree, and focused fresh checks.
- Standard work receives one batched Terra review after the deliverable is stable, with at most one incremental repair review. Minor findings do not cause a return.
- Elevated work retains independent Sol review for architecture, authorization, privacy and regulated personal data, cryptography and security compliance, payments, destructive behavior, data safety, migrations, concurrency, shared contracts, cross-module integration, deployment, and release.
- No objective may launch a third automatic review. After two returns, the controller explains the root cause and waits for a user-approved revised plan.
- User progress updates now default to four plain-language lines and hide internal ledgers, hashes, model names, and review identifiers unless they explain a real blocker.
- Detailed skill-installation transaction rules moved from the core skill into a progressive reference loaded only after exact candidate approval. The normal instruction surface fell from 5,314 to about 1,210 words without removing installation safety checks.
- The public English and Chinese introductions now explain automatic installed-skill selection, bounded read-only discovery, and the user-approval boundary before installation.

### Added

- A self-contained skill-discovery workflow for complex projects and evidence-backed capability gaps, with no dependency on `find-skills`.
- Structured read-only public search, bounded privacy-preserving queries, complete static candidate-closure inspection, and explicit no-result handling.
- Short recommendations describing each candidate's function, project-specific value, and available trust or risk evidence.
- Candidate-level lifecycle records, orthogonal user/capability blockers, and explicit same-candidate second-opinion handling.
- A parsed safety-contract validator plus adversarial regression tests for comments, contradictory rules, mixed-negation clauses, package runners, mutable approval labels, and false completion.
- Risk-lane regression tests and fresh-agent pressure scenarios covering Fast, Standard, and Elevated behavior.

### Safety

- Discovery is deduplicated by project and capability gap across phase-name changes; routine work and deadline pressure do not trigger searches.
- Discovery cannot execute candidate content or install, update, or enable a skill. The user must approve the repository, exact commit, full-tree digest, skill path, access/effect manifest, method, target, and target-path binding before a separate copy-and-verification task.
- Candidate instructions are untrusted evidence. Opaque or unresolved trees, hooks, downloads, links, submodules, LFS objects, binaries, and dependency code fail closed; installation runs no candidate code and writes only the approved bound target plus same-parent transaction/staging/rollback entries.
- Installation traverses from a trusted root with no-follow `openat`/`fstat`, requires exclusive parent mutation and loader quiescence, and commits a verified sibling tree only through atomic no-replace or exchange; unverified rollback enters an explicit cleanup-required blocker.
- A durable fsynced transaction record and loader startup gate preserve the blocker across process or host failure and require recovery reconciliation before the target can be enabled.
- Staged files and directories are fsynced before preparation completes, and the bound parent is fsynced after every commit or rollback before durable success is recorded.
- The durable transaction record remains loader-excluded as startup-gate proof; staging and rollback siblings must be removed, verified absent, and parent-fsynced before loader resumption.
- Loader recovery has two explicit durable terminal outcomes: verified installation, or verified restoration after cleanup; restoration never becomes evidence that the new capability was installed.
- Precommit and post-commit failures converge on verified restoration, mark the candidate `install_failed`, and retain the capability blocker instead of leaving it `installing`.
- `approved` or `declined` is not treated as capability evidence: dependent scope remains blocked until `installed_verified`, explicit scope removal or deferral, or an approved verified alternative.

## [0.5.0] - 2026-08-14

### Added

- Automatic supporting-skill routing: controllers choose the minimum necessary available skill from the task evidence, record the decision, and give the user a short reason instead of requiring the user to remember skill names.
- Bounded routes for throwaway prototypes, read-only architecture reports, interface design, interaction design, and browser-rendered web acceptance.
- A reproducible structural regression check for the skill-routing contract.

### Safety

- Routine isolated work explicitly selects no supporting skill; controllers may use at most one discovery or design skill per phase and must not run every skill "just in case."
- Prototypes remain isolated from production state; architecture reports cannot approve architecture or bypass independent review; browser evidence cannot replace native iOS, watchOS, or WeChat Mini Program evidence.

## [0.4.0] - 2026-08-14

### Added

- An architecture routing decision: Sol may draft a no-code system architecture decision record for high-impact, cross-module work; Terra remains the default for accepted module architecture and implementation.
- Review-ready batching, risk-based reviewer selection, immutable candidate fingerprints, incremental repair review, and a two-RETURN circuit breaker.

### Changed

- Routine bounded module review now defaults to an independent `gpt-5.6-terra high`; elevated-risk review defaults to an independent `gpt-5.6-sol xhigh`.
- Related work-in-progress repairs are consolidated before review, and full-repository rescans now require a recorded cross-cutting or uncertain-impact reason.

### Safety

- The authoring controller cannot review its own system architecture record. A separate reviewer must approve it before dependent work is dispatched, and an uncertain classification is treated as system architecture.
- Duplicate review events cannot rerun an unchanged candidate or convert an unchanged `RETURN` into `APPROVE`; circuit breaking pauses wasteful loops but never waives repair review.

## [0.3.2] - 2026-08-13

### Added

- A visible controller closure receipt in the original executor task after independent acceptance, so later task history shows that the controller accepted the result.

### Safety

- The receipt is not new work, requires no executor reply, is not sent for an unaccepted candidate, and is deduplicated by task plus accepted candidate.

## [0.3.1] - 2026-08-13

### Added

- A safe approval-card fallback when a controller can see `waitingOnApproval` but cannot read the card's exact command or confirmation text.
- Public synchronization of the installed completion-relay rules, so a controller does not mistake dispatch acknowledgement for executor completion.

### Safety

- A controller must not guess approval-card details from task context or send a clarification message to an executor frozen by that card.
- The original approval card remains the source of truth; the controller tells the user when its contents are unavailable.

## [0.3.0] - 2026-08-13

### Added

- Immediate controller-to-user relay for executor command approvals, confirmations, and required user input.
- A `blocked_on_user` ledger state with task/action notice deduplication and resume-time re-notification.

### Safety

- The controller never approves on the user's behalf and does not use the 30-minute Luna fallback for an approval blocker already reported by a task.
- A sidebar `running` label cannot clear a user-action blocker without executor evidence.

## [0.2.0] - 2026-08-12

### Added

- A bounded fallback for tasks with 30 minutes of no substantive progress.
- A single status-only `gpt-5.6-luna` follow-up when a fresh snapshot remains unclear.
- Explicit recovery of nonterminal task handles when a controller starts or resumes.
- An explicit one-owner rule and evidence requirements for handing off abnormal nonterminal work.
- Sanitized real-world case studies for Yuji and Shengxue Youpin.
- Behavioral pressure-test records for duplicate routing, authority boundaries, independent review, and stale-task handling.
- Contribution guidance and GitHub issue templates.

### Changed

- The control ledger now records last substantive progress and whether the stale fallback was used.
- Event-driven waiting now defines substantive progress and rearming behavior.

### Safety

- The fallback cannot modify code, review, accept, restart, or create tasks.
- The same silent period cannot trigger repeated Luna follow-ups.
- The skill does not create heartbeat, cron, recurring automation, timer loops, or periodic polling.
- The documentation no longer implies background monitoring after controller termination.

## [0.1.0] - 2026-08-11

### Added

- Initial public release of `project-lead`.
- Controller/executor role separation, ownership-aware routing, independent code review, and evidence-based acceptance.

[Unreleased]: https://github.com/yousef555khg-beep/project-lead/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.5.0
[0.4.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.4.0
[0.3.2]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.2
[0.3.1]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.1
[0.3.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.0
[0.2.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.2.0
[0.1.0]: https://github.com/yousef555khg-beep/project-lead/commit/2225d9c
