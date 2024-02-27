import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world!")
data = {"a": [1, 2, 3],
        "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.dataframe(df)
    sql_query = st.text_area(label="Entrez votre input")
    st.write(f"Vous avez entré la requête suivante : {sql_query}")
    result = duckdb.query(sql_query).df()
    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("A owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)