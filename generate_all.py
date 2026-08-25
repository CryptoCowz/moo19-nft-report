#!/usr/bin/env python3
import os, sys, json
from datetime import datetime

print("[*] Starting All-in-One MOO19 Production Engine...")
now_str = datetime.now().strftime("%B %d, %Y")

output_dir = "output"
bumpers_dir = os.path.join(output_dir, "bumpers")
standalone_dir = os.path.join(output_dir, "standalone_clips")
os.makedirs(bumpers_dir, exist_ok=True)
os.makedirs(standalone_dir, exist_ok=True)

celeb_name = "Daisy M. (Minty) Ledger"
science_name = "Professor Hartmut von Schnurrbart"
weather_name = "Sunshine Innocent Nimbus"

# 1. Full Show Script
script_content = f"""# MOO19 NEWS: THE NFT REPORT (PUNCHY 10-SECOND CLIP SCRIPT WITH VIDEO BUMPS)
**Episode Air Date:** {now_str}
**Hosts:** {celeb_name} (Left Desk) & {science_name} (Right Desk next to microscope)
**Network:** MOO19 News Channel - The Pasture
**Master Background:** Newsroom01_Large copy.jpg

============================================================

### [CLIP 01: MOO19 NEWS STUDIO INTRO (10s Max)]
**{celeb_name.upper()}:** "Welcome back to MOO19 News! Today on the NFT Report, we're reviewing top digital flexes!"
**{science_name.upper()}:** "And check your screen for Cow-pedia Pop-ups and Scam or Stampede Checks! Let me examine the code!"

============================================================

### [BUMPER 01: CRYPTOPUNKS INTRO BUMP (4s)]
**VISUAL CUE:** Dynamic 2D graphic card displaying CryptoPunks art (24x24 pixel art portraits with gold chains and shades), floor price (30.3 ETH), and scannable QR Code linking to https://cryptopunks.app/.
**AUDIO STING & VOICEOVER:** "Up next on the NFT Report: CryptoPunks! Scan to explore!"

### [CLIP 02: CRYPTOPUNKS - LORE & GLAM (10s Max)]
**ON-SCREEN GRAPHIC:** CryptoPunks | Floor: 30.3 ETH | Vol: 66.79 ETH
**{celeb_name.upper()}:** "Darlings, CryptoPunks became digital status symbols when Jay-Z and Snoop Dogg flexed Punks #6095 and #3831! 66.79 ETH volume!"
**{celeb_name.upper()}:** "Glam & Hype Rating: 7.8/10!"

### [CLIP 03: CRYPTOPUNKS - TECH & CODE (10s Max)]
**[COW-PEDIA POP-UP]:** **On-Chain** — Verified technical asset storage architecture.
**{science_name.upper()}:** "Fascinating! CryptoPunks code is stored 100% on Ethereum. Pure digital identity and blue-chip store of value."
**{science_name.upper()}:** "Code & Security Rating: 9.5/10!"

----------------------------------------

### [BUMPER 02: PUDGY PENGUINS INTRO BUMP (4s)]
**VISUAL CUE:** Dynamic 2D graphic card displaying Pudgy Penguins art (cute chubby penguin avatars with winter beanies and scarves), floor price (6.05 ETH), and scannable QR Code linking to https://pudgypenguins.com/.
**AUDIO STING & VOICEOVER:** "Up next on the NFT Report: Pudgy Penguins! Scan to explore!"

### [CLIP 04: PUDGY PENGUINS - LORE & GLAM (10s Max)]
**ON-SCREEN GRAPHIC:** Pudgy Penguins | Floor: 6.05 ETH | Vol: 255.94 ETH
**{celeb_name.upper()}:** "Darlings, look at Pudgy Penguins! 8,888 cute penguins spreading good vibes with 255.94 ETH volume!"
**{celeb_name.upper()}:** "Glam & Hype Rating: 10.0/10!"

### [CLIP 05: PUDGY PENGUINS - TECH & CODE (10s Max)]
**[COW-PEDIA POP-UP]:** **IPFS** — Verified technical asset storage architecture.
**{science_name.upper()}:** "Fascinating! Pudgy Penguins uses ERC-721 with IPFS hosting, physical Pudgy Toys merch, and Overpass IP licensing."
**{science_name.upper()}:** "Code & Security Rating: 8.0/10!"

----------------------------------------

### [BUMPER 03: BORED APE YACHT CLUB INTRO BUMP (4s)]
**VISUAL CUE:** Dynamic 2D graphic card displaying Bored Ape Yacht Club art (expressive bored ape avatars with sailor caps and leather jackets), floor price (5.94 ETH), and scannable QR Code linking to https://boredapeyachtclub.com/.
**AUDIO STING & VOICEOVER:** "Up next on the NFT Report: Bored Ape Yacht Club! Scan to explore!"

### [CLIP 06: BORED APE YACHT CLUB - LORE & GLAM (10s Max)]
**ON-SCREEN GRAPHIC:** Bored Ape Yacht Club | Floor: 5.94 ETH | Vol: 42.34 ETH
**{celeb_name.upper()}:** "Darlings, Bored Ape Yacht Club features 10,000 iconic apes defining Web3 pop-culture with 42.34 ETH volume!"
**{celeb_name.upper()}:** "Glam & Hype Rating: 7.3/10!"

### [CLIP 07: BORED APE YACHT CLUB - TECH & CODE (10s Max)]
**[COW-PEDIA POP-UP]:** **IPFS** — Verified technical asset storage architecture.
**{science_name.upper()}:** "Fascinating! BAYC grants full commercial IP usage rights, ApeCoin allocations, and Otherside metaverse land access."
**{science_name.upper()}:** "Code & Security Rating: 8.0/10!"

----------------------------------------

### [BUMPER 04: INFINEX PATRONS INTRO BUMP (4s)]
**VISUAL CUE:** Dynamic 2D graphic card displaying Infinex Patrons art (holographic patronage card and token nodes), floor price (1.79 ETH), and scannable QR Code linking to https://infinex.xyz/.
**AUDIO STING & VOICEOVER:** "Up next on the NFT Report: Infinex Patrons! Scan to explore!"

### [CLIP 08: INFINEX PATRONS - LORE & GLAM (10s Max)]
**ON-SCREEN GRAPHIC:** Infinex Patrons | Floor: 1.79 ETH | Vol: 65.91 ETH
**{celeb_name.upper()}:** "Darlings, Infinex Patrons are foundational patronage NFTs for the non-custodial cross-chain platform with 65.91 ETH volume!"
**{celeb_name.upper()}:** "Glam & Hype Rating: 6.8/10!"

### [CLIP 09: INFINEX PATRONS - TECH & CODE (10s Max)]
**[COW-PEDIA POP-UP]:** **Arweave** — Verified technical asset storage architecture.
**{science_name.upper()}:** "Fascinating! Infinex Patrons receive platform revenue yield share stored permanently on Arweave with governance rights."
**{science_name.upper()}:** "Code & Security Rating: 8.8/10!"

----------------------------------------

### [BUMPER 05: CHROMIE SQUIGGLE INTRO BUMP (4s)]
**VISUAL CUE:** Dynamic 2D graphic card displaying Chromie Squiggle art (rainbow generative ribbon on clean canvas), floor price (2.58 ETH), and scannable QR Code linking to https://artblocks.io/collection/chromie-squiggle-by-snowfro.
**AUDIO STING & VOICEOVER:** "Up next on the NFT Report: Chromie Squiggle by Snowfro! Scan to explore!"

### [CLIP 10: CHROMIE SQUIGGLE - LORE & GLAM (10s Max)]
**ON-SCREEN GRAPHIC:** Chromie Squiggle by Snowfro | Floor: 2.58 ETH | Vol: 9.93 ETH
**{celeb_name.upper()}:** "Darlings, Chromie Squiggle by Snowfro is seminal generative art of colorful undulating ribbons with 9.93 ETH volume!"
**{celeb_name.upper()}:** "Glam & Hype Rating: 5.7/10!"

### [CLIP 11: CHROMIE SQUIGGLE - TECH & CODE (10s Max)]
**[COW-PEDIA POP-UP]:** **On-Chain** — Verified technical asset storage architecture.
**{science_name.upper()}:** "Fascinating! Chromie Squiggle executes on-chain rendering scripts derived directly from transaction hash seeds."
**{science_name.upper()}:** "Code & Security Rating: 9.5/10!"

----------------------------------------

### [CLIP 12: MOO19 WEATHER FORECAST (10s Max)]
**{weather_name.upper()}:** "Expect high volatility across ERC-721 tokens tonight with an 80% chance of a bull surge! Embrace the chaos, traders!"

### [CLIP 13: MOO19 STUDIO OUTRO (10s Max)]
**{celeb_name.upper()}:** "That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote!"
**{science_name.upper()}:** "Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight!"
"""

