#!/usr/bin/env python3
"""Build the MCCCD context pages from fetch_mcccd.py markdown.

WHAT: Reads source/*.md (output of co-professor
_SYSTEM/tools/fetch_mcccd.py) and writes one HTML page per course
outline plus one for the certificate program, all in this folder.

WHY: The markdown is faithful but flat. The HTML gives the textbook
build session and Mr. Vega a readable, accessible reference: facts in
a definition list, the outline nested with Roman, letter, and arabic
labels, and each competency's outline references visible. Official
MCCCD text is reproduced verbatim. index.html is hand-written and is
not touched here.

Usage (from this folder, after re-fetching when MCCCD revises a page):
  python3 build_mcccd_html.py
"""
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FETCHED = "2026-10-21"

PAGES = [
    ("mcccd-cis137-course-16459059.md", "cis137-course-outline.html", "course"),
    ("mcccd-cis144-course-16459032.md", "cis144-course-outline.html", "course"),
    ("mcccd-cis218-course-16459061.md", "cis218-course-outline.html", "course"),
    ("mcccd-5364n-program-16459028.md",
     "ccl-5364n-foundations-of-applied-ai.html", "program"),
]
NAV = [
    ("index.html", "Context pack"),
    ("cis137-course-outline.html", "CIS137"),
    ("cis144-course-outline.html", "CIS144"),
    ("cis218-course-outline.html", "CIS218"),
    ("ccl-5364n-foundations-of-applied-ai.html", "CCL 5364N"),
]
COURSE_PAGE = {"CIS137": "cis137-course-outline.html",
               "CIS144": "cis144-course-outline.html",
               "CIS218": "cis218-course-outline.html"}


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def field(md: str, label: str) -> str:
    """Value of a 'Label: **Value**' fact."""
    m = re.search(re.escape(label) + r":\s*\*\*(.+?)\*\*", md)
    return m.group(1).strip() if m else ""


def bold_para(md: str, label: str) -> str:
    """Text of a '**Label:** paragraph' line."""
    m = re.search(r"^\*\*" + re.escape(label) + r":\*\*\s*(.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def between(md: str, start: str, end: str) -> str:
    """Text after the first `start` marker and before the next `end`."""
    i = md.index(start) + len(start)
    j = md.index(end, i)
    return md[i:j]


def approval(md: str) -> str:
    m = re.search(r"Approval Date:\s*\**(.+?)\**\s*$", md, re.M)
    return m.group(1).strip() if m else ""


def body_of(md: str) -> tuple:
    url = re.search(r"^URL Source:\s*(\S+)", md, re.M).group(1)
    body = md.split("Markdown Content:", 1)[1].strip("\n")
    return url, body


def parse_outline(block: str) -> list:
    """Nested outline from indented lines: 0 Roman, 3 letter, 6 arabic."""
    label = re.compile(r"^(?:[IVX]+|[A-Z]|\d+)\.\s+")
    sections = []
    for raw in block.splitlines():
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip())
        item = {"title": label.sub("", raw.strip()), "children": []}
        if indent == 0:
            sections.append(item)
        elif indent == 3:
            sections[-1]["children"].append(item)
        else:
            sections[-1]["children"][-1]["children"].append(item)
    return sections


def parse_course(md: str) -> dict:
    url, body = body_of(md)
    first = body.splitlines()[0].strip().strip("*")
    m = re.search(r"Lecture \*\*([\d.]+)\*\* Credit\(s\) \*\*([\d.]+)\*\* "
                  r"Period\(s\) \*\*([\d.]+)\*\* Load", body)
    comps = []
    for line in between(body, "## MCCCD Official Course Competencies",
                        "_MCCCD Official").splitlines():
        hit = re.match(r"^\d+\.\s+(.*?)\s*\(([IVX,\s\-]+)\)\s*$", line)
        if hit:
            comps.append((hit.group(1), hit.group(2)))
        elif re.match(r"^\d+\.\s+", line):
            comps.append((re.sub(r"^\d+\.\s+", "", line).strip(), ""))
    note = re.search(r"^_(.+)_$", body, re.M)
    return {
        "url": url, "title": first,
        "code": field(body, "Course"),
        "first_term": field(body, "First Term"),
        "final_term": field(body, "Final Term"),
        "credits": m.group(1) if m else "",
        "periods": m.group(2) if m else "",
        "load": m.group(3) if m else "",
        "subject_type": field(body, "Subject Type"),
        "load_formula": field(body, "Load Formula"),
        "approval": approval(body),
        "description": bold_para(body, "Description"),
        "requisites": bold_para(body, "Requisites"),
        "notes": bold_para(body, "Course Notes"),
        "competencies": comps,
        "note": note.group(1) if note else "",
        "outline": parse_outline(between(
            body, "## MCCCD Official Course Outline",
            "MCCCD Governing Board Approval Date")),
        "disclaimer": body.strip().splitlines()[-1].strip(),
    }


