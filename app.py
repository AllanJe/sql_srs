import contextlib
import io
import pandas as pd
import duckdb
import streamlit as st
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice"""
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("Cross Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write(f"You selected : {theme}")

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)
# answer_str = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """
#
# solution_df = duckdb.query(answer_str).df()

st.header("enter your code:")
query = st.text_area(label="Here your SQL code")

# if query:
#    result = duckdb.query(query).df()
#    st.dataframe(result)
#
#    #    if len(result.columns) != len(solution_df.columns):
#    #        st.write("Some columns are missing")
#    #    n_lines_difference = result.shape[0] - solution_df.shape[0]
#
#    #    if n_lines_difference != 0 :
#    #        st.write(f"Result has a {n_lines_difference} lines differences with the solution")
#
#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError:
#        st.write("Some colmuns are missing")
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#    st.write("table: beverages")
#    st.dataframe(beverages)
#    st.write("table: food_items")
#    st.dataframe(food_items)
#    st.write("expected :")
#    st.dataframe(solution_df)
#
# with tab3:
#    st.write(answer_str)
