# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

## [0.9.0] - 2026-08-22

### Added

- Formal implementation, independent review, and long validation now use titled, sidebar-visible standalone Codex tasks created with `create_thread`.
- Every dispatch now selects model and reasoning effort from the current child task's actions, uncertainty, coupling, consequences, and checks, then includes one short task-specific reason in the route notice.
- Before `xhigh` or `ultra`, the controller performs one bounded internal reverse check at the next lower effort; it creates no task and calls no tool, Luna assistant, or comparison model.

### Fixed

- Internal subagents are limited to short read-only helper checks. If a visible task cannot be created, Project Lead reports `blocked_on_visibility` instead of claiming that work was dispatched.
- Parent-project complexity, review lanes, prior routes, and earlier effort levels no longer force new executor tasks into `xhigh`; uncertainty alone also cannot justify escalation.

## [0.8.3] - 2026-08-21

### Added

- Before every task creation or substantive follow-up, the controller now announces the task, selected model, reasoning effort, and actual speed in one non-blocking line; speed is ordinary unless the exact objective already has explicit Fast authorization.
- Automatic routing now chooses supported reasoning effort as well as model: bounded Spark high/xhigh, Terra high/xhigh/Ultra, and read-only Luna medium/high/xhigh.

### Fixed

- Cross-model dispatch no longer uses full-history inheritance, which can silently preserve the controller's Sol route instead of the requested child route.
- Every created task now receives no or bounded history, including a same-route independent reviewer, so review isolation does not depend on model differences.
- Dispatch now verifies an atomically exposed route before work or uses a no-project-access handshake before sending the substantive brief; an unobservable route fails closed as `blocked_on_routing`.
- Spark-to-Terra capacity guards are local to the same objective or logical scope and no longer block unrelated Terra work.
- A follow-up without model and effort fields is no longer treated as an in-place route switch; the logical scope is handed off only after the prior turn is terminal or interrupted, with one active owner.
- Accepted task model and effort are verified before substantive work; any corrected route is announced before redispatch without asking for approval.
- Approval now follows the proposed action and missing authority; Elevated review, local reversible preparation, normal dispatch, and in-scope repair no longer create prose approval requests by themselves.
- `blocked_on_user` is bound to one objective, candidate or scope version, exact action, and authority gap, then cleared or superseded when that identity or need changes.
- Repository plans, designs, source, tests, complex debugging, repeated repair, and long or broad validation must stay with executor tasks instead of accumulating in the controller.
- Elevated risk now strengthens review without automatically creating a separate architecture phase.
- The two-return circuit breaker now has an explicit closeout: Standard uses one evidence-bound root-cause repair without another review; Elevated gets one final independent closure review, never a fourth, and stays `blocked_on_quality` if unresolved.
- Routing validation now covers cross-line follow-up switches, universal Ultra defaults, approval-gated notice synonyms, and bounded Ultra exceptions without false positives.
- The validator now binds the complete core Skill to its reviewed SHA-256, so even a short unknown override fails closed until the changed core and bound digest are reviewed together; semantic scanners remain a second defense.

### Safety

- Real product or security-policy forks, new authority or secrets, irreversible or destructive actions, external side effects, purchases, deployment, release, and user-only platform approval cards still require the user.

## [0.8.2] - 2026-08-20

### Changed

- Child dispatch now uses the platform Standard/default when no service-tier field exists, instead of blocking and asking whether to use Fast.

### Safety

- Project Lead never asks, suggests, recommends, or offers Fast. Fast is used only after an explicit user request for one exact child objective and resets to Standard/default on the next objective.
- Unexpected observable Fast/priority evidence stops further child follow-ups and is reported to the user.

## [0.8.1] - 2026-08-20

### Fixed

- Standard/default speed now applies to every newly dispatched child task and child follow-up, not to the controller's own user-configured speed.
- A controller's Fast/priority state, model-routing authority, and a previous child objective can never authorize or leak Fast service into a new child objective.
- Dispatch fails closed and asks the user when it cannot set and verify Standard service for the child task.

## [0.8.0] - 2026-08-20

### Added

- A reusable project-scoped Luna information assistant for large or repetitive read-only evidence, including task-report, log, test-output, blocker, approval, terminal-state, deduplication, and plain-language update extraction.
- Event-driven completion relay that keeps the controller turn open on exact delegated targets until they finish or need attention.
- A separate speed-tier contract: controllers and child tasks default to Standard, while Fast requires explicit approval for one objective.

### Changed

- The former "Fast lane" is now named "Low-risk lane" so review intensity cannot be confused with Codex Fast service.

### Safety

- Luna assistance is advisory, source-bound, deduplicated, and reserved for work that materially reduces controller context or cost; routine short updates stay with the controller.
- Luna owns no mutable scope and cannot write code, select execution or review routes, decide architecture, review, accept, mark work complete, call mutating tools, or replace required verification.
- Controllers cannot end with a promised target still accepted, queued, or running; timeouts renew the same cursor-bound event wait without polling, repeated reads, or Luna.
- When event waiting is unavailable, the controller must disclose that automatic relay is not guaranteed; neither Luna nor the 30-minute fallback is presented as a background wake mechanism.
- Model-routing authority never enables Fast/priority service, Fast approval never carries into another objective, and unverifiable child speed fails closed with a user-facing request to disable Fast.

## [0.7.0] - 2026-08-15

### Added

- One-time per-project authorization for automatic Spark/Terra execution-model routing.
- A task-local model decision for every new objective, dispatch, and substantive follow-up, with explicit model overrides instead of inheriting an executor task's current model.
- A strict Spark allowlist for small Fast-lane work and a Terra fallback for ambiguity, complexity, expanded scope, or unavailable Spark capacity.

### Safety

- A completed Spark objective never authorizes Spark for the next objective, including when the same executor task is reused.
- Spark-to-Terra escalation preserves the same owner and task, starts on the next turn, and cannot mark interrupted work complete or create a replacement owner.
- An accepted, running, or queued Spark turn blocks a concurrent Terra fallback until rejection, interruption, or terminal state is confirmed.
- Execution-model routing remains independent of review routing: Standard review stays with Terra, Elevated review stays with Sol, and Spark cannot review its own implementation.

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

[Unreleased]: https://github.com/yousef555khg-beep/project-lead/compare/v0.8.3...HEAD
[0.8.3]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.8.3
[0.8.2]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.8.2
[0.7.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.7.0
[0.6.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.6.0
[0.5.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.5.0
[0.4.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.4.0
[0.3.2]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.2
[0.3.1]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.1
[0.3.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.0
[0.2.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.2.0
[0.1.0]: https://github.com/yousef555khg-beep/project-lead/commit/2225d9c