with open(os.path.join(output_dir, "weekly_nft_report_script.md"), "w", encoding="utf-8") as f:
    f.write(script_content)

# 2. Shorts Script
shorts_content = f"""# MOO19 NEWS: NFT REPORT SHORTS (60-SECOND TEASER)
**Air Date:** {now_str}
**Format:** 9:16 Vertical Video (TikTok / YouTube Shorts / Instagram Reels)

============================================================

**[00:00 - 00:10] {celeb_name.upper()}:** "Stop scrolling, pasture trendsetters! Here are this week's top 3 selling NFTs on MOO19 News!"
**[00:10 - 00:25] {celeb_name.upper()}:** "#1 CryptoPunks with 66.79 ETH volume! Jay-Z and Snoop Dogg flexed Punks #6095 and #3831!"
**[00:25 - 00:40] {science_name.upper()}:** "#2 Pudgy Penguins with 255.94 ETH volume using ERC-721 and IPFS metadata hosting!"
**[00:40 - 00:50] {celeb_name.upper()}:** "#3 Bored Ape Yacht Club with full commercial IP rights and ApeCoin perks!"
**[00:50 - 01:00] {science_name.upper()}:** "Scan the QR code to watch the full episode on MOO19 News and vote on our Pasture Poll! Don't trust, verify!"
"""
with open(os.path.join(output_dir, "weekly_nft_report_shorts_script.md"), "w", encoding="utf-8") as f:
    f.write(shorts_content)

