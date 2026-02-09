import json
import streamlit as st
from google.oauth2.credentials import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def get_sheets_service():
    creds_info = json.loads(st.secrets["google_oauth"]["token"])
    creds = Credentials.from_authorized_user_info(
        creds_info,
        scopes=SCOPES
    )
    return creds