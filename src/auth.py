import json
import streamlit as st
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def get_sheets_service():
    creds_info = json.loads(st.secrets["google_oauth"]["token"])
    creds = Credentials.from_authorized_user_info(creds_info, SCOPES)

    service = build("sheets", "v4", credentials=creds)
    return service