#!/usr/bin/env python3
"""What is free to take in openspec/ROADMAP.md, with step state taken from OpenSpec.

Usage: python3 openspec/roadmap-ready.py [--mechanical] [ROADMAP.md]   (default: ROADMAP.md next to this script)
Step — a «### <change>» heading followed by a «Depends:» line; «Depends:» lists change
names up to the first «.» before a space or the line end, «;» or « — »; a known change named
in parentheses counts too. «<step>@<repo>» is a step of another roadmap: <repo> is a folder
of ~/projects, «.claude» is ~/.claude; it is done when archived there, waits (section
«Waiting on another roadmap») while it is in that repo's roadmap or an active change, and is
a typo when the repo or the step is not found.
Done = archived (openspec/changes/archive/<date>-<change>), in progress = an active
change (`openspec list --json`) or a git branch named <step> (local or in origin,
`git for-each-ref`; no `gh` call; the variant branches <step>--* of a new screen do not count), free = neither, with every dependency done.
Three blockers: «Decide:» (a decision of the user), «Hands:» (only the owner can do it),
«Waits:» (an external event); a field set to «—» is absent. Mechanical = «Decide: —» and no
«Hands:» or «Waits:» with a value; a step without «Decide:» is not. --mechanical lists only
the free mechanical steps.
«unblocks N» counts the unfinished steps of this roadmap that depend on the step directly or
through a chain of «Depends:». The last section, «Blockers (most unblocking first):», has a
line per blocker of every step not archived and not in progress — decide (the «Decide:» value,
or «not stated» without the line), hands, waits (the «Waits:» value or an unfinished
«<step>@<repo>») — most unblocking first, then file order.
"""
import json, os, re, subprocess, sys

FIELD = re.compile(r"\b(Order|Read|Goal|Scope|Out|Done when|Decide|Decided|Hands|Waits):")


def tokens(text):
    return [t.strip("`") for t in re.split(r"[\s,]+", text) if t.strip("`") not in ("", "—", "-")]


def parse(text):
    """[{change, deps, aside, glued, mechanical, blocked, decide, hands, waits}] — headings that carry a «Depends:» line."""
    steps, head, step = [], None, None
    for line in text.splitlines():
        if line.startswith("#"):
            head = line[4:].split()[0].strip("`") if line.startswith("### ") and line[4:].split() else None
            step = None
        elif step and line.startswith("Decide:"):
            step["decide"] = line[len("Decide:"):].strip()
            step["mechanical"] = step["decide"][:1] in ("—", "-")
        elif step and line.startswith(("Hands:", "Waits:")):
            key, _, val = line.partition(":")
            step[key.lower()] = val.strip()
            step["blocked"] |= val.strip()[:1] not in ("", "—", "-")
        elif head and line.startswith("Depends:"):
            body = line[len("Depends:"):]
            inner = " ".join(re.findall(r"\(([^)]*)\)", body))
            outer = re.split(r"\.(?=\s|$)|[;(]| — ", re.sub(r"\([^)]*\)", "", body), maxsplit=1)[0]
            step = {"change": head, "deps": tokens(outer), "aside": tokens(inner),
                    "glued": bool(FIELD.search(line)), "mechanical": False, "blocked": False,
                    "decide": None, "hands": "", "waits": ""}
            steps.append(step)
            head = None
    return steps


def foreign_state(dep):
    """«<step>@<repo>» → "done" (archived there), "wait" (in its roadmap or an active change) or None (typo).
    <repo> is ~/projects/<repo> or, for «.claude», ~/.claude — read from files, no CLI (HOME from the environment)."""
    step, _, repo = dep.partition("@")
    home = os.path.expanduser("~")
    root = os.path.join(home, ".claude" if repo == ".claude" else os.path.join("projects", repo))
    if not step or not repo or "/" in step + repo or not os.path.isdir(os.path.join(root, "openspec")):
        return None
    changes = os.path.join(root, "openspec", "changes")
    arch = os.path.join(changes, "archive")
    if any(re.fullmatch(r"\d{4}-\d{2}-\d{2}-" + re.escape(step), d) for d in (os.listdir(arch) if os.path.isdir(arch) else [])):
        return "done"
    if step != "archive" and os.path.isdir(os.path.join(changes, step)):
        return "wait"
    roadmap = os.path.join(root, "openspec", "ROADMAP.md")
    if os.path.isfile(roadmap) and step in {t["change"] for t in parse(open(roadmap, encoding="utf-8").read())}:
        return "wait"
    return None


