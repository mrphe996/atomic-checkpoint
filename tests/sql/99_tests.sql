\set ON_ERROR_STOP 1
-- two families + a marker
insert into auth.users (id, email, raw_user_meta_data) values
 ('00000000-0000-0000-0000-00000000000a', 'a@test', '{"display_name":"Parent A","country":"SG"}'),
 ('00000000-0000-0000-0000-00000000000b', 'b@test', '{"display_name":"Parent B","country":"GB"}'),
 ('00000000-0000-0000-0000-00000000000c', 'm@test', '{"display_name":"Marker"}');
update public.profiles set role = 'marker' where id = '00000000-0000-0000-0000-00000000000c';
select 'profiles created: ' || count(*) from public.profiles;

-- as parent A
set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
insert into public.learners (id, parent_id, nickname) values ('10000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-00000000000a', 'Neutron');
insert into public.progress (learner_id, unit, state) values ('10000000-0000-0000-0000-000000000001', 'stage7-unit03', '{"x":1}');
do $$ begin
  begin update public.profiles set role = 'admin' where id = auth.uid(); raise exception 'FAIL: role escalation allowed';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
  begin insert into public.attempts (learner_id, unit, n, form, client_key, answers, per, auto, status) values ('10000000-0000-0000-0000-000000000001','stage7-unit03',1,'A','k','{}','{}',30,'final'); raise exception 'FAIL: client wrote an attempt';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
select 'PASS A sees own learner: ' || (select count(*) = 1 from public.learners);
select 'PASS default leaderboard opt-in is off: ' || (select not leaderboard_opt_in from public.learners);

-- as parent B: cannot see A's family
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false)) _x;
select 'PASS B sees no learners of A: ' || (select count(*) = 0 from public.learners);
select 'PASS B sees no progress of A: ' || (select count(*) = 0 from public.progress);
do $$ begin
  begin insert into public.learners (parent_id, nickname) values ('00000000-0000-0000-0000-00000000000a', 'Spy'); raise exception 'FAIL: B created a learner for A';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
  begin insert into public.progress (learner_id, unit) values ('10000000-0000-0000-0000-000000000001', 'stage7-unit03b'); raise exception 'FAIL: B wrote A progress';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;

-- server (service role) writes attempts: fail then pass → first pass recorded once
reset role; set role service_role;
insert into public.attempts (id, learner_id, unit, n, form, client_key, answers, per, auto, score, pct, status, passed)
values ('20000000-0000-0000-0000-000000000001','10000000-0000-0000-0000-000000000001','stage7-unit03',1,'A','k1','{}','{}',15,15,50,'final',false),
       ('20000000-0000-0000-0000-000000000002','10000000-0000-0000-0000-000000000001','stage7-unit03',2,'B','k2','{}','{}',24,24,80,'final',true),
       ('20000000-0000-0000-0000-000000000003','10000000-0000-0000-0000-000000000001','stage7-unit03',3,'A','k3','{}','{}',30,30,100,'final',true);
do $$ begin
  begin insert into public.attempts (learner_id, unit, n, form, client_key, answers, per, auto, status) values ('10000000-0000-0000-0000-000000000001','stage7-unit03',4,'A','k1','{}','{}',0,'pending'); raise exception 'FAIL: duplicate client key accepted';
  exception when unique_violation then null; end;
end $$;
select 'PASS first-pass % fixed at 80 (not 100): ' || (select first_pass_pct = 80 from public.unit_results);
select 'PASS notifications created: ' || (select count(*) >= 2 from public.notifications);

-- leaderboard and certificate as parent A
reset role; set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
select 'PASS own child visible to own parent on board: ' || (select count(*) = 1 from public.leaderboard(7));
do $$ begin
  begin perform public.issue_certificate('10000000-0000-0000-0000-000000000001'); raise exception 'FAIL: certificate issued with 1 of 14 units';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false)) _x;
select 'PASS B does not see A child on board (not opted in): ' || (select count(*) = 0 from public.leaderboard(7));
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
update public.learners set leaderboard_opt_in = true;
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false)) _x;
select 'PASS after opt-in B sees A child: ' || (select count(*) = 1 from public.leaderboard(7));
-- complete the stage (service role) then certificate is idempotent
reset role; set role service_role;
insert into public.unit_results (learner_id, unit, stage, first_pass_pct, attempt_id)
select '10000000-0000-0000-0000-000000000001', unit, 7, 80, '20000000-0000-0000-0000-000000000002' from public.stage_units where unit <> 'stage7-unit03';
reset role; set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
do $$ begin
  begin perform public.issue_certificate('10000000-0000-0000-0000-000000000001'); raise exception 'FAIL: certificate issued without an end-of-year exam';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
