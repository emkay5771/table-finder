import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Table Finder 🪑",
    page_icon="🪑",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Table Finder 🪑")

# Read the excel file once and store it in a variable
df = pd.read_excel("table-list.xlsx")

# Get the unique names from the 'Name' column
names = df['Name'].unique()

name = st.multiselect("Type your name", names, placeholder="Select a name")

if name != "":
    for entry in name:
        # Find the row where 'Name' equals the selected name
        row = df[df['Name'] == entry]
        #row = df[df['Name'] == name]
        
        # Check if such a row exists
        if not row.empty:
            # Get the table number from the second column ('Table')
            n = row['Table'].values[0]
            try:
                specific, general = st.tabs([f"{entry}'s Table", "Full Table Map"])
                with specific:
                    st.write(f"{entry} is sitting at table {n}.")
                    st.image(f"images/table{n}.jpg")
                with general:
                    st.image("images/table-overview.jpg")
            except:
                st.write("Table not found")
else:
    st.write("No tables found for this name.")
