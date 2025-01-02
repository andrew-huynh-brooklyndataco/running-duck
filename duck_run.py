import duckdb
import queries

input_race_distance = 'Marathon'    # choose '5k' '10k', 'Half Marathon', 'Marathon', 'Ultra Marathon'
input_training_level = 1                  # choose 1,2,3
input_race_date = '2025-07-26'            # Input your race date YYYY-MM-DD

set_var_query = f"""
    SET VARIABLE input_race_distance = '{input_race_distance}';
    SET VARIABLE input_training_level = {input_training_level};
    SET VARIABLE input_race_date = '{input_race_date}';
"""

duckdb.sql(set_var_query)

print(f"""
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
----- Your race plan for a level {input_training_level} {input_race_distance} on {input_race_date}
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
""")

duckdb.sql(queries.race_plan_query).show(max_rows=250)
#duckdb.sql(queries.data_validation).show(max_rows=250)

#write to csv
csv_file_name = (f"""level_{input_training_level}_plan_for_{input_race_distance}_on_{input_race_date}.csv"""
                 ).replace(" ", "_").replace("-", "_")
csv_write_string = (f"""COPY ({queries.race_plan_query_write_to_gcal}) TO {csv_file_name} (HEADER, DELIMITER ',')""")

duckdb.sql(csv_write_string)