select 'PASS no certificate without the end-of-year exam';
reset role; set role service_role;
insert into public.attempts (learner_id, unit, n, form, client_key, answers, per, auto, score, pct, status, passed)
values ('10000000-0000-0000-0000-000000000001', 'stage7-final', 1, '01', 'fin1', '{}', '{}', 40, 40, 80, 'final', true);
select 'PASS final exam kept out of unit results: ' || (select count(*) = 0 from public.unit_results where unit = 'stage7-final');
reset role; set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
select 'PASS certificate code stable: ' || (select public.issue_certificate('10000000-0000-0000-0000-000000000001') = public.issue_certificate('10000000-0000-0000-0000-000000000001'));
select 'PASS one certificate row: ' || (select count(*) = 1 from public.certificates);
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false)) _x;
do $$ begin
  begin perform public.issue_certificate('10000000-0000-0000-0000-000000000001'); raise exception 'FAIL: B issued A certificate';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
reset role; select code as cert_code from public.certificates \gset
set role anon;
select 'PASS public verification works: ' || (select count(*) = 1 from public.verify_certificate(:'cert_code'));
-- enrolment: simulated checkout only where mock_payments = on
set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
do $$ begin
  begin perform public.enrol_stage('10000000-0000-0000-0000-000000000001', 8); raise exception 'FAIL: enrolled while payments are closed';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
reset role; insert into private.app_secrets (name, value) values ('mock_payments', 'on') on conflict (name) do update set value = 'on';
set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
select 'PASS test checkout enrols: ' || (select public.enrol_stage('10000000-0000-0000-0000-000000000001', 8) = 'ok' and exists (select 1 from public.enrolments where stage = 8));
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false)) _x;
select 'PASS another parent cannot see the enrolment: ' || (select count(*) = 0 from public.enrolments);
do $$ begin
  begin perform public.enrol_stage('10000000-0000-0000-0000-000000000001', 9); raise exception 'FAIL: B enrolled A child';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
reset role;
-- events: optional analytics refused while opt-out
reset role; set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000a', false)) _x;
insert into public.events (learner_id, parent_id, name, props, essential) values ('10000000-0000-0000-0000-000000000001', auth.uid(), 'answer', '{"q":"s31r1","ok":true,"try":1,"unit":"stage7-unit03"}', true);
do $$ begin
  begin insert into public.events (parent_id, name, essential) values (auth.uid(), 'page_view', false); raise exception 'FAIL: optional analytics stored without consent';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
select 'PASS parent cannot read events table: ' || (select count(*) = 0 from public.events);
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000c', false)) _x;
select 'PASS marker sees item stats: ' || (select count(*) = 1 from public.item_stats('stage7-unit03'));
select 'PASS marker can read attempts: ' || (select count(*) = 3 from public.attempts);
-- account deletion cascades
reset role;
delete from auth.users where id = '00000000-0000-0000-0000-00000000000a';
select 'PASS deleting the account removes the family data: ' || ((select count(*) = 0 from public.learners where parent_id = '00000000-0000-0000-0000-00000000000a') and (select count(*) = 0 from public.attempts) and (select count(*) = 0 from public.certificates));

-- ---------- students who sign up themselves ----------
reset role;
insert into auth.users (id, email, raw_user_meta_data) values
 ('00000000-0000-0000-0000-0000000000d1', 's@test', '{"display_name":"Kid","role":"student","country":"VN"}'),
 ('00000000-0000-0000-0000-0000000000e1', 'hack@test', '{"role":"admin"}');
select 'PASS student role from sign-up: ' || (select role = 'student' from public.profiles where id = '00000000-0000-0000-0000-0000000000d1');
select 'PASS sign-up metadata cannot create staff: ' || (select role = 'parent' from public.profiles where id = '00000000-0000-0000-0000-0000000000e1');
-- the sign-up function (service role) creates the pending learner
set role service_role;
insert into public.learners (id, user_id, nickname, birth_year, country, consent_status, invite_code)
values ('10000000-0000-0000-0000-0000000000d1', '00000000-0000-0000-0000-0000000000d1', 'Kiddo', 2014, 'VN', 'pending', 'ABCD1234');
reset role; set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-0000000000d1', false)) _x;
select 'PASS pending student sees own learner row: ' || (select count(*) = 1 from public.learners);
do $$ begin
  begin insert into public.progress (learner_id, unit, state) values ('10000000-0000-0000-0000-0000000000d1', 'stage7-unit03', '{}'); raise exception 'FAIL: pending student stored progress before parental consent';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
  begin update public.learners set consent_status = 'approved' where id = '10000000-0000-0000-0000-0000000000d1';
    if found then raise exception 'FAIL: student approved themselves'; end if;
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
  begin perform public.approve_learner('ABCD1234'); raise exception 'FAIL: a student approved an invite';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
