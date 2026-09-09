# Model capacity fallback

Read this only after a Spark usage-limit, quota-exhausted, or capacity rejection.

- Treat the attempt as a terminal capacity failure, not `blocked_on_user`.
- If Spark still appears active, interrupt it and wait for terminal state.
- Reconcile partial work and the exact live worktree before handoff.
- Redispatch the same remaining objective once to Terra without asking.
- Select Terra effort from the remaining work; never inherit Spark effort or escalate merely because fallback occurred.
- Keep the fallback objective-local. Do not switch back to Spark during that objective.
- If Terra also hits model capacity, report `blocked_on_capacity`; never bounce between models.
