
import io

import duckdb
import pandas as pd
import streamlit as st

st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice"""
)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ?",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme",
    )
    st.write(f"You selected : {option}")

CSV = """
beverage,price
orange juice, 2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))

answer_str = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.query(answer_str).df()

st.header("enter your code:")
query = st.text_area(label="Here your SQL code")

if query:
    result = duckdb.query(query).df()
    st.dataframe(result)

    #    if len(result.columns) != len(solution_df.columns):
    #        st.write("Some columns are missing")
    #    n_lines_difference = result.shape[0] - solution_df.shape[0]

    #    if n_lines_difference != 0 :
    #        st.write(f"Result has a {n_lines_difference} lines differences with the solution")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError:
        st.write("Some colmuns are missing")

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected :")
    st.dataframe(solution_df)

with tab3:
    st.write(answer_str)
