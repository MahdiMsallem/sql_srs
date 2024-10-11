import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dogs", "Owl"])

with tab1:
    input_text = st.text_area(label="Entrez votre query")
    st.write("My Table")
    st.dataframe(df)
    st.write(f"My SQL query is: {input_text}")
    #sql_query = f"{input_text}"
    result = duckdb.query(input_text).df()
    st.dataframe(result)