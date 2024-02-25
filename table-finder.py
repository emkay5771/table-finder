import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Table Finder 🪑",
    page_icon="🪑",
    layout="wide",
    initial_sidebar_state="collapsed",
)
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title("Table Finder 🪑")

# Read the excel file once and store it in a variable
df = pd.read_excel("table-list.xlsx")

# Get the unique names from the 'Name' column
names = df['Name'].unique()

name = st.selectbox("Type your name", names, index=None)

if name != "":
    # Find the row where 'Name' equals the selected name
    row = df[df['Name'] == name]
    
    # Check if such a row exists
    if not row.empty:
        # Get the table number from the second column ('Table')
        n = row['Table'].values[0]
        try:
            st.write(f"Your table is table {n}")
            specific, general = st.tabs(["Specific", "General"])
            with specific:
                st.image(f"images/{n}.jpg")
            with general:
                st.image("images/table-overview.jpg")
        except:
            st.write("Table not found")
else:
    st.write("No tables found for this name.")
