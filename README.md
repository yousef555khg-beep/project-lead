# Project Lead

English | [简体中文](README.zh-CN.md)

A Codex skill for governing multi-module projects through disciplined delegation, independent review, and verified acceptance.

## Overview

`project-lead` turns a regular Codex conversation into a project control layer.

It is designed for product and engineering work spanning multiple modules, worktrees, repositories, or execution tasks. The controller owns intent, scope, routing, dependency management, review, acceptance, and reporting. Executors own substantial implementation, complex debugging, and long-running verification.

Its central principle is simple: an executor reporting that work is complete does not mean the work has been accepted.

Every substantial candidate must be checked against its scope, independently reviewed, and verified with fresh evidence before the controller can declare it complete.

## Why Project Lead

Complex projects become unreliable when one conversation is expected to analyze requirements, modify code, test the result, review its own changes, and approve the final release.

Common failure modes include:

- The controller becomes absorbed in implementation and loses project-level visibility.
- The same agent acts as both primary implementer and final reviewer.
- Multiple tasks duplicate work or modify the same module concurrently.
- Frontend, backend, database, and API dependencies are executed in the wrong order.
- Completion is reported without current build or test evidence.
- Task ownership and progress are lost after an interruption.
- Approval prompts remain hidden at the bottom of an executor conversation while the sidebar still shows the task as running.
- Polling loops and background waiting consume quota without producing decisions.

`project-lead` addresses these problems through explicit role boundaries, ownership-aware routing, independent review, and evidence-based acceptance.

## Core Capabilities

### Controller and executor separation

The controller may clarify intent, inspect repositories and tasks using read-only operations, maintain plans, improve executor briefs, coordinate tasks, organize reviews, evaluate evidence, and report results.

Executors own code implementation, multi-file changes, non-trivial debugging, architecture and database work, builds, tests, manual verification, and review repairs.

The controller does not become both the primary implementer and final reviewer of the same substantial change.

### Evidence-based executor briefs

Users do not need to provide complete engineering specifications. The controller first examines live repository, branch, worktree, and task state, then turns a brief request into an executor-ready specification containing:

- The desired user outcome and relevant context.
- Current-version requirements and explicitly deferred work.
- Scope, module ownership, worktree, branch, and base commit.
- Dependencies and safe parallelism.
- Acceptance criteria and required checks.
- Security boundaries and forbidden actions.
- Completion-report requirements and stop conditions.

Engineering details are derived from evidence rather than guesses.

### Ownership-aware routing

Before creating work, the controller inventories active and relevant completed tasks. Compatible tasks are reused for the same module, checkout, repair cycle, or unfinished work. A silent or abnormal task does not justify a second owner for overlapping scope: ownership must be ended and its worktree state recorded before a handoff. Independent modules may proceed in parallel, while shared files, migrations, and dependent contracts are serialized.

A lightweight control ledger keeps objectives, ownership, branches, dependencies, status, review decisions, and follow-up work traceable.

### Independent acceptance

Executor self-reports are not treated as acceptance. For every substantial candidate, the controller checks:

- The actual branch and worktree.
- Base and head commits.
- Changed files and scope.
- Working-tree cleanliness.
- Fresh build and test results.
- Unreported or unrelated changes.

The controller then invokes `requesting-code-review` with the exact requirements and commit range. Critical or Important findings return to the same executor for repair, and the changed diff is reviewed again.

Before reporting success, the controller invokes `verification-before-completion` and confirms that the evidence is fresh and relevant.

### Event-driven coordination

`project-lead` coordinates work through task events and current cursors. It does not create timers, heartbeat jobs, recurring automation, or periodic polling loops. If an active task produces no substantive progress for 30 minutes, the controller may take one fresh read-only snapshot and, only when the state remains unclear, ask the same task once through `gpt-5.6-luna` for status. The fallback cannot edit, review, accept, restart, or duplicate work, and it rearms only after real progress.

This reduces unnecessary quota usage while preserving bounded status recovery. It is not background monitoring: if the controller terminates, it cannot wake itself, and the next controller turn must reconcile saved task handles.

### Human approval relay

When an executor needs a command approval, confirmation, or other user input, `project-lead` treats it as an immediate `blocked_on_user` state instead of an ordinary running task. The controller names the affected task, explains the exact action and its effect or risk, and tells the user to open that task and act at the bottom of the conversation. It does not wait for the 30-minute fallback or approve on the user's behalf.

Repeated notices are deduplicated within a controller session. An unresolved request is surfaced again when a later controller session resumes, and the blocker is cleared only after the executor reports that approval was received or produces substantive progress beyond it.

Some system approval cards expose their exact command or confirmation only at the bottom of the executor conversation. If the controller can see `waitingOnApproval` but cannot see that card, it says so plainly, does not guess from the surrounding task plan, and does not message the frozen executor for clarification. It tells the user to expand the original card, which remains the source of truth.

## Workflow

```text
Product request
      ↓
Inspect repository, branch, and active tasks
      ↓
Compile scope, dependencies, and acceptance criteria
      ↓
Route work by module ownership
      ↓
Executor implements and provides evidence
      ↓
Controller validates the candidate
      ↓
Independent code review
      ↓
Repair and re-review when required
      ↓
Final verification and acceptance
      ↓
Result report and release recommendation
```

## When to Use

Use `project-lead` for:

- Full-stack projects spanning frontend, backend, and database work.
- Products containing multiple applications, services, or repositories.
- Long-running projects coordinated through several Codex tasks.
- Work requiring formal review and release gates.
- Projects that must recover cleanly after interrupted conversations.

Do not use it for:

- Small, isolated code changes.
- Tasks that do not require delegation or independent review.
- Simple questions or code explanations.

## Installation

Install globally for Codex with the Skills CLI:

```bash
npx skills add yousef555khg-beep/project-lead@project-lead -g -a codex
```

Then explicitly activate it when starting a controller conversation:

```text
Use project-lead to govern this project.
```

## Companion Skills

`project-lead` expects these companion skills to be available:

- `requesting-code-review` for structured review briefs and review gates.
- `verification-before-completion` for evidence-based completion claims.

## Evidence and Community

- [Sanitized real-world use cases](docs/USE-CASES.md) describe how the skill has governed two private multi-module products without publishing private source code.
- [Behavior validation](docs/VALIDATION.md) records repeatable pressure scenarios for duplicate dispatch, controller authority, independent review, and the 30-minute status fallback.
- [Changelog](CHANGELOG.md) tracks public releases.
- [Contributing guide](CONTRIBUTING.md) explains how to report problems and propose rule changes.

## Model Defaults

For tasks first created under `project-lead`, Terra is the default execution model and Sol is the default control and review model. A user-specified model choice always takes precedence.

## Design Goal

`project-lead` is not intended to create more tasks for their own sake. Its purpose is to make every task traceable: each task should have a clear objective, owner, scope, evidence, review decision, and stop condition.

Success is not measured by how much activity was generated. It is measured by whether the project produced an independently reviewed result that can be safely accepted.

## License

[MIT](LICENSE)
