import json
import os
import streamlit as st
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def get_sheets_service():
    # --- Cloud (Streamlit) ---
    if "google_oauth" in st.secrets:
        creds_info = json.loads(st.secrets["google_oauth"]["token"])
        creds = Credentials.from_authorized_user_info(
            creds_info, SCOPES
        )

    # --- Local dev ---
    else:
        with open("secrets/token.json", "r") as f:
            creds_info = json.load(f)
        creds = Credentials.from_authorized_user_info(
            creds_info, SCOPES
        )

    return build("sheets", "v4", credentials=creds)