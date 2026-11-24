# Fortune in a Pot — entry program.
#
# Writes one original fortune for the houseplant on the windowsill to
# /output/entry.txt, where the house gate and judge read it. The fortune is a
# fixed, reviewed line: nothing is generated at run time, so the judged text
# is exactly the line below.
import os
import sys

FORTUNE = "On Thursday the sunbeam you saved all winter arrives — lean into it, and you will grow an inch taller by Friday."


def check_fortune(line):
    """Mirror the house gate: 1-120 chars, one line, not only whitespace."""
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"fortune is {len(line)} chars, gate wants 1-120")
    if not line.strip():
        raise SystemExit("fortune is only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("fortune must be a single line")


def main(argv):
    check_fortune(FORTUNE)
    out_dir = argv[1] if len(argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Read back and verify byte-for-byte what the judge will see.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    check_fortune(written)
    if written != FORTUNE:
        raise SystemExit("entry.txt does not match the reviewed fortune")
    print(f"wrote {path} ({len(FORTUNE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
