#!/bin/sh
# Rebuild a Maths stage after editing maths_notes_v4: notes (v3 + v4) → lesson documents → reading packs → index.
# Usage: tools/rebuild_maths_v4.sh 7 [units…]   (the originals must be in /tmp/content_before, see the progress doc)
set -e
cd "$(dirname "$0")/.."
ST=$1; shift
cp /tmp/content_before/stage1${ST}-unit*.json web/content/
python3 tools/apply_notes_v3.py "$ST" | tail -1
python3 tools/maths_video/apply.py "$ST"
UNITS=$(python3 -c "import json,glob,sys; print(' '.join(str(json.load(open(f))['unit']['n']) for f in sorted(glob.glob('web/content/stage1$ST-unit*.json')) if any(s.get('book') for s in json.load(open(f))['sections'])))")
[ -n "$UNITS" ] && python3 tools/build_books.py "$ST" $UNITS 2>&1 | grep "^c$ST" || true
python3 tools/build_read_packs.py "$ST" ${*:-$UNITS} 2>&1 | tail -1
python3 content/authoring/read_index.py > /dev/null
