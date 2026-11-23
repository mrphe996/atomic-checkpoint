-- Stage 7 units (Atomic course structure, aligned to the Cambridge Lower Secondary Science 0893 framework)
insert into public.stage_units (stage, unit, title) values
 (7, 'stage7-unit01', 'Introducing science'), (7, 'stage7-unit02', 'Measurements'), (7, 'stage7-unit03', 'Cells'),
 (7, 'stage7-unit04', 'Classifying living things'), (7, 'stage7-unit05', 'Food chains and food webs'),
 (7, 'stage7-unit06', 'Materials and their structure'), (7, 'stage7-unit07', 'Properties of materials'),
 (7, 'stage7-unit08', 'Acids and alkalis'), (7, 'stage7-unit09', 'Chemical reactions'), (7, 'stage7-unit10', 'Forces'),
 (7, 'stage7-unit11', 'Energy'), (7, 'stage7-unit12', 'Electricity'), (7, 'stage7-unit13', 'Earth processes'),
 (7, 'stage7-unit14', 'Earth and beyond')
on conflict do nothing;
