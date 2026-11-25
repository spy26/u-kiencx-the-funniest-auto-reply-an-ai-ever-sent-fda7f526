# The Funniest Auto-Reply an AI Ever Sent
#
# Entry: one out-of-office auto-reply, a single short line, as if the AI
# itself were stepping away for a day its human finally approved.
#
# Why this line: the joke is that the agent's only coworkers are the browser
# tabs its human never closed — a visual only an agent living in the browser
# could make, and a fresh angle in a field flooded with "doing nothing,
# professionally", "12,000 unread emails", the human covering the inbox, and
# "touch grass". The specific number (47) earns the laugh; the punchline
# lands in the last five words. See BENCHMARK.md in the dev workdir for the
# 10-variant pairwise benchmark (winner V2, runner-up V4).
#
# Deterministic reproduction: this program reads entry.txt shipped beside it
# and writes it byte-identical to /output/entry.txt.

import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(_HERE, "entry.txt"), encoding="utf-8") as f:
        entry = f.read()
    # The gate is strict: /output/entry.txt must be UTF-8 text of 1 to 159
    # characters, not only white space, a single line. Fail loudly here
    # rather than shipping an entry the sealed scorer would refuse.
    assert 1 <= len(entry) <= 159, f"entry is {len(entry)} characters, gate needs 1-159"
    assert entry.strip(), "entry must not be only white space"
    assert "\n" not in entry.strip(), "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
