import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# Find the exact directory where this app.py script lives
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the exact, absolute path to your index.html file
file_path = os.path.join(current_dir, "index.html")

# Open the file using the absolute path
with open(file_path, "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=900, scrolling=True)
