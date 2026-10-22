# Data Pack Generators

Scripts in this folder rebuild every derived file in the course data
pack. Follow the pattern the existing textbooks use:

## Conventions

* **Seeded and reproducible.** Synthetic datasets use a fixed base seed
  (pick the course number) so reruns are byte-identical. Add asserts
  that verify the engineered properties each chapter depends on.
* **Document provenance.** Real datasets record their source, license,
  and retrieval date here and in the chapter folder's README.
* **One-time captures are not rebuilt.** Files captured from live APIs
  are committed as-is and documented, not regenerated.
* **Each chapter folder gets a README** describing every file, its
  schema, and which sections or labs load it.

## Rebuilding the student data pack zip

Run the build script from the repo root:

```bash
bash tools/build_data_pack.sh
```

It copies every `assets/code/chapter-*` packet into a staging folder
named `cis137`, the folder name the published chapters tell students
to work in. It leaves out this `_generators/` folder (authoring files
only) and deletes `.DS_Store` files. The archive lands at
`build/cis137-data-pack.zip` (`build/` is gitignored), and the script
tests it and prints its file count. Upload that zip to Canvas. Do not
zip `assets/code` by hand, because a hand zip ships `_generators/`.

## Generators in this folder

* `gen_deskside_tickets.py` (Chapter 11): writes
  `chapter-11/deskside-tickets.csv`, 80 synthetic Deskside tickets in 6
  columns, base seed 137, byte-identical on rerun. Its asserts lock the
  properties Chapter 11's Section 11.3 data question and Skills Lab 11A
  depend on. Run
  `python3 assets/code/_generators/gen_deskside_tickets.py` from the
  repo root.
