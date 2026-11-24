-- Cambridge Primary Mathematics Stage 4 (Atomic course, 0096 framework). Course key 14 = units stage14-unit01 … stage14-unit18.
insert into public.stage_units (stage, unit, title, free_sections) values
 (14, 'stage14-unit01', 'Numbers and the number system', array['1.1']),
 (14, 'stage14-unit02', 'Time and timetables', array['2.1']),
 (14, 'stage14-unit03', 'Addition and subtraction of whole numbers', array['3.1']),
 (14, 'stage14-unit04', 'Probability', array['4.1']),
 (14, 'stage14-unit05', 'Multiplication, multiples and factors', array['5.1']),
 (14, 'stage14-unit06', '2D shapes', array['6.1']),
 (14, 'stage14-unit07', 'Fractions', array['7.1']),
 (14, 'stage14-unit08', 'Angles', array['8.1']),
 (14, 'stage14-unit09', 'Comparing, rounding and dividing', array['9.1']),
 (14, 'stage14-unit10', 'Collecting and recording data', array['10.1']),
 (14, 'stage14-unit11', 'Fractions and percentages', array['11.1']),
 (14, 'stage14-unit12', 'Investigating 3D shapes and nets', array['12.1']),
 (14, 'stage14-unit13', 'Addition and subtraction', array['13.1']),
 (14, 'stage14-unit14', 'Area and perimeter', array['14.1']),
 (14, 'stage14-unit15', 'Special numbers', array['15.1']),
 (14, 'stage14-unit16', 'Data display and interpretation', array['16.1']),
 (14, 'stage14-unit17', 'Multiplication and division', array['17.1']),
 (14, 'stage14-unit18', 'Position, direction and movement', array['18.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get Mathematics Stage 4 too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 14, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