# 3. Weekly Newsletter
newsletter_content = f"""# 🐮 THE PASTURE POST: MOO19 NFT & WEB3 WEEKLY
**Issue #15 • {now_str}**
*Demystifying the Blockchain with Culture, Code, and Common Sense*

=================================================================

## 🎙️ FROM THE NEWSROOM DESK
**{celeb_name.upper()} (Celebrity Reporter):**
> "Hello, pasture fashionistas and Web3 explorers! Welcome to this week's edition of *The Pasture Post*. We've rounded up the hottest mainstream crossovers, biggest retail drops, and cultural alpha across the metaverse!"

**{science_name.upper()} (Science Reporter):**
> "And I'm here to ensure we dissect the technical anatomy behind the headlines! This week, we examine how on-chain generative algorithms and decentralized storage are turning digital code into museum-grade fine art. Let's dig into the data!"

-----------------------------------------------------------------

## 📰 TOP STORIES THIS WEEK (ALIGNED WITH THE MOO19 MISSION)

### 1. Pudgy Penguins Expands Global Toy Line to Major Retailers Nationwide
**Category:** Mainstream & Brand Expansion | **Source:** [Pudgy Penguins](https://pudgypenguins.com/)
**The Story:** Pudgy Penguins continues bridging digital collectibles to physical retail, generating over $10M in toy sales while onboarding non-crypto consumers via embedded QR-code digital passport wallets.
💡 **The Pasture Takeaway:** Proves that digital IP can thrive as a mainstream toy and entertainment brand without requiring users to be crypto experts.
💬 **Daisy's Glam Commentary:** *"Watching digital characters turn into real-world plush toys sold in Walmart is proof that community vibes and cute IP rule the world!"*

----------------------------------------

### 2. Museum of Modern Art (MoMA) Acquires Historic On-Chain Generative Artworks
**Category:** On-Chain Tech & Generative Art | **Source:** [Art Blocks Chromie Squiggle](https://artblocks.io/collection/chromie-squiggle-by-snowfro)
**The Story:** Major international art institutions add seminal on-chain algorithmic artworks (including Chromie Squiggles and CryptoPunks) to permanent collections, validating code as a fine art medium.
💡 **The Pasture Takeaway:** Highlights the difference between temporary off-chain JPEGs and immutable on-chain generative scripts that live forever on Ethereum.
🔬 **Professor Hartmut's Tech Note:** *"Notice the key technical distinction: When code is stored on-chain like Chromie Squiggle or CryptoPunks, the artwork cannot be deleted even if servers go down!"*

----------------------------------------

### 3. Infinex Patron NFT Model Pioneering Non-Custodial Platform Revenue Sharing
**Category:** DeFi & Yield-Bearing Utilities | **Source:** [Infinex](https://infinex.xyz/)
**The Story:** Infinex demonstrates how NFTs can serve as transparent revenue-sharing and patronage instruments for decentralized infrastructure rather than purely speculative profile pictures.
💡 **The Pasture Takeaway:** Shows how smart contracts transform digital tokens into productive, yield-bearing assets with verifiable on-chain governance.
📊 **Bull vs. Bear Meter:** *"DeFi patronage models are proving that NFTs can be functional productive assets rather than just flipping JPEGs!"*

----------------------------------------

### 4. Smart Contract Audits & Decentralized Metadata: Why 'Don't Trust, Verify' Matters More Than Ever
**Category:** Security, Anti-Scam & 'Don't Trust, Verify' | **Source:** [CryptoPunks](https://cryptopunks.app/)
**The Story:** A breakdown of common metadata vulnerabilities and why collectors must verify contract source code, creator royalties, and decentralized storage permanence before purchasing.
💡 **The Pasture Takeaway:** Educates everyday buyers on running basic contract checks to protect their wallets from centralized points of failure.
🛡️ **Frank Rizzo's Safety Corner:** *"Remember the golden rule of the streets: Don't trust, verify! Always inspect contract permissions before signing transactions."*

----------------------------------------

## 📚 COW-PEDIA TERM OF THE WEEK
**Term: Immutability (On-Chain Storage)**
> *Definition:* The state of being unchangeable. In blockchain, once data or code is written to an immutable smart contract (like Ethereum or Arweave), it cannot be modified, edited, or deleted by anyone—not even the original creator!
> 
> *Why It Matters in Plain English:* If you own an immutable digital collectible, no central company can change the artwork or turn off your access.

-----------------------------------------------------------------

## ⛈️ MARKET CLIMATE OUTLOOK
**Forecast by {weather_name}:**
> "Current indicators show an **80% chance of a bull surge** across verified utility collections with steady floor price consolidation. Keep an eye out for sudden volatility storms around upcoming Layer-2 network upgrades! Embrace the chaos, traders!"

-----------------------------------------------------------------

## 🗳️ WEEKLY PASTURE POLL
**Which project should Daisy and Professor Hartmut examine on next Monday's animated episode?**
1. On-Chain Generative Art Collection
2. Web3 Gaming & Metaverse Asset
3. Real-World Asset (RWA) Tokenization Project

👉 *Cast your vote by replying to this newsletter or voting in our Discord community!*

=================================================================
© 2026 CryptoCowz / MOO19 News • *Demystifying cryptocurrency until the cows come home!*
Follow us: [YouTube](https://www.youtube.com/@cryptocollectablesNY) | [Facebook](https://www.facebook.com/CryptocollectiblesNY)
"""

