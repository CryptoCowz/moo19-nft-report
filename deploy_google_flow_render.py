#!/usr/bin/env python3
"""
Google Flow API Automation Trigger for MOO19 TV The NFT Report
Sends google_flow_animation_manifest.json directly to Google Flow's rendering pipeline.
"""

import os
import json
import requests

GOOGLE_FLOW_API_ENDPOINT = os.getenv(
    "GOOGLE_FLOW_ENDPOINT", 
    "https://flow.googleapis.com/v1/projects/MOO19_TV_The_NFT_Report/renders"
)
API_KEY = os.getenv("GOOGLE_FLOW_API_KEY", "YOUR_GOOGLE_FLOW_API_KEY")
MANIFEST_PATH = os.path.join("output", "google_flow_animation_manifest.json")

def trigger_batch_render():
    if not os.path.exists(MANIFEST_PATH):
        print(f"[!] Error: {MANIFEST_PATH} not found.")
        return

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_payload = json.load(f)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print(f"[*] Sending batch render request for {manifest_payload.get('show_title')}...")
    
    try:
        response = requests.post(GOOGLE_FLOW_API_ENDPOINT, json=manifest_payload, headers=headers)
        
        if response.status_code in (200, 201, 202):
            result = response.json()
            print("[✓] Render job triggered successfully!")
            print(f"    - Render Job ID: {result.get('job_id', 'N/A')}")
        else:
            print(f"[!] API Request Failed (Status {response.status_code}): {response.text}")
    except Exception as e:
        print(f"[!] Network Error: {e}")

if __name__ == "__main__":
    trigger_batch_render()
