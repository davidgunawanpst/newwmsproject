import streamlit as st
import json
import gspread
from google.oauth2.credentials import Credentials

st.title("Google Sheets Test")

# Load OAuth token from Streamlit secrets
token_info = json.loads(st.secrets["google_oauth"]["token"])

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_authorized_user_info(token_info, SCOPES)
client = gspread.authorize(creds)

SHEET_ID = "1W8uHHbW4L7inmQ82TRdC_4kdow1N0cVDepePK5rMusI"
sheet = client.open_by_key(SHEET_ID).sheet1

if st.button("Print"):
    value = sheet.acell("A1").value
    st.write("Cell A1 contains:")
    st.code(value)