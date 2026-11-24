-- Cambridge Lower Secondary Mathematics Stage 7 (Atomic course, 0862 framework). Course key 17 = units stage17-unit01 … stage17-unit16.
insert into public.stage_units (stage, unit, title, free_sections) values
 (17, 'stage17-unit01', 'Integers', array['1.1']),
 (17, 'stage17-unit02', 'Expressions, formulae and equations', array['2.1']),
 (17, 'stage17-unit03', 'Place value and rounding', array['3.1']),
 (17, 'stage17-unit04', 'Decimals', array['4.1']),
 (17, 'stage17-unit05', 'Angles and constructions', array['5.1']),
 (17, 'stage17-unit06', 'Collecting data', array['6.1']),
 (17, 'stage17-unit07', 'Fractions', array['7.1']),
 (17, 'stage17-unit08', 'Shapes and symmetry', array['8.1']),
 (17, 'stage17-unit09', 'Sequences and functions', array['9.1']),
 (17, 'stage17-unit10', 'Percentages', array['10.1']),
 (17, 'stage17-unit11', 'Graphs', array['11.1']),
 (17, 'stage17-unit12', 'Ratio and proportion', array['12.1']),
 (17, 'stage17-unit13', 'Probability', array['13.1']),
 (17, 'stage17-unit14', 'Position and transformation', array['14.1']),
 (17, 'stage17-unit15', 'Shapes, area and volume', array['15.1']),
 (17, 'stage17-unit16', 'Interpreting and discussing results', array['16.1'])
on conflict (stage, unit) do update set title = excluded.title, free_sections = excluded.free_sections;

-- testers get Mathematics Stage 7 too
insert into public.enrolments (learner_id, stage, method, amount)
select t.learner_id, 17, 'test', 'tester' from public.testers t
on conflict (learner_id, stage) do nothing;
