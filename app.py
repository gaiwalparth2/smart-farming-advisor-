import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Smart Farming Advisor",
    page_icon="🌾",
    layout="wide"
)

# This automatically finds the HTML file in the same folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Try multiple possible filenames
possible_names = [
    "smart-farming-advisor.html",
    "smart_farming_advisor.html", 
    "smart-farming-advisor (5).html",
    "smart-farming-advisor (4).html",
    "smart-farming-advisor(5).html",
    "smart-farming-advisor(4).html",
]

html_file = None
for name in possible_names:
    path = os.path.join(BASE_DIR, name)
    if os.path.exists(path):
        html_file = path
        break

if html_file is None:
    st.error("HTML file not found! Files in directory:")
    for f in os.listdir(BASE_DIR):
        st.write(f)
    st.stop()

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=True)