import streamlit as st
import pandas as pd

import base64

st.set_page_config(
    page_title="Table Finder 🪑",
    page_icon="🪑",
    layout="centered",
    initial_sidebar_state="collapsed",
)


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
background_image=(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("https://github.com/emkay5771/table-finder/blob/main/images/background-darker-er.jpg?raw=true");
        background-size: 100vw;  # This sets the size to cover 100% of the viewport width and height
        background-position: 50%, 50%;  
        background-repeat: space repeat-y;
        backdrop-filter: blur(5px); 
    }}
    </style>
""")
st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: #692121 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(background_image, unsafe_allow_html=True)

st.title("Table Finder")

# Read the excel file once and store it in a variable
df = pd.read_excel("table-list.xlsx")

# Get the unique names from the 'Name' column
names = df['Name'].unique()

name = st.multiselect("Type your name to find your table", names, placeholder="Select a name")
with st.expander("Table Map Overview"):
    st.image("images/table-overview.jpg")
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
                    st.header(f"*{entry}* is sitting at table {n}.", divider="gray")
                    st.image(f"images/{n}.jpg")
            except:
                st.write("Table not found")
else:
    st.write("No tables found for this name.")
