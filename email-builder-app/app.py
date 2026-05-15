import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode to fit your builder
st.set_page_config(layout="wide")

# Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render the HTML in Streamlit
# height=900 allows for scrolling inside the utility
components.html(html_code, height=900, scrolling=True)