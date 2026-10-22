#!/bin/bash
# Build the student course data pack: every chapter packet under assets/code,
# without the authoring-only _generators folder or system files.
# Output: build/cis137-data-pack.zip (build/ is gitignored). Students extract
# it and work at the extracted cis137 root, so every chapter path reads
# assets/code/chapter-NN/<file>.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f build/cis137-data-pack.zip
mkdir -p build
STAGE="$(mktemp -d)/cis137"
mkdir -p "$STAGE/assets/code"
for d in assets/code/chapter-*; do cp -R "$d" "$STAGE/assets/code/"; done
find "$STAGE" -name ".DS_Store" -delete
( cd "$(dirname "$STAGE")" && zip -q -r -X "$OLDPWD/build/cis137-data-pack.zip" cis137 )
unzip -tq build/cis137-data-pack.zip
echo "files: $(unzip -Z1 build/cis137-data-pack.zip | grep -vc '/$')"