def parse_program(md: str) -> dict:
    url, body = body_of(md)
    first = body.splitlines()[0].strip().strip("*")
    soc = re.search(r"SOC Code:\s*\*\*(.+?)\*\*", body, re.S)
    soc_lines = [l.strip() for l in soc.group(1).splitlines()] if soc else []
    codes = []
    for line in soc_lines[1:]:
        hit = re.match(r"(\d{2}-\d{4})\s+(.+)", line)
        if hit:
            codes.append((hit.group(1), hit.group(2).strip()))
    outcomes = []
    for line in between(body, "## Learning Outcomes",
                        "## Program Notes").splitlines():
        hit = re.match(r"^\d+\.\s+(.*?)\s*\(([A-Z0-9,\s]+)\)\s*$", line)
        if hit:
            outcomes.append((hit.group(1), hit.group(2)))
    notes_block = between(body, "## Program Notes",
                          "**Program Prerequisites").strip()
    hit = re.match(r"\*\*(.+?)\*\*\s*(.*)", notes_block, re.S)
    prog_notes = [hit.group(1).strip(), hit.group(2).strip()] if hit else [notes_block]
    prereq = re.search(r"\*\*Program Prerequisites:\s*(.+?)\*\*", body)
    courses = []
    for line in body.splitlines():
        hit = re.match(r"^>\s*(\+{1,2})?\s*([A-Z]{2,4}\d{3}[A-Z]{0,2})\s+(.+?)"
                       r"\s+(\d+)(?:\s+\*\*Credits:\s*(\d+)\*\*)?\s*$", line)
        if hit:
            courses.append({"flag": hit.group(1) or "", "code": hit.group(2),
                            "title": hit.group(3), "credits": hit.group(4)})
    legend = [l.strip() for l in body.splitlines()
              if re.match(r"^\s*\+{1,2} indicates", l)]
    return {
        "url": url, "title": first,
        "major": field(body, "Major"),
        "catalog_year": field(body, "Catalog Year"),
        "effective_term": field(body, "Effective Term"),
        "award": field(body, "Award"),
        "total_credits": field(body, "Total Credits"),
        "cip": field(body, "CIP Code"),
        "initiating": field(body, "Initiating College"),
        "availability": field(body, "Program Availability"),
        "field_of_interest": field(body, "Field of Interest"),
        "council": field(body, "Instructional Council"),
        "gpa": field(body, "GPA"),
        "approval": approval(body),
        "soc_intro": soc_lines[0] if soc_lines else "",
        "soc": codes,
        "description": bold_para(body, "Description"),
        "outcomes": outcomes,
        "program_notes": prog_notes,
        "prereq": prereq.group(1).strip() if prereq else "",
        "courses": courses,
        "legend": legend,
        "disclaimer": body.strip().splitlines()[-1].strip(),
    }


def render_outline(sections: list) -> str:
    def ol(items, kind):
        if not items:
            return ""
        nxt = {"I": "A", "A": "1"}.get(kind, "1")
        inner = "".join(
            f"<li>{esc(i['title'])}{ol(i['children'], nxt)}</li>" for i in items)
        cls = ' class="outline"' if kind == "I" else ""
        return f'<ol type="{kind}"{cls}>{inner}</ol>'
    return ol(sections, "I")


def facts(rows: list) -> str:
    cells = "".join(f"<dt>{esc(k)}</dt><dd>{v}</dd>" for k, v in rows if v)
    return f'<dl class="facts">{cells}</dl>'


def page(title: str, current: str, body: str, source_url: str) -> str:
    links = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == current else ""}>'
        f"{esc(label)}</a></li>" for href, label in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="stylesheet" href="mcccd.css">
</head>
<body>
<header class="site"><div class="wrap">
<span class="brand">MCCCD context pack for CIS137</span>
<nav aria-label="Context pack pages"><ul>{links}</ul></nav>
</div></header>
<main>
{body}
</main>
<footer>
<p>Source: <a href="{esc(source_url)}">{esc(source_url)}</a>, fetched {FETCHED}
through <code>co-professor/_SYSTEM/tools/fetch_mcccd.py</code>. Official MCCCD
text appears verbatim. Rebuild this page with <code>python3 build_mcccd_html.py</code>.</p>
</footer>
</body>
</html>
"""


def render_course(d: dict, out: str) -> str:
    comps = "".join(
        f"<li>{esc(t)}" + (f' <span class="ref">({esc(r)})</span>' if r else "")
        + "</li>" for t, r in d["competencies"])
    credit_line = (f"{esc(d['credits'])} lecture credit(s), {esc(d['periods'])} "
                   f"period(s), {esc(d['load'])} load")
    body = f"""<h1>{esc(d['code'])}: {esc(d['title'])}</h1>
