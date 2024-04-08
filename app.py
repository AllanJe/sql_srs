import contextlib
import io
import pandas as pd
import ast
import os
import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")
if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run(["python","init_db.py"])

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice"""
)

with st.sidebar:
    # available_themes_df = con_execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review ?",
        con.execute("SELECT DISTINCT theme FROM memory_state").df(), # available_themes_df["theme].unique()
        #("Cross Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme",
    )
    if theme:
        st.write(f"You selected : {theme}")
        select_exercise_query = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
    else:
        select_exercise_query = f"SELECT * FROM memory_state"

    exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )

    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()
# answer_str = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """
#
# solution_df = duckdb.query(answer_str).df()

st.header("enter your code:")
query = st.text_area(label="Here your SQL code")


if query:
    result = con.execute(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some columns are missing")
    n_lines_difference = result.shape[0] - solution_df.shape[0]

    if n_lines_difference != 0:
        st.write(
            f"Result has a {n_lines_difference} lines differences with the solution"
        )

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError:
        st.write("Some colmuns are missing")
# if query:
#    result = duckdb.query(query).df()
#    st.dataframe(result)
#


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    if theme:
        exercise_tables = exercise.loc[0, "tables"]
        for table in exercise_tables:
            st.write(f"table: {table}")
            df_table = con.execute(f"SELECT * FROM '{table}'").df()
            st.dataframe(df_table)

#    st.write("table: food_items")
#    st.dataframe(food_items)
#    st.write("expected :")
#    st.dataframe(solution_df)
#
with tab3:
    if theme:
        st.write(answer)
