# Model capacity fallback

Read this only after any model's usage-limit, quota-exhausted, or capacity rejection. A model-specific failure does not prove another model has quota; a shared account limit is not bypassed by switching.

- Treat the attempt as a terminal capacity failure, not `blocked_on_user`.
- If the failed attempt still appears active, interrupt it and wait for terminal state. Unknown state never permits overlapping execution.
- Reconcile partial work and the exact live worktree before handoff.
- Select an alternate from current tool-supported, already authorized routes that can perform the remaining work. Apply the existing task-fit policy for GPT-6 Sol, GPT-6 Luna and GPT-6 Astra; do not hard-code a replacement model or violate an explicit fixed-model constraint. A read-only helper is not an implementation fallback.
- If no eligible alternate exists or a shared limit excludes all candidates, report `blocked_on_capacity` without another dispatch.
- Redispatch the same remaining objective once to the selected alternate without asking for already-held authority. Reuse the idle owner with explicit supported route fields where possible; a replacement must preserve the same live worktree and unique ownership.
- Select effort from the remaining work; never inherit the failed route's effort or escalate merely because fallback occurred. Preserve scope, review requirements and Standard/default speed; announce the corrected route before resuming.
- Keep the fallback objective-local and record its use in the existing objective ledger so follow-ups or context handoffs cannot reset it. Do not switch back to the failed route during that objective; do not replay completed or irreversible actions.
- If that one alternate also hits model capacity, report `blocked_on_capacity`; never bounce between models. A later recovery needs fresh capacity evidence or user direction, not another automatic dispatch loop.
