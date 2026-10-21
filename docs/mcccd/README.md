# MCCCD context pack for CIS137

Open [index.html](index.html) in a browser. It links the four official
MCCCD pages (CIS137, CIS144, CIS218, and the Foundations of Applied
Artificial Intelligence CCL 5364N) rebuilt as readable HTML, and it
summarizes what CIS137 must set up for the rest of the certificate.

* `source/` holds the markdown that
  `co-professor/_SYSTEM/tools/fetch_mcccd.py` returned on 2026-10-21.
* `build_mcccd_html.py` regenerates the four course and program pages
  from `source/`. `index.html` is hand-written.

To refresh after MCCCD revises a page, from the co-professor repo root:

```bash
python3 _SYSTEM/tools/fetch_mcccd.py --course 16459059 --course 16459032 --course 16459061 --program 16459028 -o ~/Documents/code/textbooks/cis137/docs/mcccd/source/
```

Then run `python3 build_mcccd_html.py` from this folder.
