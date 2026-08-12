# Changelog

All notable changes to this project are documented in this file.

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

[0.3.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.3.0
[0.2.0]: https://github.com/yousef555khg-beep/project-lead/releases/tag/v0.2.0
[0.1.0]: https://github.com/yousef555khg-beep/project-lead/commit/2225d9c
