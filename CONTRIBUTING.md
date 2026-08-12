# Contributing to Project Lead

Thank you for helping make project coordination safer and more verifiable.

## Before opening an issue

- Remove repository paths, source code, credentials, customer data, private prompts, and internal logs.
- Search existing issues for the same behavior.
- Distinguish what the controller observed from what an executor merely reported.
- For a rule failure, include the smallest pressure scenario that reproduces it.

## Reporting a behavior problem

Include:

1. The controller situation and active task state.
2. The instruction that created pressure or ambiguity.
3. The action the controller took.
4. The action you expected.
5. Whether any external, destructive, deployment, authentication, or secret-handling boundary was involved.

Do not attach private repositories or secrets. Replace project names and identifiers with neutral placeholders.

## Proposing a change

Rule changes should be small and evidence-driven:

1. Record a scenario that fails with the current skill.
2. Explain the safety or reliability impact.
3. Change the minimum necessary text in `skills/project-lead/SKILL.md`.
4. Rerun the original scenario and relevant entries in `docs/VALIDATION.md`.
5. Update `docs/VALIDATION.md`, `README.md`, `README.zh-CN.md`, and `CHANGELOG.md` when behavior or public guidance changes.

## Pull request checklist

- [ ] The change addresses one clear controller behavior.
- [ ] A pre-change failure or gap is documented.
- [ ] Post-change validation is recorded.
- [ ] No private code, paths, credentials, customer data, or internal logs are included.
- [ ] The controller/executor role firewall remains intact.
- [ ] Independent review and fresh verification remain mandatory.
- [ ] The change does not introduce background polling or duplicate task routing.
- [ ] Documentation and changelog entries are updated.

## 中文说明

提交 Issue 或 PR 前，请删除私有仓库路径、源码、账号、密钥、客户数据、内部日志和未公开提示词。规则修改必须先记录当前 Skill 的失败场景，再做最小改动并重新验证。任何贡献都不能削弱总控与执行者的职责隔离、独立审查、完成前验证、禁止重复派发及禁止后台轮询等边界。