def report(steps, active, archived, mechanical=False):
    known = {s["change"] for s in steps} | active | archived
    for s in steps:  # a known change named in parentheses is a dependency too
        s["deps"] += [d for d in s["aside"] if d in known and d not in s["deps"]]
    todo = [s for s in steps if s["change"] not in archived]
    kids = {s["change"]: [t["change"] for t in todo if s["change"] in t["deps"]] for s in todo}

    def below(name, seen):  # every step that depends on `name`, directly or through a chain
        for k in kids[name]:
            if k not in seen:
                seen.add(k)
                below(k, seen)
        return seen
    opens = {name: len(below(name, set())) for name in kids}
    state = {d: foreign_state(d) for s in todo for d in s["deps"] if "@" in d}
    done = lambda d: state[d] == "done" if "@" in d else d in archived
    free = [s for s in todo if s["change"] not in active and all(done(d) for d in s["deps"])
            and (s["mechanical"] and not s["blocked"] or not mechanical)]
    title = "Free mechanical (Decide: —):" if mechanical else "Free:"
    blockers = []  # (steps it unblocks, step, kind rank, text); the sort is stable: file order
    for s in todo:
        if s["change"] in active:
            continue
        rows = []
        if s["decide"] is None or not s["decide"]:
            rows.append(("decide", "not stated"))
        elif not s["mechanical"]:
            rows.append(("decide", s["decide"]))
        if s["hands"][:1] not in ("", "—", "-"):
            rows.append(("hands", s["hands"]))
        if s["waits"][:1] not in ("", "—", "-"):
            rows.append(("waits", s["waits"]))
        rows += [("waits", d) for d in s["deps"] if state.get(d) == "wait"]
        blockers += [(opens[s["change"]], s["change"], kind, text) for kind, text in rows]
    blockers.sort(key=lambda b: -b[0])
    sections = [
        (title, [f"  {s['change']} ← {', '.join(s['deps']) or '—'}"
                       + (f"  · unblocks {opens[s['change']]}" if opens[s["change"]] else "") for s in free]),
        ("In progress (active change or branch):", [f"  {s['change']}" for s in todo if s["change"] in active]),
        ("Archived but still in the file (delete the block):", [f"  {s['change']}" for s in steps if s["change"] in archived]),
        ("Waiting on another roadmap:", [f"  {s['change']}: {d}" for s in todo for d in s["deps"] if state.get(d) == "wait"]),
        ("Neither a step nor a change (typo):", [f"  {s['change']}: {d}" for s in todo for d in s["deps"]
                                                if (state[d] is None if "@" in d else d not in known)]),
        ("«Depends:» glued to another field (split the line):", [f"  {s['change']}" for s in todo if s["glued"]]),
        ("Blockers (most unblocking first):", [f"  {name}" + (f"  · unblocks {n}" if n else "") + f"  · {kind}: {text}"
                                               for n, name, kind, text in blockers]),
    ]
    out = [] if free else ["No free mechanical steps." if mechanical else "No free steps."]
    for title, rows in sections:
        if rows:
            out += [title] + rows
    return "\n".join(out)


def openspec_state(cwd):
    info = json.loads(subprocess.run(["openspec", "list", "--json"], cwd=cwd, capture_output=True, text=True).stdout)
    active = {c["name"] for c in info.get("changes", [])}
    arch = os.path.join(info["root"]["path"], "openspec", "changes", "archive")
    archived = {re.sub(r"^\d{4}-\d{2}-\d{2}-", "", d) for d in (os.listdir(arch) if os.path.isdir(arch) else [])}
    return active, archived


def branch_steps(cwd, names):
    """Steps with a branch <step> in refs/heads or refs/remotes/origin; none outside git. The variant branches
    <step>--<letter> do not make a step "in progress": until a variant is chosen the step is an ordinary one."""
    r = subprocess.run(["git", "-C", cwd, "for-each-ref", "--format=%(refname:short)", "refs/heads", "refs/remotes/origin"],
                       capture_output=True, text=True)
    refs = {re.sub(r"^origin/", "", b) for b in r.stdout.split()} if r.returncode == 0 else set()
    return {n for n in names if n in refs}


if __name__ == "__main__":
    args = sys.argv[1:]
    mechanical = "--mechanical" in args
    args = [a for a in args if a != "--mechanical"]
    path = os.path.abspath(args[0] if args else os.path.join(os.path.dirname(os.path.abspath(__file__)), "ROADMAP.md"))
    steps = parse(open(path, encoding="utf-8").read())
    active, archived = openspec_state(os.path.dirname(path))
    active |= branch_steps(os.path.dirname(path), {s["change"] for s in steps})
    print(report(steps, active, archived, mechanical))
