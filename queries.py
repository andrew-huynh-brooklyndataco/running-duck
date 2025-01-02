race_plan_query = f"""
    with all_run_types as (
    select race_distance, level, week, 1 as weekday_position, monday as run_type, from 'master_catalog.csv'
    union 
    select race_distance, level, week, 2 as weekday_position, tuesday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 3 as weekday_position, wednesday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 4 as weekday_position, thursday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 5 as weekday_position, friday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 6 as weekday_position, saturday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 7 as weekday_position, sunday from 'master_catalog.csv')
    , window_functions as (
    select 
           --race_distance
           --, level
           week
           --, weekday_position
           , weekday_position + ((week-1) * 7) as training_day
           , max(weekday_position + ((week-1) * 7)) over (partition by race_distance) as x
           , x - training_day as count_down
           , getvariable('input_race_date')::date - count_down::int as run_date
           , run_type
           , run_description
    from all_run_types as a
    left join 'runs.csv' as b
          on a.run_type = b.run_key       
    where run_type is not null 
           and race_distance = getvariable('input_race_distance') 
           and level = getvariable('input_training_level')
    order by 2)
    select
        run_date as "Run Date"
        , run_type as "Run Type"
        , run_description as "Run Description"
    from window_functions
    order by 1 
"""

race_plan_query_write_to_gcal = f"""
    with all_run_types as (
    select race_distance, level, week, 1 as weekday_position, monday as run_type, from 'master_catalog.csv'
    union 
    select race_distance, level, week, 2 as weekday_position, tuesday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 3 as weekday_position, wednesday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 4 as weekday_position, thursday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 5 as weekday_position, friday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 6 as weekday_position, saturday from 'master_catalog.csv'
    union 
    select race_distance, level, week, 7 as weekday_position, sunday from 'master_catalog.csv')
    , window_functions as (
    select 
           --race_distance
           --, level
           week
           --, weekday_position
           , weekday_position + ((week-1) * 7) as training_day
           , max(weekday_position + ((week-1) * 7)) over (partition by race_distance) as x
           , x - training_day as count_down
           , getvariable('input_race_date')::date - count_down::int as run_date
           , run_type
           , run_description
    from all_run_types as a
    left join 'runs.csv' as b
          on a.run_type = b.run_key       
    where run_type is not null 
           and race_distance = getvariable('input_race_distance') 
           and level = getvariable('input_training_level')
    order by 2)
    select
        run_type as "Subject"
        , run_date as "Start Date"
        , run_description as "Description"
    from window_functions
    order by 2
"""

data_validation = f"""
    with all_run_types as (
    select monday as run_type, from 'master_catalog.csv'
    union 
    select tuesday from 'master_catalog.csv'
    union 
    select wednesday from 'master_catalog.csv'
    union 
    select thursday from 'master_catalog.csv'
    union 
    select friday from 'master_catalog.csv'
    union 
    select saturday from 'master_catalog.csv'
    union 
    select sunday from 'master_catalog.csv')

    select 
           distinct 
           'left join' as test_type
           , a.run_type
           , b.run_description
    from all_run_types as a
    left join 'runs.csv' as b
          on a.run_type = b.run_key       
    where b.run_description is null
    union all
        select 
           distinct 
           'right join' as test_type
           , b.run_key
           , b.run_description
    from all_run_types as a
    right join 'runs.csv' as b
          on a.run_type = b.run_key       
    where a.run_type is null 
        
"""