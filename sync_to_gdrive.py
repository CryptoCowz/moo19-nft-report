#!/usr/bin/env python3
"""
Syncs all generated output files from GitHub Actions to Google Drive.
"""

import os
import glob
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

FOLDER_ID = os.getenv("GDRIVE_FOLDER_ID", "1qmy-BiGcMdlYtlCiAtOsfxOvvXnD642x")
SERVICE_ACCOUNT_FILE = "gdrive_credentials.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]

def upload_files():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"[!] Warning: {SERVICE_ACCOUNT_FILE} not found. Skipping Google Drive sync.")
        return

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    drive_service = build("drive", "v3", credentials=creds)

    # Collect all generated files from output/
    files_to_upload = []
    for root, _, files in os.walk("output"):
        for f in files:
            files_to_upload.append(os.path.join(root, f))

    print(f"[*] Uploading {len(files_to_upload)} files to Google Drive Folder: {FOLDER_ID}...")

    for file_path in files_to_upload:
        file_name = os.path.basename(file_path)
        mime_type = "application/json" if file_name.endswith(".json") else "text/markdown"

        file_metadata = {
            "name": file_name,
            "parents": [FOLDER_ID]
        }
        media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)

        try:
            drive_service.files().create(
                body=file_metadata, media_body=media, fields="id"
            ).execute()
            print(f"[✓] Uploaded: {file_name}")
        except Exception as e:
            print(f"[!] Error uploading {file_name}: {e}")

if __name__ == "__main__":
    upload_files()
