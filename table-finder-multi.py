import streamlit as st
import pandas as pd

import base64

st.set_page_config(
    page_title="Table Finder 🪑",
    page_icon="🪑",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "Report a bug": None,
        'About': "Table Finder 🪑: A small utility to allow guests to find their table at an event. To contact the developer of this app, email them [here.](mailto:mkievman@outlook.com)",
    },
)

import streamlit as st
import pandas as pd


st.title("Table Finder")
# Your existing setup code...
with st.expander("Table Map Overview", expanded=True):
    st.image("images/table-overview.jpg")
# Read the excel file once and store it in a variable
df = pd.read_excel("Sorted Seating.xlsx")

# Get the unique names from the 'Name' column
names = df['Name'].unique()

# Create placeholders for each possible result
#placeholder = st.empty()
#with st.container():
    #placeholder_header = {name: st.empty() for name in names}
    #placeholder_image = {name: st.empty() for name in names}

st.header("Search for your name below:")
name = st.multiselect("", names, placeholder="Type in a name")

# Display the header


# Display the image if no name is selected
if not name:
    st.image("images/k-monogram-2.png")
else:
    # For each selected name, update the corresponding placeholder
    for entry in name:
        #container = st.container()

        row = df[df['Name'] == entry]
        if not row.empty:
            n = row['Table'].values[0]
            n = int(n)
            try:
                #with container:
                    #with placeholder.container():
                st.header(f"*{entry.strip()}* is sitting at table {n}.", divider="gray")
                st.image(f"images/{n}.jpg")
            except:
                st.write("Table not found")
    if len(name) == 0:
        st.write("No tables found for this name.")



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

#st.markdown(background_image, unsafe_allow_html=True)
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

footer {
    visibility: hidden !important;
    }
#root > div:nth-child(1) > div > div > a > div {
    visibility: hidden;
    }   
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}
    [data-testid="stToolbarActions"] > {
        display: none;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-zq5wmm.ezrtsby0 > div
    {
        display: none;
    }

</style>""",
unsafe_allow_html=True)