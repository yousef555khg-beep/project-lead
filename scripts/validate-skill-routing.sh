#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

exec python3 "$script_dir/validate_skill_routing.py" "${1:-$script_dir/../skills/project-lead/SKILL.md}"
