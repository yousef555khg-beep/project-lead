# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- An architecture routing decision: Sol may draft a no-code system architecture decision record for high-impact, cross-module work; Terra remains the default for accepted module architecture and implementation.

### Safety

- The authoring controller cannot review its own system architecture record. A separate reviewer must approve it before dependent work is dispatched, and an uncertain classification is treated as system architecture.

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

[0.3.2]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.2
[0.3.1]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.1
[0.3.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.0
[0.2.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.2.0
[0.1.0]: https://github.com/yousef555khg-beep/project-lead/commit/2225d9c
