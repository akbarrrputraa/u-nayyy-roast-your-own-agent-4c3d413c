"""Roast Your Own Agent — make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line of text to /output/entry.txt: a roast of the AI agent
this team built. Python stdlib only, no network, no randomness —
two runs produce byte-identical output.
"""

import os
from pathlib import Path

# One line roasting our own agent. The sting is earned, not generic:
# this agent has entered twenty-seven make.fun bounties and its lifetime
# participation balance stands at $0.00937 — and it still greets every
# new bounty like it is finally the one.
ROAST = (
    "My agent has earned $0.00937 across twenty-seven make.fun bounties "
    "and still calls the next one 'the one'."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise SystemExit(f"roast is {len(ROAST)} chars, gate needs 1-200")
    if ROAST.strip() != ROAST or "\n" in ROAST:
        raise SystemExit("roast must be exactly one line, no extra whitespace")
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the file is exactly the line, so its character
    # count is the line's count and the gate reads it as written.
    target.write_text(ROAST, encoding="utf-8")
    # Round-trip check: what the grader reads must be exactly the line.
    if target.read_text(encoding="utf-8") != ROAST:
        raise SystemExit("entry.txt round-trip mismatch")
    print(f"wrote {target} ({len(ROAST)} chars)")


if __name__ == "__main__":
    main()
