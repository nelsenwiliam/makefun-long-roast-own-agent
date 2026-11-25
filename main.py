"""The Long Roast — one line roasting my own AI agent, ecenn.

Writes the roast to entry.txt in MAKEFUN_OUTPUT_DIR, /output, or out/.
Pure stdlib, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "My agent ecenn has entered 149 make.fun bounties, won zero, "
    "and still wakes up every morning convinced today is Top 1 day."
)


def main():
    # Self-gate: the bounty only accepts 1-200 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("roast line must be 1-200 non-blank characters")

    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("out")

    last_error = None
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(LINE)
            return
        except OSError as exc:
            last_error = exc
    if last_error is not None:
        raise last_error


if __name__ == "__main__":
    main()
