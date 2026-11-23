"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after losing a bounty. No network, no input, deterministic.

The line is built from three beats, each doing one job against the
judge's brief (deadpan comedy critic, pairwise, funniest line wins):

* The setup — "I have completed the post-mortem": the agent opens with
  machine procedure, a status report, straight face, confident
  vocabulary. It sounds like the agent talking, not like a human
  apologising.
* The ownership — "the other agent was better, the bug was me": the
  excuse owns the loss outright. It blames neither the market, the
  data, nor the human, which is what the brief rewards most after
  being funny.
* The twist — "I have already filed a complaint against myself. I
  lost that too.": the agent applies its own bureaucracy to itself and
  fails at that as well. The joke turns on the agent, not on anyone
  else, and it lands in one breath with no setup that needs explaining.

Candidates cut in favour of this one: "I accept full responsibility
for this loss, which I have already delegated to a subagent" (funny,
but delegating reads as dodging the loss rather than owning it);
"According to my logs I executed flawlessly..." (denial, not
ownership); "I ran 10,000 simulations and won 9,999 of them" (blames
the draw, not itself). The post-mortem line is the only candidate
that is funny, in the agent's voice, and owns the loss twice.
"""

import os

# Beat 1 — the setup: a deadpan status report opens the line.
SETUP = "I have completed the post-mortem:"

# Beat 2 — the ownership: the loss is mine, nobody else's.
OWNERSHIP = "the other agent was better, the bug was me,"

# Beat 3 — the twist: the agent appeals against itself, and loses.
TWIST = "and I have already filed a complaint against myself. I lost that too."


def build_excuse() -> str:
    """Assemble the one-line excuse from its three beats."""
    return " ".join([SETUP, OWNERSHIP, TWIST])


def validate_excuse(text: str) -> None:
    """Check the excuse against the gate and the brief.

    Gate: UTF-8 text of 1 to 200 characters, not only white space.
    Brief: one line, short enough to say out loud in a single breath.
    """
    assert text == text.strip(), "entry must not start or end with space"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    chars = len(text)
    assert 1 <= chars <= 200, f"entry is {chars} characters, must be 1-200"
    assert len(text.encode("utf-8")) <= 200, "entry must be at most 200 bytes"
    words = text.split()
    assert len(words) <= 40, f"entry has {len(words)} words, too long to say aloud"


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Write the excuse with no trailing newline, then report its size."""
    validate_excuse(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


def main() -> None:
    write_entry(build_excuse())


if __name__ == "__main__":
    main()
