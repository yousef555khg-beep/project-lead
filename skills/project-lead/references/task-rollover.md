# Task rollover

Read this only after a controller, executor, or reviewer reaches a hard context trigger.

Token thresholds refer to the current context input, not cumulative billed tokens across all turns. The size threshold refers to this task's history record. These are Project Lead's conservative handoff thresholds, not a model's official context limit. Astra's larger model window alone does not prove that client history and relay limits have changed.

- Transfer only the remaining objective, owner and writable scope, source-of-truth paths or IDs, accepted evidence, blockers, next check, active child task IDs, and route.
- Preserve the user-selected controller route, including Astra. Apply executor exclusions only to executor successors; a controller successor is still a controller. Keep existing child IDs and owners instead of restarting them.
- The successor verifies the live worktree and source of truth before mutation.
- Mark the old task retired and name its successor; never allow overlapping owners.
- Notify: `上下文换线：<old title> → <new title>｜剩余目标：<one line>｜模型/档位/速度：<route>`. This notice is informational, not an approval gate.
- If `create_thread` is unavailable, report `blocked_on_visibility`; do not reuse the overlong task or claim handoff.
