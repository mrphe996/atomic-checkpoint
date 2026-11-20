#!/bin/sh
# Run the schema + RLS tests against a throwaway database (needs a local Postgres 15+ on $PGHOST:$PGPORT).
set -e
DB=atomic_test_$$
createdb "$DB"
psql -q -v ON_ERROR_STOP=1 -d "$DB" -f "$(dirname "$0")/00_supabase_stub.sql"
for f in "$(dirname "$0")"/../../supabase/migrations/*.sql "$(dirname "$0")"/../../supabase/seed.sql; do psql -q -v ON_ERROR_STOP=1 -d "$DB" -f "$f"; done
psql -q -t -v ON_ERROR_STOP=1 -d "$DB" -f "$(dirname "$0")/99_tests.sql" | sed '/^\s*$/d'
dropdb "$DB"
