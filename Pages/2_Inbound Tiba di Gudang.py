import streamlit as st
from src.constants import PAGE_TITLES
from src.data_access import load_data

st.set_page_config(layout="wide")

st.title(PAGE_TITLES["inbound_tiba"])

data = load_data("inbound_tiba")

st.write(data)