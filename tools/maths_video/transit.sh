#!/bin/sh
# Lesson videos are not kept in git. To get them into the video storage, push them on a throw-away branch and let the
# Supabase function `mv-pull` copy them into the bucket `lesson-videos`; then delete the branch (sh transit.sh --done).
# Usage: sh tools/maths_video/transit.sh web/media/mv/s7/1-2.mp4 …   → prints the commit to pass to mv-pull
set -e
if [ "$1" = "--done" ]; then git push -q origin :refs/heads/mv-transit; exit; fi
export GIT_INDEX_FILE=$(mktemp -u)
git add -f "$@"
c=$(git commit-tree "$(git write-tree)" -m "Lesson videos in transit to the video storage")
rm -f "$GIT_INDEX_FILE"; unset GIT_INDEX_FILE
git push -q -f origin "$c:refs/heads/mv-transit"
echo "$c"
