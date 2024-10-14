# pylint: disable = missing-module-docstring
import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice, 2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
beverage,price
cookie juice, 2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * from beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    option = st.selectbox(
        "How would you like to review",
        ["Joins", "GroupBy", "Windows Functions"],
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected", option)

st.header("enter your code")
query = st.text_area(label="votre code sql ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some Columns are missing")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_diff = result.shape[0] - solution_df.shape[0]
    if n_lines_diff != 0:
        st.write(
            f"result has a difference of {abs(n_lines_diff)} line compared to solution_df"
        )


tab2, tab3 = st.tabs(["Tables", "solution_df"])

with tab2:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_STR)