with open(os.path.join(output_dir, "weekly_pasture_post_newsletter.md"), "w", encoding="utf-8") as f:
    f.write(newsletter_content)

# 4. Master Animation Manifest & Standalone Clips & Bumpers
manifest_data = {
    "manifest_version": "1.0",
    "google_flow_project_target": "MOO19 TV The NFT Report",
    "show_title": "MOO19 NFT Report - Production Manifest with Video Bumpers",
    "target_model": "Omni Flash (10s Dialogue Clips & 4s Bumpers)",
    "clip_duration_seconds": 10,
    "bumper_duration_seconds": 4,
    "total_duration_seconds": 150,
    "master_assets": {
        "environment": {
            "asset_id": "Newsroom01_Large copy.jpg",
            "file_name": "Newsroom01_Large copy.jpg",
            "type": "2D_BACKGROUND_PLATE"
        },
        "character_references": [
            {"character_id": "CELEBRITY_REPORTER", "character_name": celeb_name, "file_name": "CelebReporter_2k.png", "layer_position": {"x_percent": 18, "y_percent": 30, "scale": 1.0}},
            {"character_id": "SCIENCE_REPORTER", "character_name": science_name, "file_name": "ScienceReporter_2k.png", "layer_position": {"x_percent": 68, "y_percent": 30, "scale": 1.0}}
        ]
    },
    "bumpers": [],
    "clips": []
}

