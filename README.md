# Atomic Checkpoint – Science Stage 7

Self-study course for Cambridge Lower Secondary Science (Stage 7), sold to families in the UK and South-East Asia.

* **Website** – static HTML/JS in `web/` (no framework, no build step), hosted on **Vercel**.
* **Database, sign-in, marking** – **Supabase**: Postgres with row-level security (`supabase/migrations`) and two Edge Functions:
  `api` (Unit Test marking, marker queue, data export/delete) and `signup` (test-phase sign-up without email).
* **Answer keys never reach the browser and are never in git** (`.gitignore`): they live in `content/private/` on the author's machine
  and inside the deployed `api` function only.

```
web/                  the site: app.js (screens), core.js (learning rules), backend.js (demo | live), content/ (public, keys stripped)
shared/               marking + test rules used by the browser AND the server
supabase/migrations/  schema, RLS, grants, students & parental consent          supabase/functions/  Edge Functions
api/                  the same server handlers as plain Node modules (tests, and a Vercel option)
content/authoring/    Python sources of every question (test papers are in content/private/, not in git)
tests/                api.test.mjs, sql/, e2e.py, e2e_beta.py               tools/  build + dev scripts
```

## Two environments

| | **Test** (us and pilot families) | **Production** (paying clients) |
| --- | --- | --- |
| Git branch | `staging` | `main` |
| Website | Vercel *Preview* deployment of `staging` | Vercel *Production* deployment of `main` |
| Supabase project | `mrphe996's Project` – ref `condufamthngjudcdtgs` (Seoul) | `atomic-production` – ref `camrubtiydncxqyjmkja` (Singapore) |
| `ATOMIC_ENV` | `test` – orange “TEST environment” bar, data may be reset | `production` |
| Payments | `BILLING=off` (everything free) | `off` during the pilot → `paddle` at launch |
| Sign-up | `DIRECT_SIGNUP=on` (no email needed) | `on` until a mail sender is set up, then `off` |

Flow: work on `staging` → check the Test website → merge `staging` into `main` → Production updates.
Database changes: apply the new file in `supabase/migrations` to **Test first**, then Production.

### Vercel environment variables (public values only)

| Variable | Test (Preview, branch `staging`) | Production |
| --- | --- | --- |
| `ATOMIC_MODE` | `live` | `live` |
| `ATOMIC_ENV` | `test` | `production` |
| `SUPABASE_URL` | `https://condufamthngjudcdtgs.supabase.co` | `https://camrubtiydncxqyjmkja.supabase.co` |
| `SUPABASE_ANON_KEY` | test publishable key | production publishable key |
| `API_BASE` | `https://condufamthngjudcdtgs.supabase.co/functions/v1/api` | `https://camrubtiydncxqyjmkja.supabase.co/functions/v1/api` |
| `SIGNUP_URL` | `https://condufamthngjudcdtgs.supabase.co/functions/v1/signup` | `https://camrubtiydncxqyjmkja.supabase.co/functions/v1/signup` |
| `DIRECT_SIGNUP` / `BILLING` | `on` / `off` | `on` / `off` |

The Supabase service key is only used inside the Edge Functions, where Supabase provides it automatically.

## Run locally (demo mode – no accounts needed)

```
npm run dev          # http://localhost:8765 – accounts, marking and payments simulated in the browser
```

## Content and functions (author's machine – needs content/private/)

```
npm run build:content    # Python sources → web/content (public) + server/private (keys)
npm run build:edge       # supabase/functions/{_shared,api,signup}
supabase functions deploy api --no-verify-jwt --project-ref <ref>
supabase functions deploy signup --no-verify-jwt --project-ref <ref>
```
(Or `EDGE_LIB=https://cdn.jsdelivr.net/gh/mrphe996/atomic-checkpoint@<commit>/supabase/functions/_shared npm run build:edge`
and upload only `api/index.ts`, `api/units.js`, `api/data/*` – this is how the current functions were deployed, from commit `6cf5ba3`.)
After each deploy, `GET /functions/v1/api/health` returns the answer-key checksum and a self-marking check.

## Tests

```
npm run test:api     # server handlers (Node)          npm run test:edge   # the same tests on the Edge build
npm run test:sql     # schema + RLS on local Postgres  npm run test:e2e    # 61 browser checks (demo build)
```

## Before selling

1. Lawyer review of `#privacy`, `#terms`, `#cookies` (marked “Draft”).
2. Vercel Pro (Hobby is for non-commercial use only) and Supabase Pro (no pausing, daily backups).
3. Mail sender (e.g. Resend) + Supabase custom SMTP, then `DIRECT_SIGNUP=off`.
4. Paddle account and prices (below), then `BILLING=paddle`.
5. Make this GitHub repository **private** – it holds all course questions. (Edge deploys then use the Supabase CLI.)

## Prices (suggested, tax-inclusive; Paddle collects VAT/GST/SST)

| Market | Monthly | Yearly |
| --- | --- | --- |
| United Kingdom | £9.99 | £79 |
| Singapore | S$14.90 | S$119 |
| Malaysia | RM29 | RM229 |
| Thailand | ฿249 | ฿1,990 |
| Vietnam | ₫149,000 | ₫1,190,000 |
| Indonesia | Rp99,000 | Rp790,000 |
| Philippines | ₱299 | ₱2,390 |

## Rules worth knowing

* Unit Test: 30 marks, pass strictly above 70 %. Papers A/B alternate; review questions before a retake. Written answers are marked by staff.
* Ranking score = mean of first-pass % across passed units, fixed by a database trigger. Leaderboard shows only opted-in learners.
* Students may sign up themselves. Under their country's consent age (UK/SG 13, VN 16, MY/ID/PH 18, TH 20) the account stays
  *pending* until a parent approves it through a link; until then nothing is stored on the server.
