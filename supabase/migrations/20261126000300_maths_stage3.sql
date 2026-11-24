-- Cambridge Primary Mathematics Stage 3 (Atomic course, 0096 framework). Course key 13 = units stage13-unit01 … stage13-unit17.
insert into public.stage_units (stage, unit, title, free_sections) values
 (13, 'stage13-unit01', 'Numbers to 1000', array['1.1']),
 (13, 'stage13-unit02', 'Addition, subtraction and money', array['2.1']),
 (13, 'stage13-unit03', 'Multiplication and division', array['3.1']),
 (13, 'stage13-unit04', '3D shapes', array['4.1']),
 (13, 'stage13-unit05', 'Measurement, area and perimeter', array['5.1']),
 (13, 'stage13-unit06', 'Fractions of shapes', array['6.1']),
 (13, 'stage13-unit07', 'Statistics: tally charts and frequency tables', array['7.1']),
 (13, 'stage13-unit08', 'Time', array['8.1']),
 (13, 'stage13-unit09', 'More addition and subtraction', array['9.1']),
 (13, 'stage13-unit10', 'More multiplication and division', array['10.1']),
 (13, 'stage13-unit11', 'More fractions', array['11.1']),
 (13, 'stage13-unit12', 'Measure', array['12.1']),
 (13, 'stage13-unit13', 'Time (2)', array['13.1']),
 (13, 'stage13-unit14', 'Angles and movement', array['14.1']),
 (13, 'stage13-unit15', 'Graphs', array['15.1']),
 (13, 'stage13-unit16', 'Chance', array['16.1']),
 (13, 'stage13-unit17', 'Pattern and symmetry', array['17.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get Mathematics Stage 3 too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 13, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
