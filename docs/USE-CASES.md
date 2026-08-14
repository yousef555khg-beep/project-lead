# Sanitized Real-World Use Cases

These case studies describe real controller usage on private products. They intentionally omit repository paths, source code, API contracts, credentials, customer data, internal metrics, and unreleased product details. They are maintenance evidence, not claims of public adoption.

## Yuji: coordinating an iPhone and Apple Watch product

**Context.** Yuji is a private fishing product with separate iPhone and Apple Watch work, shared release gates, and device-specific verification. A single completion message is not enough to establish that both applications are ready.

**How `project-lead` was used.**

- The controller separated phone, watch, document, and release-readiness work by ownership and dependency.
- Existing compatible tasks were reused instead of opening new tasks for every follow-up.
- Executor results were treated as candidates. Small isolated work used controller verification; cross-device, shared-contract, and release work retained independent review.
- Device checks, build results, distribution status, and production readiness were kept as separate evidence states.
- After an interruption, saved task handles and nonterminal ledger entries were reconciled before new work was routed.

**Observed value.** The workflow kept one module's green result from being presented as approval for the whole product, while avoiding a separate review task for every small repair. High-risk review findings and unresolved release gates remained visible until they had their own evidence.

## Shengxue Youpin: coordinating a mini program and merchant platform

**Context.** Shengxue Youpin is a private commerce product spanning a mini program, merchant administration, backend contracts, and content workflows. Work across these modules can look independent while still sharing data and authorization boundaries.

**How `project-lead` was used.**

- The controller routed work by module ownership and serialized changes that depended on shared contracts.
- Follow-up repairs stayed with the original compatible executor, preventing duplicate edits to the same module.
- Requirements were compiled from live repository evidence rather than guessed interface fields.
- Candidates were checked for scope and fresh verification. Bounded module work used one batched Terra review; authorization, shared-contract, deployment, and other elevated work retained Sol review.
- Authentication, storage, deployment, and external-service actions remained outside executor authority unless explicitly authorized.

**Observed value.** The workflow made dependencies and stop conditions explicit, reduced duplicate implementation, and kept an executor's self-report separate from final acceptance.

## 中文摘要

以上两个案例分别来自私有的渔迹 iPhone/Apple Watch 产品，以及盛学优品小程序与商家平台。公开内容只描述项目治理方法：按模块划分责任、复用兼容任务、保存任务句柄、区分候选结果与最终验收、按风险选择快速验收或独立审查，并对鉴权、部署和外部操作设置权限边界。本文不包含任何私有代码、接口、路径、账号、密钥、客户数据或未发布功能。