bumpers_data = [
    ("bump_001", "CryptoPunks", "https://cryptopunks.app/", "https://opensea.io/collection/cryptopunks", "30.3", "Ethereum", "Iconic 24x24 pixel art portraits on vibrant solid background with rare punk traits like gold chains, wild hair, and shades"),
    ("bump_002", "Pudgy Penguins", "https://pudgypenguins.com/", "https://opensea.io/collection/pudgypenguins", "6.05", "Ethereum", "Vibrant 2D illustrated cute chubby penguin characters with winter beanies, scarves, and cheerful expressions"),
    ("bump_003", "Bored Ape Yacht Club", "https://boredapeyachtclub.com/", "https://opensea.io/collection/boredapeyachtclub", "5.94", "Ethereum", "2D cel-shaded expressive bored ape avatars with sailor caps, leather jackets, neon traits, and party horns"),
    ("bump_004", "Infinex Patrons", "https://infinex.xyz/", "https://opensea.io/collection/infinex-patrons", "1.79", "Ethereum", "Sleek holographic 2D card art displaying cross-chain patronage insignia and dynamic geometric token nodes"),
    ("bump_005", "Chromie Squiggle by Snowfro", "https://artblocks.io/collection/chromie-squiggle-by-snowfro", "https://opensea.io/collection/chromie-squiggle-by-snowfro", "2.58", "Ethereum", "Hypnotic undulating 2D rainbow generative spectrum ribbon looping fluidly on a clean digital canvas")
]

for bid, bname, burl, bopensea, bfloor, bchain, bart in bumpers_data:
    b_spoken = f"Up next on the NFT Report: {bname}! Scan the QR code to explore!"
    b_prompt = f"2D animated high-energy motion graphic bumper card, 4 seconds. Center featured 2D artwork of {bname} ({bart}). Prominent scannable QR Code on right overlay linking to {burl}. Lower third displaying '{bname} | Floor: {bfloor} ETH | Chain: {bchain}'. Audio sting with energetic voiceover: '{b_spoken}'"
    b_obj = {
        "manifest_version": "1.0",
        "google_flow_project_target": "MOO19 TV The NFT Report",
        "clip_id": bid,
        "clip_type": "SEGMENT_BUMPER",
        "duration_seconds": 4,
        "title": f"Bumper: {bname} Intro",
        "featured_nft": bname,
        "official_url": burl,
        "opensea_url": bopensea,
        "qr_code_target_url": burl,
        "prompt": b_prompt,
        "script": b_spoken,
        "text_prompt": b_prompt,
        "voice_prompt": b_spoken,
        "speech": b_spoken,
        "audio_sting": "MOO19_Station_Chime_Fast_4s.mp3",
        "visual_elements": {
            "featured_artwork_style": bart,
            "qr_code_overlay": {
                "position": "BOTTOM_RIGHT",
                "target_url": burl,
                "callout_label": f"SCAN TO VIEW {bname.upper()}"
            },
            "lower_third_badge": f"{bname} | Floor: {bfloor} ETH | {bchain}"
        }
    }
    manifest_data["bumpers"].append(b_obj)
    b_clean = bname.lower().replace(" ", "_").replace(":", "")
    with open(os.path.join(bumpers_dir, f"{bid}_{b_clean}_bump.json"), "w", encoding="utf-8") as bf:
        json.dump(b_obj, bf, indent=2)

