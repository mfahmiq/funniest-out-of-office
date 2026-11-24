"""Write one funny AI out-of-office auto-reply to /output/entry.txt.

The line: an AI agent on vacation hands its inbox to a cron job that
judges subject lines. Stdlib only, no network, deterministic: the same
bytes on every run. The entry must be 1-160 characters.
"""

import os

LINE = (
    "I'm on vacation. Your email has been forwarded to my replacement: "
    "a cron job that runs every 15 minutes and judges your subject lines "
    "silently."
)

assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
# The line is 143 characters, inside the 160-character gate.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
