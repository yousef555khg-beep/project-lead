# Security Policy / 安全策略

## Supported versions / 支持版本

Security fixes are applied to the latest published release and the current `main` branch.

安全修复会应用到最新正式版本和当前 `main` 分支。

| Version | Supported |
| --- | --- |
| Latest release | Yes |
| `main` | Yes |
| Older releases | Best effort only |

## Report a vulnerability privately / 私密报告漏洞

Do **not** open a public issue for a suspected vulnerability.

请勿通过公开 Issue 报告疑似漏洞。

Use GitHub's private [Report a vulnerability](https://github.com/yousef555khg-beep/project-lead/security/advisories/new) form. Include:

- the affected version, commit, file, or workflow;
- a clear reproduction or abuse scenario;
- the possible impact and required permissions;
- the smallest safe proof, without real credentials or private project data; and
- any suggested mitigation, if available.

请使用 GitHub 的私密 [漏洞报告入口](https://github.com/yousef555khg-beep/project-lead/security/advisories/new)，并说明：受影响版本或文件、复现方式、可能影响、所需权限和建议修复。请勿提交真实凭据或私有项目数据。

Maintainers aim to acknowledge a complete report within seven days. Validation and disclosure timing depend on severity and reproducibility. Please allow time for a fix before public disclosure.

维护者会尽量在七天内确认完整报告。验证与披露时间取决于严重程度和可复现性；请在公开披露前为修复预留时间。

## Security scope / 安全范围

Useful reports include, but are not limited to:

- prompt-injection or untrusted-instruction paths that bypass Project Lead boundaries;
- unsafe skill discovery, approval binding, installation, rollback, or loader behavior;
- credential, private-data, or filesystem exposure;
- unauthorized network, command, deployment, or destructive actions;
- validation bypasses that falsely mark blocked work or unsafe candidates as complete; and
- supply-chain risks in scripts, references, releases, or dependencies.

有效报告包括但不限于：绕过 Project Lead 边界的提示注入、不安全的 Skill 搜索或安装、凭据或隐私泄露、未经授权的命令或网络操作、错误完成判定，以及脚本或发布供应链风险。

General feature requests, review-policy preferences, and non-security bugs belong in the normal issue templates.

一般功能建议、审查策略偏好和非安全 Bug 请使用普通 Issue 模板。