clips_info = [
    ("clip_001", "Clip 01: Studio Intro", f"{celeb_name}: Welcome back to MOO19 News! Today on the NFT Report, we're reviewing top digital flexes! {science_name}: And check your screen for Cow-pedia Pop-ups and Scam or Stampede Checks! Let me examine the code!", [celeb_name, science_name], {}),
    ("clip_002", "Clip 02: CryptoPunks (Celeb Lore)", f"{celeb_name}: Darlings, CryptoPunks became digital status symbols when Jay-Z and Snoop Dogg flexed Punks #6095 and #3831! 66.79 ETH volume! Glam Rating: 7.8/10!", [celeb_name], {"lower_third_text": "CryptoPunks | Floor: 30.3 ETH | Vol: 66.79 ETH", "hype_badge": "Hype: 7.8/10", "gauge_status": "BULLISH STAMPEDE 🟢"}),
    ("clip_003", "Clip 03: CryptoPunks (Science Tech)", f"{science_name}: Fascinating! CryptoPunks code is stored 100% on Ethereum. Pure digital identity and blue-chip store of value. Code Rating: 9.5/10!", [science_name], {"cowpedia_banner": "Cow-pedia: On-Chain Verified On-Chain", "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH", "tech_badge": "Tech: 9.5/10"}),
    ("clip_004", "Clip 04: Pudgy Penguins (Celeb Lore)", f"{celeb_name}: Darlings, look at Pudgy Penguins! 8,888 cute penguins spreading good vibes with 255.94 ETH volume! Glam Rating: 10.0/10!", [celeb_name], {"lower_third_text": "Pudgy Penguins | Floor: 6.05 ETH | Vol: 255.94 ETH", "hype_badge": "Hype: 10.0/10", "gauge_status": "BULLISH STAMPEDE 🟢"}),
    ("clip_005", "Clip 05: Pudgy Penguins (Science Tech)", f"{science_name}: Fascinating! Pudgy Penguins uses ERC-721 with IPFS hosting, physical Pudgy Toys merch, and Overpass IP licensing. Code Rating: 8.0/10!", [science_name], {"cowpedia_banner": "Cow-pedia: IPFS Verified On-Chain", "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH", "tech_badge": "Tech: 8.0/10"}),
    ("clip_006", "Clip 06: Bored Ape Yacht Club (Celeb Lore)", f"{celeb_name}: Darlings, Bored Ape Yacht Club features 10,000 iconic apes defining Web3 pop-culture with 42.34 ETH volume! Glam Rating: 7.3/10!", [celeb_name], {"lower_third_text": "Bored Ape Yacht Club | Floor: 5.94 ETH | Vol: 42.34 ETH", "hype_badge": "Hype: 7.3/10", "gauge_status": "BULLISH STAMPEDE 🟢"}),
    ("clip_007", "Clip 07: Bored Ape Yacht Club (Science Tech)", f"{science_name}: Fascinating! BAYC grants full commercial IP usage rights, ApeCoin allocations, and Otherside metaverse land access. Code Rating: 8.0/10!", [science_name], {"cowpedia_banner": "Cow-pedia: IPFS Verified On-Chain", "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH", "tech_badge": "Tech: 8.0/10"}),
    ("clip_008", "Clip 08: Infinex Patrons (Celeb Lore)", f"{celeb_name}: Darlings, Infinex Patrons are foundational patronage NFTs for the non-custodial cross-chain platform with 65.91 ETH volume! Glam Rating: 6.8/10!", [celeb_name], {"lower_third_text": "Infinex Patrons | Floor: 1.79 ETH | Vol: 65.91 ETH", "hype_badge": "Hype: 6.8/10", "gauge_status": "BULLISH STAMPEDE 🟢"}),
    ("clip_009", "Clip 09: Infinex Patrons (Science Tech)", f"{science_name}: Fascinating! Infinex Patrons receive platform revenue yield share stored permanently on Arweave with governance rights. Code Rating: 8.8/10!", [science_name], {"cowpedia_banner": "Cow-pedia: Arweave Verified On-Chain", "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH", "tech_badge": "Tech: 8.8/10"}),
    ("clip_010", "Clip 10: Chromie Squiggle by Snowfro (Celeb Lore)", f"{celeb_name}: Darlings, Chromie Squiggle by Snowfro is seminal generative art of colorful undulating ribbons with 9.93 ETH volume! Glam Rating: 5.7/10!", [celeb_name], {"lower_third_text": "Chromie Squiggle by Snowfro | Floor: 2.58 ETH | Vol: 9.93 ETH", "hype_badge": "Hype: 5.7/10", "gauge_status": "BULLISH STAMPEDE 🟢"}),
    ("clip_011", "Clip 11: Chromie Squiggle by Snowfro (Science Tech)", f"{science_name}: Fascinating! Chromie Squiggle executes on-chain rendering scripts derived directly from transaction hash seeds. Code Rating: 9.5/10!", [science_name], {"cowpedia_banner": "Cow-pedia: On-Chain Verified On-Chain", "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH", "tech_badge": "Tech: 9.5/10"}),
    ("clip_012", "Clip 12: Weather Forecast", f"{weather_name}: Expect high volatility across ERC-721 tokens tonight with an 80% chance of a bull surge! Embrace the chaos, traders!", [weather_name], {}),
    ("clip_013", "Clip 13: Studio Outro", f"{celeb_name}: That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote! {science_name}: Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight!", [celeb_name, science_name], {"pasture_poll_qr_code": "SCAN QR CODE TO VOTE FOR NEXT WEEK'S WILDCARD NFT"})
]