select 'PASS still pending: ' || (select consent_status = 'pending' from public.learners);
-- parent B opens the link and approves
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-00000000000b', false)) _x;
select 'PASS parent sees invite details: ' || (select nickname = 'Kiddo' from public.learner_invite('abcd1234'));
select 'PASS approve links the student: ' || (select public.approve_learner('abcd1234') = '10000000-0000-0000-0000-0000000000d1');
select 'PASS invite cannot be reused: ' || (select count(*) = 0 from public.learner_invite('ABCD1234'));
select 'PASS parent now sees the student: ' || (select count(*) = 1 from public.learners where id = '10000000-0000-0000-0000-0000000000d1' and parent_id = auth.uid());
select 'PASS consent recorded: ' || (select count(*) = 1 from public.consents where learner_id = '10000000-0000-0000-0000-0000000000d1' and kind = 'parental_consent');
select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-0000000000d1', false)) _x;
insert into public.progress (learner_id, unit, state) values ('10000000-0000-0000-0000-0000000000d1', 'stage7-unit03', '{"ok":1}');
select 'PASS approved student saves progress: ' || (select count(*) = 1 from public.progress);
-- (students may switch their own leaderboard setting since migration 0006)
select 'PASS student cannot see other learners: ' || (select count(*) = 1 from public.learners);

-- ---------- student-only model: school, parent email, email on unit completion ----------
reset role;
insert into auth.users (id, email, raw_user_meta_data) values ('00000000-0000-0000-0000-0000000000f1', 'solo@test', '{"display_name":"Solo Kid","role":"student","country":"SG"}');
set role service_role;
insert into public.learners (id, user_id, nickname, birth_year, country, consent_status, school_id, grade)
values ('10000000-0000-0000-0000-0000000000f1', '00000000-0000-0000-0000-0000000000f1', 'Solo', 2014, 'SG', 'not_required', (select id from public.schools where name = 'Tanglin Trust School'), 'Year 7');
reset role; set role anon;
select 'PASS anyone can list schools: ' || (select count(*) > 40 from public.schools);
reset role; set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-0000000000f1', false)) _x;
update public.learners set parent_email = 'mum@family.test', leaderboard_opt_in = true where id = '10000000-0000-0000-0000-0000000000f1';
select 'PASS student sets parent email and leaderboard: ' || (select parent_email = 'mum@family.test' and leaderboard_opt_in from public.learners where id = '10000000-0000-0000-0000-0000000000f1');
do $$ begin
  begin update public.learners set consent_status = 'approved' where id = '10000000-0000-0000-0000-0000000000f1'; raise exception 'FAIL: student changed a protected column';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
  begin update public.learners set user_id = null where id = '10000000-0000-0000-0000-0000000000f1'; raise exception 'FAIL: student changed owner';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
insert into public.progress (learner_id, unit, state) values ('10000000-0000-0000-0000-0000000000f1', 'stage7-unit03', '{}');
select 'PASS student without parent saves progress: ' || (select count(*) = 1 from public.progress where learner_id = '10000000-0000-0000-0000-0000000000f1');
reset role; set role service_role;
insert into public.attempts (learner_id, unit, n, form, client_key, answers, per, auto, score, pct, status, passed)
values ('10000000-0000-0000-0000-0000000000f1','stage7-unit03',1,'A','solo1','{}','{}',25,25,83.33,'final',true);
reset role;
select 'PASS parent email queued once on unit pass: ' || (select count(*) = 1 from public.email_outbox where to_email = 'mum@family.test' and subject like 'Solo has finished Unit 3: Cells%');
select 'PASS student notified: ' || (select count(*) = 1 from public.notifications where parent_id = '00000000-0000-0000-0000-0000000000f1');
set role authenticated; select 1 from (select set_config('request.jwt.claim.sub', '00000000-0000-0000-0000-0000000000f1', false)) _x;
do $$ begin
  begin perform 1 from public.email_outbox; raise exception 'FAIL: client read the email outbox';
  exception when others then if sqlerrm like 'FAIL%' then raise; end if; end;
end $$;
select 'PASS student sees own result: ' || (select count(*) = 1 from public.unit_results);
