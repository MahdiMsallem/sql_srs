# pylint: disable = missing-module-docstring
import logging
import os
import duckdb
import streamlit as st

if "data" not in os.listdir():
    print("creating data folder")
    logging.error(os.listdir())
    logging.error("creating data folder")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)


with st.sidebar:
    theme = st.selectbox(
        "How would you like to review",
        ["cross_joins", "GroupBy", "window_functions"],
        index=None,
        placeholder="Select a theme",
    )
    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * from memory_state where theme = '{theme}'").df().sort_values("last_reviewed").reset_index()
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r", encoding="utf-8") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("enter your code")
query = st.text_area(label="votre code sql ici", key="user_input")


if query:
    result = con.execute(query).df()
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
    # st.write(exercise.loc[0, "tables"])
    try:
        exercise_tables = exercise.loc[0, "tables"]
        for table in exercise_tables:
            st.write(f"table: {table}")
            df_table = con.execute(f"SELECT * from {table}").df()
            st.dataframe(df_table)
    except KeyError:
        st.print("Select a theme from the side bar")
# st.write("table: food_items")
# st.dataframe(food_items)
#    st.write("expected")
#    st.dataframe(solution_df)

with tab3:
    st.write(answer)
