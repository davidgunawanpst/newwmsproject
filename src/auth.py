from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_sheets_service():
    creds = Credentials.from_authorized_user_file(
        "secrets/token.json", SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    return service
