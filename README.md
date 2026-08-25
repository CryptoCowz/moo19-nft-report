# MOO19 News: The NFT Report & Newsletter Automation Pipeline 🐮📺

Automated research, scriptwriting, 10-second multi-clip video manifest generation, video bumpers, and weekly newsletter production for **MOO19 News / CryptoCowz**.

## Repository Structure

- `nft_report_agent.py`: Analyzes top 5 NFT collections across 4 core pillars, generates episode scripts (`weekly_nft_report_script.md`, `weekly_nft_report_shorts_script.md`), master manifest (`google_flow_animation_manifest.json`), 13 standalone clip JSONs (`clip_001` to `clip_013`), and 5 video bumpers (`bump_001` to `bump_005`).
- `newsletter_agent.py`: Curates mission-aligned Web3/NFT stories and formats the weekly edition of *The Pasture Post* (`weekly_pasture_post_newsletter.md`).
- `sync_to_gdrive.py`: Automatically syncs all files in `output/` directly to your Google Drive folder.
- `deploy_google_flow_render.py`: Optional API trigger for Google Flow rendering endpoints.
- `.github/workflows/weekly_production.yml`: GitHub Actions automated cron job (runs every Monday at 9:00 AM EDT).

## Setup & Configuration

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
