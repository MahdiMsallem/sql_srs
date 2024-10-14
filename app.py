# pylint: disable = missing-module-docstring

import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

#solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "How would you like to review",
        ["cross_joins", "GroupBy", "window_functions"],
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * from memory_state where theme = '{theme}'")
    st.write(exercise)
st.header("enter your code")
query = st.text_area(label="votre code sql ici", key="user_input")


#if query:
#    result = duckdb.sql(query).df()
#    st.dataframe(result)

#    if len(result.columns) != len(solution_df.columns):
#        st.write("Some Columns are missing")

#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError as e:
#        st.write("Some columns are missing")

#    n_lines_diff = result.shape[0] - solution_df.shape[0]
#    if n_lines_diff != 0:
#        st.write(
#            f"result has a difference of {abs(n_lines_diff)} line compared to solution_df"
#        )


#tab2, tab3 = st.tabs(["Tables", "solution_df"])

#with tab2:
#    st.write("table : beverages")
#    st.dataframe(beverages)
#    st.write("table: food_items")
#    st.dataframe(food_items)
#    st.write("expected")
#    st.dataframe(solution_df)

#with tab3:
#    st.write(ANSWER_STR)
