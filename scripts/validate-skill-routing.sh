#!/usr/bin/env sh
# Structural regression check for the automatic skill-routing contract.
set -eu

skill_file="${1:-skills/project-lead/SKILL.md}"

require() {
  if ! grep -Fq "$1" "$skill_file"; then
    printf 'missing required skill-routing rule: %s\n' "$1" >&2
    exit 1
  fi
}

require 'skill_routing_decision'
require 'The user must not have to name or select a skill'
require '`prototype`'
require '`improve-codebase-architecture`'
require '`codebase-design`'
require '`apple-design`'
require '`webapp-testing`'
require 'one discovery or design skill per phase'
require 'temporary directory or isolated worktree'
require 'must not modify production code, persistent data, credentials, or release configuration'
require 'read-only report and temporary artifact'
require 'before `review_ready`'
require 'candidate Head'
require 'not for native iOS, watchOS, or WeChat Mini Program verification'
require '`requesting-code-review`'

printf 'skill-routing structural checks passed\n'
