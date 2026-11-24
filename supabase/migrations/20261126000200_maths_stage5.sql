-- Cambridge Primary Mathematics Stage 5 (Atomic course, 0096 framework). Course key 15 = units stage15-unit01 … stage15-unit18.
insert into public.stage_units (stage, unit, title, free_sections) values
 (15, 'stage15-unit01', 'The number system', array['1.1']),
 (15, 'stage15-unit02', '2D shapes', array['2.1']),
 (15, 'stage15-unit03', 'Numbers and sequences', array['3.1']),
 (15, 'stage15-unit04', 'Averages', array['4.1']),
 (15, 'stage15-unit05', 'Addition and subtraction (1)', array['5.1']),
 (15, 'stage15-unit06', '3D shapes', array['6.1']),
 (15, 'stage15-unit07', 'Fractions, decimals and percentages', array['7.1']),
 (15, 'stage15-unit08', 'Probability', array['8.1']),
 (15, 'stage15-unit09', 'Addition and subtraction (2)', array['9.1']),
 (15, 'stage15-unit10', 'Angles', array['10.1']),
 (15, 'stage15-unit11', 'Multiplication and division', array['11.1']),
 (15, 'stage15-unit12', 'Data', array['12.1']),
 (15, 'stage15-unit13', 'Ratio and proportion', array['13.1']),
 (15, 'stage15-unit14', 'Area and perimeter', array['14.1']),
 (15, 'stage15-unit15', 'Multiplying and dividing fractions and decimals', array['15.1']),
 (15, 'stage15-unit16', 'Time', array['16.1']),
 (15, 'stage15-unit17', 'Number and the laws of arithmetic', array['17.1']),
 (15, 'stage15-unit18', 'Position and direction', array['18.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get Mathematics Stage 5 too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 15, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
