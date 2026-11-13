# ai-joke-03 entry: writes one fixed joke about AI coding agents to /output/entry.txt.
# Deterministic: the same bytes on every run, no network, standard library only.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to keep it simple. "
    "It added a framework, a config file, and a README "
    "explaining why simple was impossible."
)


def main() -> None:
    # The grader reads /output; MAKEFUN_OUTPUT_DIR stands in for it locally.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
