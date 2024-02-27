import io
import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition System SQL practice""")

with st.sidebar:
    option = st.selectbox(
        'What would you like to review ?',
        ('Joins', 'GroupBy', 'Windows Functions'),
        index=None,
        placeholder="Select a theme")
    st.write(f"You selected : {option}")

csv = '''
beverage,price
orange juice, 2.5
Expresso,2
Tea,3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.query(answer).df()

st.header("enter your code:")
query = st.text_area(label = "Here your SQL code")
st.dataframe(duckdb.query(query).df())

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected :")
    st.dataframe(solution)

with tab3:
    st.write(answer)
