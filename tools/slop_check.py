"""Anti-AI slop check for LinkedIn drafts (rules: database/writing/anti-ai.md).
Usage: python slop_check.py draft.txt   (or pipe text in: python slop_check.py < draft.txt)
Prints every hit with its line number. No hits = passes the automatic part of the gate.
It can't judge rhythm or specificity; the coach still reads it.
"""
import re, sys

PATTERNS = [
    (r"—", "em dash (use a full stop, comma or colon)"),
    (r"\bnot just\b", "'not just X' shape"),
    (r"\bnot only\b", "'not only X but Y' shape"),
    (r"\bit'?s not (about )?\w[^.]{0,60}[,.]\s*it'?s\b", "'It's not X, it's Y' shape"),
    (r"\b(isn'?t|aren'?t|wasn'?t)\b[^.]{0,60}\.\s*(it'?s|they'?re|it was)\b", "'It isn't X. It's Y.' shape"),
    (r"\bmost (people|teams|coaches|businesses) think\b[^.]*\.\s*the reality\b", "'Most think X. The reality is Y.'"),
    (r"\beveryone does\b[^.]*\.\s*nobody\b", "'Everyone does X. Nobody does Y.'"),
    (r"\bhere'?s the (thing|deal)\b", "banned phrase"),
    (r"\b(at the end of the day|the bottom line is|when it comes to|at its core|in today's|let's dive|dive in|without further ado|in a nutshell|buckle up|move the needle|bridge the gap|take it to the next level|in the realm of|it'?s worth noting|it'?s important to note|moving forward|circle back|touch base)\b", "banned phrase"),
    (r"\b(unlock|elevate|streamline|supercharge|empower)(s|ed|ing)?\b", "banned verb"),
    (r"\b(delve|tapestry|testament|vibrant|pivotal|crucial|intricate|meticulous(ly)?|bolster(ed)?|garner(ed)?|underscore[sd]?|foster(ing)?|leverag(e|ed|ing)|utili[sz]e|facilitate|paramount|groundbreaking|cutting-edge|game[- ]chang(er|ing)|transformative|revolutioni[sz]e|seamless(ly)?|robust|unprecedented|synerg(y|ies)|pain points)\b", "banned word"),
    (r"(^|\n)\s*(moreover|furthermore|additionally|interestingly|notably|importantly|indeed|certainly|absolutely),", "banned opener"),
    (r",\s+[A-Z][a-z]", "comma then a capital letter: typo, or two sentences joined by a comma"),
]

def do_checks(text):
    """The Do's (M3 L4). Returns warnings; the manual ones are always printed as reminders."""
    warns = []
    words = re.findall(r"[A-Za-z']+", text)
    first = [w for w in words if w.lower() in ("i", "i'm", "i've", "i'd", "i'll", "my", "me", "mine")]
    hook = "\n".join([l for l in text.strip().splitlines() if l.strip()][:2])
    if not first:
        warns.append("DO first person: no I / my / me anywhere.")
    elif not re.search(r"\b(I|I'm|I've|I'd|my|me)\b", hook):
        warns.append("DO first person: not in the hook (first 2 lines). Fine if deliberate.")
    sents = [x for x in re.split(r"(?<=[.!?:])\s+|\n+", text) if x.strip()]
    lens = [len(x.split()) for x in sents]
    for i in range(len(lens) - 2):
        a, b, c = lens[i:i+3]
        if a > 3 and max(a, b, c) - min(a, b, c) <= 2:
            warns.append(f"DO vary sentence length: 3 in a row ~{a} words: '{sents[i][:40]}...'")
    for para in re.split(r"\n\s*\n", text):
        n = len(para.split())
        if n > 45:
            warns.append(f"DO break up long sections: a {n}-word block with no line break: '{para.strip()[:40]}...'")
    return warns

MANUAL_DOS = [
    "DO provide unique, personal value: could anyone else have posted this unchanged? (coach judges)",
    "DO read it out loud: does it sound like me talking? (I do this before posting)",
]

def check(text):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        for pat, why in PATTERNS:
            for m in re.finditer(pat, line, flags=0 if "A-Z" in pat else re.I):
                hits.append((i, m.group(0).strip(), why, line.strip()))
    return hits

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    # Workflow footer (added 2026-10-05): a line starting "[WORKFLOW" is not part of the post.
    lines = text.splitlines()
    wf = [l for l in lines if l.strip().startswith("[WORKFLOW")]
    text = "\n".join(l for l in lines if not l.strip().startswith("[WORKFLOW"))
    hits = check(text)
    if not hits:
        print("PASS: no automatic slop hits.")
    for i, hit, why, line in hits:
        print(f"line {i}: '{hit}'  ->  {why}\n    {line}")
    warns = do_checks(text)
    print("\nDO'S:" + (" automatic checks OK." if not warns else ""))
    for w in warns:
        print("  WARN " + w)
    for m in MANUAL_DOS:
        print("  MANUAL " + m)
    # Workflow gate: full = promise, hooks, variations, draft, checker, gate. quick = promise, draft, gate.
    if len(sys.argv) > 1 and "posts" in sys.argv[1].replace("\\", "/") and sys.argv[1].endswith(".txt"):
        if not wf:
            print("\nWORKFLOW: NOT READY - no [WORKFLOW] footer. Add: [WORKFLOW] promise [ ] hooks [ ] variations [ ] draft [ ] styles [ ] checker [ ] gate [ ]")
        else:
            todo = re.findall(r"(\w+) \[ \]", wf[0])
            if todo:
                print("\nWORKFLOW: NOT READY - unticked: " + ", ".join(todo))
            else:
                print("\nWORKFLOW: complete (" + ("quick post" if "quick" in wf[0].lower() else "full") + "). Strip the [WORKFLOW] line before posting.")
