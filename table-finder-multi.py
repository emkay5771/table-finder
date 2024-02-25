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
        background-image: url("https://github.com/emkay5771/table-finder/blob/main/images/k-monogram.jpg?raw=true");
        background-size: 100vw !important;  # This sets the size to cover 100% of the viewport width and height 
        background-repeat: none !important;  # This ensures that the image is only shown once
        backdrop-filter: blur(5px); 
    }}
    </style>
""")
st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: #e7aa54 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(background_image, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    div[data-testid="stExpander"] details summary p{
    font-size: 1.5rem;
}
</style>
    """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    #MainMenu {
  visibility: hidden;
}
footer {
    visibility: hidden !important;
    }
#root > div:nth-child(1) > div > div > a > div {
    visibility: hidden;
    }   
    </style>
    """, unsafe_allow_html=True)
st.title("Table Finder")
with st.expander("Table Map Overview"):
    st.image("images/table-overview.jpg")
# Read the excel file once and store it in a variable
df = pd.read_excel("table-list.xlsx")

# Get the unique names from the 'Name' column
names = df['Name'].unique()
st.subheader("Type your name to find your table")
name = st.multiselect("",names, placeholder="Select a name")
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