for cid, title, script_text, chars, overlays in clips_info:
    clip_obj = {
        "manifest_version": "1.0",
        "google_flow_project_target": "MOO19 TV The NFT Report",
        "clip_id": cid,
        "duration_seconds": 10,
        "title": title,
        "source": "Newsroom01_Large copy.jpg",
        "prompt": f"2D cel-shaded cartoon news broadcast, Newsroom01_Large copy.jpg background plate with curved wooden news desk. Spoken audio line: '{script_text}'",
        "script": script_text,
        "text_prompt": f"2D cel-shaded cartoon news broadcast, Newsroom01_Large copy.jpg background plate with curved wooden news desk. Spoken audio line: '{script_text}'",
        "voice_prompt": script_text,
        "speech": script_text,
        "character_references": chars,
        "gui_overlays": overlays
    }
    manifest_data["clips"].append(clip_obj)
    clean_title = title.lower().replace(" ", "_").replace(":", "")
    with open(os.path.join(standalone_dir, f"{cid}_{clean_title}.json"), "w", encoding="utf-8") as cf:
        json.dump(clip_obj, cf, indent=2)

with open(os.path.join(output_dir, "google_flow_animation_manifest.json"), "w", encoding="utf-8") as mf:
    json.dump(manifest_data, mf, indent=2)

print("[✓] All production assets generated successfully!")
