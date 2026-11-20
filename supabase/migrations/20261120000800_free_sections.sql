-- Each unit's free taster is its own first section (N.1), not 3.1.
update stage_units set free_sections = array[(substring(unit from 'unit(\d+)')::int)::text || '.1'] where stage = 7;
