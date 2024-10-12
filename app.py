import streamlit as st
import pandas as pd
import duckdb
import io

csv = '''
beverage,price
orange juice, 2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
beverage,price
cookie juice, 2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * from beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()

with st.sidebar:
    option = st.selectbox(
        "How would you like to review",
        ["Joins", "GroupBy", "Windows Functions"],
        index=None,
        placeholder="Select a theme"
    )
    st.write('You selected', option)
<<<<<<< HEAD

=======
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
>>>>>>> 1b77bbd (add side-bar)

st.header("enter your code")
query = st.text_area(label="votre code sql ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table : beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab3:
    st.write(answer)