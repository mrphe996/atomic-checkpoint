-- Cambridge Primary Mathematics Stage 6 (Atomic course, 0096 framework). Course key 16 = units stage16-unit01 … stage16-unit17.
insert into public.stage_units (stage, unit, title, free_sections) values
 (16, 'stage16-unit01', 'The number system', array['1.1']),
 (16, 'stage16-unit02', 'Numbers and sequences', array['2.1']),
 (16, 'stage16-unit03', 'Averages', array['3.1']),
 (16, 'stage16-unit04', 'Addition and subtraction (1)', array['4.1']),
 (16, 'stage16-unit05', '2D shapes', array['5.1']),
 (16, 'stage16-unit06', 'Fractions and percentages', array['6.1']),
 (16, 'stage16-unit07', 'Exploring measures', array['7.1']),
 (16, 'stage16-unit08', 'Addition and subtraction (2)', array['8.1']),
 (16, 'stage16-unit09', 'Probability', array['9.1']),
 (16, 'stage16-unit10', 'Multiplication and division (1)', array['10.1']),
 (16, 'stage16-unit11', '3D shapes', array['11.1']),
 (16, 'stage16-unit12', 'Ratio and proportion', array['12.1']),
 (16, 'stage16-unit13', 'Angles', array['13.1']),
 (16, 'stage16-unit14', 'Multiplication and division (2)', array['14.1']),
 (16, 'stage16-unit15', 'Data', array['15.1']),
 (16, 'stage16-unit16', 'The laws of arithmetic', array['16.1']),
 (16, 'stage16-unit17', 'Transformations', array['17.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get Mathematics Stage 6 too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 16, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
