import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import os
from config import SPREADSHEET_ID, SHEET_NAME

def load_wantlist():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(
        filename=os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
        scopes=scopes
    )

    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
    records = sheet.get_all_records()

    wantlist = []
    for row in records:
        artist = row.get("ARTIST")
        title = row.get("TITLE")
        if artist and title:
            wantlist.append({
                "artist": artist.strip(),
                "title": title.strip()
            })

    return wantlist