<p class="kicker">MCCCD official course outline and competencies.</p>
{facts([
    ("Course", esc(d['code'])),
    ("Title", esc(d['title'])),
    ("Credits", credit_line),
    ("First term", esc(d['first_term'])),
    ("Final term", esc(d['final_term'])),
    ("Subject type", esc(d['subject_type'])),
    ("Load formula", esc(d['load_formula'])),
    ("Governing Board approval", esc(d['approval'])),
])}
<h2>Description</h2>
<p>{esc(d['description'])}</p>
<h2>Requisites</h2>
<p>{esc(d['requisites'])}</p>
<h2>Course notes</h2>
<p>{esc(d['notes'])}</p>
<h2>MCCCD Official Course Competencies</h2>
<p class="fine">The Roman numerals after each competency point to the outline sections that serve it.</p>
<ol class="competencies">{comps}</ol>
<p class="note">{esc(d['note'])}</p>
<h2>MCCCD Official Course Outline</h2>
{render_outline(d['outline'])}
<p class="fine">{esc(d['disclaimer'])}</p>"""
    return page(f"{d['code']} {d['title']}: MCCCD outline", out, body, d["url"])


def render_program(d: dict, out: str) -> str:
    outcomes = "".join(
        f'<li>{esc(t)} <span class="ref">({esc(r)})</span></li>'
        for t, r in d["outcomes"])
    rows = ""
    for c in d["courses"]:
        href = COURSE_PAGE.get(c["code"])
        code = f'<a href="{href}">{esc(c["code"])}</a>' if href else esc(c["code"])
        req = "Has prerequisites and/or corequisites" if c["flag"] == "+" else ""
        rows += (f"<tr><td>{code}</td><td>{esc(c['title'])}</td>"
                 f"<td>{esc(c['credits'])}</td><td>{req}</td></tr>")
    soc_rows = "".join(f"<tr><td>{esc(c)}</td><td>{esc(t)}</td></tr>"
                       for c, t in d["soc"])
    notes = "".join(f"<p>{esc(n)}</p>" for n in d["program_notes"] if n)
    legend = " ".join(esc(l) for l in d["legend"])
    body = f"""<h1>{esc(d['title'])}</h1>
<p class="kicker">MCCCD program description for the Certificate of Completion (CCL), major {esc(d['major'])}.</p>
{facts([
    ("Major", esc(d['major'])),
    ("Award", esc(d['award'])),
    ("Total credits", esc(d['total_credits'])),
    ("Catalog year", esc(d['catalog_year'])),
    ("Effective term", esc(d['effective_term'])),
    ("CIP code", esc(d['cip'])),
    ("Initiating college", esc(d['initiating'])),
    ("Program availability", esc(d['availability'])),
    ("Field of interest", esc(d['field_of_interest'])),
    ("Instructional council", esc(d['council'])),
    ("GPA", esc(d['gpa'])),
    ("Program prerequisites", esc(d['prereq'])),
    ("Governing Board approval", esc(d['approval'])),
])}
<h2>Description</h2>
<p>{esc(d['description'])}</p>
<h2>Learning Outcomes</h2>
<p class="fine">The course codes after each outcome name the courses that serve it.</p>
<ol class="outcomes">{outcomes}</ol>
<h2>Program Notes</h2>
<div class="note">{notes}</div>
<h2>Required Courses</h2>
<div class="table-wrap">
<table>
<caption>Required courses, {esc(d['total_credits'])} credits in total</caption>
<thead><tr><th scope="col">Course</th><th scope="col">Title</th><th scope="col">Credits</th><th scope="col">Requisites</th></tr></thead>
<tbody>{rows}</tbody>
</table>
</div>
<p class="fine">{legend}</p>
<h2>Career paths (SOC codes)</h2>
<p>{esc(d['soc_intro'])}</p>
<div class="table-wrap">
<table>
<caption>Standard Occupational Classification codes listed by MCCCD</caption>
<thead><tr><th scope="col">SOC code</th><th scope="col">Occupation</th></tr></thead>
<tbody>{soc_rows}</tbody>
</table>
</div>
<p class="fine">{esc(d['disclaimer'])}</p>"""
    return page(f"{d['title']} CCL {d['major']}: MCCCD program", out, body, d["url"])


def main() -> None:
    for src, out, kind in PAGES:
        md = (HERE / "source" / src).read_text(encoding="utf-8")
        data = parse_course(md) if kind == "course" else parse_program(md)
        render = render_course if kind == "course" else render_program
        (HERE / out).write_text(render(data, out), encoding="utf-8")
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
