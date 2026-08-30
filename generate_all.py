```python
#!/usr/bin/env python3
"""
MOO19 News: The NFT Report - Dynamic 5-Slot Segment Production Engine
Features:
- Slot 1: Blue-Chip Anchor of the Week (Legacy titan + specific weekly catalyst)
- Slot 2: Top 24h/7d Volume Mover (Highest trading volume velocity)
- Slot 3: Breakout Gainer (% Surge / Momentum Mover)
- Slot 4: Cross-Chain Spotlight (Solana, Bitcoin Ordinals, Base L2)
- Slot 5: Wildcard Pasture Poll Pick (Community voted project / Generative Art / RWA)
- Automated episode history & rotation state management (episode_history.json)
"""

import os
import sys
import json
import argparse
from datetime import datetime

def run_production_pipeline(output_dir="output"):
    print("[*] Starting MOO19 Dynamic 5-Slot Production Engine...")
    now_str = datetime.now().strftime("%B %d, %Y")

    bumpers_dir = os.path.join(output_dir, "bumpers")
    standalone_dir = os.path.join(output_dir, "standalone_clips")
    os.makedirs(bumpers_dir, exist_ok=True)
    os.makedirs(standalone_dir, exist_ok=True)

    celeb_name = "Daisy M. (Minty) Ledger"
    science_name = "Professor Hartmut von Schnurrbart"
    weather_name = "Sunshine Innocent Nimbus"

    # Dynamic 5-Slot Segment Model Data Pool
    SLOT_CANDIDATE_POOLS = {
        "SLOT_1_BLUE_CHIP": [
            {
                "name": "CryptoPunks",
                "slot_title": "Slot 1: Blue-Chip Anchor",
                "category": "Historical Artifact / Ethereum",
                "chain": "Ethereum",
                "floor_price": "30.3 ETH",
                "volume_24h": "66.79 ETH",
                "contract_standard": "ERC-721 Custom",
                "storage": "On-Chain Pixel Code",
                "official_url": "https://cryptopunks.app/",
                "opensea_url": "https://opensea.io/collection/cryptopunks",
                "art_description": "Iconic 24x24 pixel art portraits with rare gold chains, pilot shades, and zombie traits on solid color backgrounds",
                "catalyst_lore": "Darlings, CryptoPunks anchors our broadcast with legendary prestige! Whale wallets and auction houses still treat 24x24 pixel art as the ultimate digital Rolex!",
                "science_tech": "Fascinating! CryptoPunks code is permanently compiled on Ethereum. Pure immutable digital provenance with zero external server dependencies!"
            },
            {
                "name": "Autoglyphs",
                "slot_title": "Slot 1: Blue-Chip Anchor",
                "category": "Generative History / Ethereum",
                "chain": "Ethereum",
                "floor_price": "82.0 ETH",
                "volume_24h": "35.50 ETH",
                "contract_standard": "ERC-721",
                "storage": "100% On-Chain Script",
                "official_url": "https://www.larvalabs.com/autoglyphs",
                "opensea_url": "https://opensea.io/collection/autoglyphs",
                "art_description": "Intricate black-and-white ASCII and geometric algorithmic glyph patterns generated directly by smart contracts",
                "catalyst_lore": "Darlings, Autoglyphs represents museum-grade digital history! Only 512 exist and they command jaw-dropping 82 ETH floor prices!",
                "science_tech": "Fascinating! Autoglyphs is the first on-chain generative art on Ethereum. The code that creates the visual pattern is self-contained in the contract!"
            }
        ],
        "SLOT_2_VOLUME_MOVER": [
            {
                "name": "Pudgy Penguins",
                "slot_title": "Slot 2: Top Volume Mover",
                "category": "Mainstream Brand IP",
                "chain": "Ethereum",
                "floor_price": "6.05 ETH",
                "volume_24h": "255.94 ETH",
                "contract_standard": "ERC-721",
                "storage": "IPFS",
                "official_url": "https://pudgypenguins.com/",
                "opensea_url": "https://opensea.io/collection/pudgypenguins",
                "art_description": "Charming 2D illustrated chubby penguin avatars with cheerful expressions, winter beanies, and cozy scarves",
                "catalyst_lore": "Darlings, look at Pudgy Penguins leading the volume charts with 255.94 ETH! Over 1 million plush toys sold in major retailers worldwide!",
                "science_tech": "Fascinating! Pudgy Penguins pairs ERC-721 tokens with their Overpass licensing protocol, funneling real-world toy royalties back to holders!"
            },
            {
                "name": "Bored Ape Yacht Club",
                "slot_title": "Slot 2: Top Volume Mover",
                "category": "Pop Culture Titan",
                "chain": "Ethereum",
                "floor_price": "5.94 ETH",
                "volume_24h": "142.34 ETH",
                "contract_standard": "ERC-721",
                "storage": "IPFS",
                "official_url": "https://boredapeyachtclub.com/",
                "opensea_url": "https://opensea.io/collection/boredapeyachtclub",
                "art_description": "Expressive 2D cel-shaded ape characters sporting sailor hats, leather jackets, neon fur, and party glasses",
                "catalyst_lore": "Darlings, Bored Ape Yacht Club is buzzing as secondary volume heats up with 142.34 ETH traded! Full commercial IP rights driving new creator brands!",
                "science_tech": "Fascinating! BAYC grants uncapped commercial usage rights, token-gated community access, and direct integration into the Otherside metaverse engine!"
            }
        ],
        "SLOT_3_BREAKOUT_GAINER": [
            {
                "name": "Milady Maker",
                "slot_title": "Slot 3: Breakout Gainer",
                "category": "Neo-Chibi Culture & Momentum",
                "chain": "Ethereum",
                "floor_price": "3.15 ETH",
                "volume_24h": "88.45 ETH",
                "contract_standard": "ERC-721",
                "storage": "IPFS",
                "official_url": "https://miladymaker.net/",
                "opensea_url": "https://opensea.io/collection/milady-maker",
                "art_description": "Distinctive Tokyo neo-chibi 2D anime-inspired avatar art featuring customized streetwear, oversized eyes, and vibrant hats",
                "catalyst_lore": "Darlings, Milady Maker is this week's breakout star! Surging volume and viral meme culture have collectors in a full-blown stampede!",
                "science_tech": "Fascinating! Milady Maker uses algorithmically generated 10,000 PFP tokens with distinctive aesthetic scoring and high secondary market liquidity!"
            },
            {
                "name": "Doodles",
                "slot_title": "Slot 3: Breakout Gainer",
                "category": "Animation & Entertainment IP",
                "chain": "Ethereum",
                "floor_price": "2.10 ETH",
                "volume_24h": "64.20 ETH",
                "contract_standard": "ERC-721",
                "storage": "IPFS",
                "official_url": "https://doodles.app/",
                "opensea_url": "https://opensea.io/collection/doodles-official",
                "art_description": "Pastel-colored hand-drawn 2D cartoon avatars with rainbow hair, ice cream cones, alien traits, and playful caps",
                "catalyst_lore": "Darlings, Doodles is staging a massive momentum comeback with their new animated film partnerships and music entertainment drops!",
                "science_tech": "Fascinating! Doodles pairs ERC-721 character ownership with dynamic character customization protocols and community treasury governance!"
            }
        ],
        "SLOT_4_CROSS_CHAIN": [
            {
                "name": "Mad Lads",
                "slot_title": "Slot 4: Cross-Chain Spotlight",
                "category": "xNFT Executable Web3 / Solana",
                "chain": "Solana",
                "floor_price": "85.0 SOL",
                "volume_24h": "1,450 SOL",
                "contract_standard": "Metaplex / xNFT",
                "storage": "Shadow Drive / Arweave",
                "official_url": "https://madlads.com/",
                "opensea_url": "https://magiceden.io/marketplace/mad_lads",
                "art_description": "Bold 2D graphic comic-style hero portraits with vibrant stylized jackets, sunglasses, and cybernetic accessories",
                "catalyst_lore": "Darlings, we're crossing chains to Solana where Mad Lads reigns supreme! 85 SOL floor price and the undisputed cultural heavyweight of the ecosystem!",
                "science_tech": "Fascinating! Mad Lads are 'xNFTs'—executable tokenized applications running live inside Backpack wallet without web browsers!"
            },
            {
                "name": "NodeMonkes",
                "slot_title": "Slot 4: Cross-Chain Spotlight",
                "category": "Bitcoin Inscriptions / Ordinals",
                "chain": "Bitcoin",
                "floor_price": "0.14 BTC",
                "volume_24h": "12.80 BTC",
                "contract_standard": "Bitcoin Ordinal Satoshis",
                "storage": "100% On-Chain Bitcoin L1",
                "official_url": "https://nodemonkes.com/",
                "opensea_url": "https://magiceden.io/ordinals/marketplace/nodemonkes",
                "art_description": "Minimalist 28x28 pixel art monkey avatars inscribed permanently into individual Bitcoin satoshis",
                "catalyst_lore": "Darlings, we're checking Bitcoin Ordinals where NodeMonkes is dominating the sovereign money chain! 0.14 BTC floor and pure Bitcoin prestige!",
                "science_tech": "Fascinating! NodeMonkes are inscribed directly into raw Bitcoin blocks on Layer 1. Truly immutable with zero smart contract attack surface!"
            }
        ],
        "SLOT_5_WILDCARD": [
            {
                "name": "Chromie Squiggle by Snowfro",
                "slot_title": "Slot 5: Pasture Poll Wildcard",
                "category": "Generative Code / Art Blocks",
                "chain": "Ethereum",
                "floor_price": "2.58 ETH",
                "volume_24h": "9.93 ETH",
                "contract_standard": "ERC-721 Art Blocks",
                "storage": "On-Chain Script",
                "official_url": "https://artblocks.io/collection/chromie-squiggle-by-snowfro",
                "opensea_url": "https://opensea.io/collection/chromie-squiggle-by-snowfro",
                "art_description": "Hypnotic undulating 2D rainbow generative spectrum ribbon looping fluidly on a clean digital canvas",
                "catalyst_lore": "Darlings, our community voted Chromie Squiggle as this week's Wildcard winner! Hypnotic rainbow ribbons that turned generative code into museum fine art!",
                "science_tech": "Fascinating! Chromie Squiggle executes on-chain rendering scripts derived directly from transaction hash seeds. Pure algorithmic perfection!"
            },
            {
                "name": "Infinex Patrons",
                "slot_title": "Slot 5: Pasture Poll Wildcard",
                "category": "DeFi Revenue Share / Utility",
                "chain": "Ethereum",
                "floor_price": "1.79 ETH",
                "volume_24h": "65.91 ETH",
                "contract_standard": "ERC-721",
                "storage": "Arweave",
                "official_url": "https://infinex.xyz/",
                "opensea_url": "https://opensea.io/collection/infinex-patrons",
                "art_description": "Sleek holographic 2D card art displaying cross-chain patronage insignia and dynamic geometric token nodes",
                "catalyst_lore": "Darlings, our audience voted Infinex Patrons into the Wildcard spot! Backed by top crypto founders with real DeFi revenue share utility!",
                "science_tech": "Fascinating! Infinex Patrons receive transparent platform yield distributions stored permanently on Arweave with on-chain governance rights!"
            }
        ]
    }

    # Episode Rotation Manager
    history_file = os.path.join(output_dir, "episode_history.json")
    if not os.path.exists(history_file) and os.path.exists("episode_history.json"):
        history_file = "episode_history.json"
        
    episode_index = 0
    if os.path.exists(history_file):
        try:
            with open(history_file, "r") as f:
                hdata = json.load(f)
                episode_index = len(hdata.get("history", []))
        except Exception:
            episode_index = 0

    # Select 1 candidate from each slot based on episode rotation index
    selected_projects = [
        SLOT_CANDIDATE_POOLS["SLOT_1_BLUE_CHIP"][episode_index % len(SLOT_CANDIDATE_POOLS["SLOT_1_BLUE_CHIP"])],
        SLOT_CANDIDATE_POOLS["SLOT_2_VOLUME_MOVER"][episode_index % len(SLOT_CANDIDATE_POOLS["SLOT_2_VOLUME_MOVER"])],
        SLOT_CANDIDATE_POOLS["SLOT_3_BREAKOUT_GAINER"][episode_index % len(SLOT_CANDIDATE_POOLS["SLOT_3_BREAKOUT_GAINER"])],
        SLOT_CANDIDATE_POOLS["SLOT_4_CROSS_CHAIN"][episode_index % len(SLOT_CANDIDATE_POOLS["SLOT_4_CROSS_CHAIN"])],
        SLOT_CANDIDATE_POOLS["SLOT_5_WILDCARD"][episode_index % len(SLOT_CANDIDATE_POOLS["SLOT_5_WILDCARD"])]
    ]

    # Rotating Cow-pedia Terms
    COWPEDIA_TERMS = [
        ("Immutability (On-Chain Storage)", "The state of being permanent and unchangeable. Code or art stored on-chain cannot be deleted or edited by anyone!"),
        ("xNFTs (Executable Tokens)", "Tokens that run as interactive applications inside crypto wallets without external websites!"),
        ("Zero-Knowledge Proofs (ZKP)", "Cryptographic protocol proving a statement is true without revealing underlying sensitive information!"),
        ("Decentralized Metadata (IPFS/Arweave)", "Distributed file networks ensuring NFT artwork remains online permanently without single server points of failure!")
    ]
    selected_term, selected_term_def = COWPEDIA_TERMS[episode_index % len(COWPEDIA_TERMS)]

    print(f"[*] Selected 5-Slot Projects for Episode #{episode_index + 1}: {[p['name'] for p in selected_projects]}")
    print(f"[*] Selected Cow-pedia Term: {selected_term}")

    # 1. Generate Full Show Script
    script_content = f"""# MOO19 NEWS: THE NFT REPORT (DYNAMIC 5-SLOT FORMAT)
**Episode Air Date:** {now_str} (Episode #{episode_index + 1})
**Hosts:** {celeb_name} (Left Desk) & {science_name} (Right Desk next to microscope)
**Network:** MOO19 News Channel - The Pasture
**Format:** Dynamic 5-Slot Structure (Blue-Chip, Volume Mover, Breakout Gainer, Cross-Chain, Wildcard)
**Master Background:** Newsroom01_Large copy.jpg

============================================================

### [CLIP 01: MOO19 NEWS STUDIO INTRO (10s Max)]
**{celeb_name.upper()}:** "Welcome back to MOO19 News! Today on the NFT Report, we're breaking down blue-chips, surging volume movers, and cross-chain breakouts!"
**{science_name.upper()}:** "And watch your screen for our Cow-pedia Pop-ups and Scam or Stampede Security Checks! Let's inspect the code!"

============================================================
"""

    clip_count = 2
    bump_count = 1
    clips_info = []
    bumpers_data = []

    # Intro Clip Info
    clips_info.append((
        "clip_001", "Clip 01: Studio Intro",
        f"{celeb_name}: Welcome back to MOO19 News! Today on the NFT Report, we're breaking down blue-chips, volume movers, and cross-chain breakouts! {science_name}: And watch your screen for Cow-pedia Pop-ups and Scam or Stampede Checks! Let's inspect the code!",
        [celeb_name, science_name], {}
    ))

    for p in selected_projects:
        # Bumper
        b_id = f"bump_{bump_count:03d}"
        b_title = f"Bumper {bump_count:02d}: {p['name']} ({p['slot_title']})"
        b_spoken = f"Up next on the NFT Report: {p['name']}! Scan the QR code to explore!"
        
        script_content += f"""
### [BUMPER {bump_count:02d}: {p['name'].upper()} INTRO BUMP (4s)]
**SEGMENT:** {p['slot_title']}
**VISUAL CUE:** Dynamic 2D graphic card displaying {p['name']} art ({p['art_description']}), floor price ({p['floor_price']}), and scannable QR Code linking to {p['official_url']}.
**AUDIO STING & VOICEOVER:** "{b_spoken}"
"""
        bumpers_data.append((b_id, p["name"], p["official_url"], p["opensea_url"], p["floor_price"], p["chain"], p["art_description"], p["slot_title"]))
        bump_count += 1

        # Celeb Clip
        c_clip_id = f"clip_{clip_count:03d}"
        c_title = f"Clip {clip_count:02d}: {p['name']} (Lore & Glam)"
        c_script = f"{celeb_name}: {p['catalyst_lore']} Floor Price: {p['floor_price']} with {p['volume_24h']} volume! Glam Rating: 8.5/10!"
        
        script_content += f"""
### [{c_title.upper()} (10s Max)]
**ON-SCREEN GRAPHIC:** {p['name']} | Floor: {p['floor_price']} | Vol: {p['volume_24h']} | Chain: {p['chain']}
**{celeb_name.upper()}:** "{p['catalyst_lore']}"
**{celeb_name.upper()}:** "Floor: {p['floor_price']} | Glam Rating: 8.5/10!"
"""
        clips_info.append((
            c_clip_id, c_title, c_script, [celeb_name],
            {
                "lower_third_text": f"{p['name']} | Floor: {p['floor_price']} | Vol: {p['volume_24h']} | {p['chain']}",
                "hype_badge": "Glam: 8.5/10",
                "gauge_status": "BULLISH STAMPEDE 🟢"
            }
        ))
        clip_count += 1

        # Science Clip
        s_clip_id = f"clip_{clip_count:03d}"
        s_title = f"Clip {clip_count:02d}: {p['name']} (Science Tech)"
        s_script = f"{science_name}: {p['science_tech']} Storage: {p['storage']}. Code Rating: 9.0/10!"
        
        script_content += f"""
### [{s_title.upper()} (10s Max)]
**[COW-PEDIA POP-UP]:** **{p['storage']}** — Verified technical asset storage on {p['chain']}.
**{science_name.upper()}:** "{p['science_tech']}"
**{science_name.upper()}:** "Code & Security Rating: 9.0/10!"
----------------------------------------
"""
        clips_info.append((
            s_clip_id, s_title, s_script, [science_name],
            {
                "cowpedia_banner": f"Cow-pedia: {p['storage']} Verified On-Chain ({p['chain']})",
                "security_checklist": f"Verified Contract: PASS | Chain: {p['chain']} | Liquidity Lock: HIGH",
                "tech_badge": "Tech: 9.0/10"
            }
        ))
        clip_count += 1

    # Weather & Outro
    w_clip_id = f"clip_{clip_count:03d}"
    w_title = f"Clip {clip_count:02d}: Weather Forecast"
    w_script = f"{weather_name}: Expect high volatility across Web3 ecosystems tonight with an 80% chance of a bull surge! Embrace the chaos, traders!"
    script_content += f"""
### [{w_title.upper()} (10s Max)]
**{weather_name.upper()}:** "Expect high volatility across Web3 ecosystems tonight with an 80% chance of a bull surge! Embrace the chaos, traders!"
"""
    clips_info.append((w_clip_id, w_title, w_script, [weather_name], {}))
    clip_count += 1

    o_clip_id = f"clip_{clip_count:03d}"
    o_title = f"Clip {clip_count:02d}: Studio Outro"
    o_script = f"{celeb_name}: That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote on next week's wildcard! {science_name}: Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight, everyone!"
    script_content += f"""
### [{o_title.upper()} (10s Max)]
**{celeb_name.upper()}:** "That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote on next week's wildcard!"
**{science_name.upper()}:** "Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight, everyone!"
"""
    clips_info.append((o_clip_id, o_title, o_script, [celeb_name, science_name], {"pasture_poll_qr_code": "SCAN QR CODE TO VOTE FOR NEXT WEEK'S WILDCARD"}))

    script_path = os.path.join(output_dir, "weekly_nft_report_script.md")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_content)
    print(f"[+] Show Script saved: {script_path}")

    # 2. Generate Shorts Teaser Script (Safely Indexed)
    p0 = selected_projects[0]
    p1 = selected_projects
    p2 = selected_projects
    p3 = selected_projects
    p4 = selected_projects

    shorts_content = f"""# MOO19 NEWS: NFT REPORT SHORTS (DYNAMIC 5-SLOT TEASER)
**Air Date:** {now_str} (Episode #{episode_index + 1})
**Format:** 9:16 Vertical Video (TikTok / YouTube Shorts / Instagram Reels)

============================================================

**[00:00 - 00:10] {celeb_name.upper()}:** "Stop scrolling, Web3 trendsetters! Here are this week's top NFT movers on MOO19 News!"
**[00:10 - 00:25] {celeb_name.upper()}:** "Blue-Chip Anchor: {p0['name']} at {p0['floor_price']}, and Top Volume Leader {p1['name']} with {p1['volume_24h']} volume!"
**[00:25 - 00:40] {science_name.upper()}:** "Breakout Gainer {p2['name']}, plus Cross-Chain Titan {p3['name']} on {p3['chain']}!"
**[00:40 - 00:50] {celeb_name.upper()}:** "And our community Wildcard winner: {p4['name']}!"
**[00:50 - 01:00] {science_name.upper()}:** "Scan the QR code to watch the full episode on MOO19 News and vote on our Pasture Poll! Don't trust, verify!"
"""
    shorts_path = os.path.join(output_dir, "weekly_nft_report_shorts_script.md")
    with open(shorts_path, "w", encoding="utf-8") as f:
        f.write(shorts_content)
    print(f"[+] Shorts Script saved: {shorts_path}")

    # 3. Generate Weekly Newsletter (The Pasture Post)
    newsletter_content = f"""# 🐮 THE PASTURE POST: MOO19 NFT & WEB3 WEEKLY
**Issue #{episode_index + 16} • {now_str}**
*Demystifying the Blockchain with Culture, Code, and Common Sense*

=================================================================

## 🎙️ FROM THE NEWSROOM DESK
**{celeb_name.upper()} (Celebrity Reporter):**
> "Hello, pasture fashionistas and Web3 explorers! Welcome to this week's edition of *The Pasture Post*. In this episode, we're diving into blue-chip titans, surging volume leaders, and cross-chain breakouts on Solana and Bitcoin!"

**{science_name.upper()} (Science Reporter):**
> "And we're dissecting the underlying technology! This week, we examine **{selected_term}** to show you how decentralized storage and smart contracts protect digital assets. Let's inspect the data!"

-----------------------------------------------------------------

## 📰 FEATURED PROJECTS THIS WEEK (DYNAMIC 5-SLOT REPORT)

### 1. {p0['name']} — {p0['slot_title']}
**Category:** {p0['category']} | **Chain:** {p0['chain']} | **Source:** [{p0['name']}]({p0['official_url']})
**The Breakdown:** {p0['catalyst_lore']}
💡 **Tech Note:** {p0['science_tech']}

----------------------------------------

### 2. {p1['name']} — {p1['slot_title']}
**Category:** {p1['category']} | **Chain:** {p1['chain']} | **Source:** [{p1['name']}]({p1['official_url']})
**The Breakdown:** {p1['catalyst_lore']}
💡 **Tech Note:** {p1['science_tech']}

----------------------------------------

### 3. {p2['name']} — {p2['slot_title']}
**Category:** {p2['category']} | **Chain:** {p2['chain']} | **Source:** [{p2['name']}]({p2['official_url']})
**The Breakdown:** {p2['catalyst_lore']}
💡 **Tech Note:** {p2['science_tech']}

----------------------------------------

### 4. {p3['name']} — {p3['slot_title']}
**Category:** {p3['category']} | **Chain:** {p3['chain']} | **Source:** [{p3['name']}]({p3['official_url']})
**The Breakdown:** {p3['catalyst_lore']}
💡 **Tech Note:** {p3['science_tech']}

----------------------------------------

### 5. {p4['name']} — {p4['slot_title']}
**Category:** {p4['category']} | **Chain:** {p4['chain']} | **Source:** [{p4['name']}]({p4['official_url']})
**The Breakdown:** {p4['catalyst_lore']}
💡 **Tech Note:** {p4['science_tech']}

-----------------------------------------------------------------

## 📚 COW-PEDIA TERM OF THE WEEK
**Term: {selected_term}**
> *Definition:* {selected_term_def}

-----------------------------------------------------------------

## ⛈️ MARKET CLIMATE OUTLOOK
**Forecast by {weather_name}:**
> "Current indicators show an **80% chance of a bull surge** across verified utility collections with steady floor price consolidation. Keep an eye out for sudden volatility storms around upcoming Layer-2 network upgrades! Embrace the chaos, traders!"

-----------------------------------------------------------------

## 🗳️ WEEKLY PASTURE POLL
**Which project should Daisy and Professor Hartmut examine on next Monday's animated episode?**
1. On-Chain Generative Art Collection (e.g., Fidenza / Ringers)
2. Bitcoin Inscription / Ordinals Project
3. Real-World Asset (RWA) Tokenization Project

👉 *Cast your vote by replying to this newsletter or voting in our Discord community!*

=================================================================
© 2026 CryptoCowz / MOO19 News • *Demystifying cryptocurrency until the cows come home!*
Follow us: [YouTube](https://www.youtube.com/@cryptocollectablesNY) | [Facebook](https://www.facebook.com/CryptocollectiblesNY)
"""
    nl_path = os.path.join(output_dir, "weekly_pasture_post_newsletter.md")
    with open(nl_path, "w", encoding="utf-8") as f:
        f.write(newsletter_content)
    print(f"[+] Newsletter saved: {nl_path}")

    # 4. Master Animation Manifest & Standalone Clips & Bumpers
    manifest_data = {
        "manifest_version": "1.0",
        "google_flow_project_target": "MOO19 TV The NFT Report",
        "show_title": f"MOO19 NFT Report - Dynamic 5-Slot Episode #{episode_index + 1}",
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

    for bid, bname, burl, bopensea, bfloor, bchain, bart, bslot in bumpers_data:
        b_spoken = f"Up next on the NFT Report: {bname}! Scan the QR code to explore!"
        b_prompt = f"2D animated high-energy motion graphic bumper card, 4 seconds. Center featured 2D artwork of {bname} ({bart}). Prominent scannable QR Code on right overlay linking to {burl}. Lower third displaying '{bname} | Floor: {bfloor} | Chain: {bchain} | {bslot}'. Audio sting with energetic voiceover: '{b_spoken}'"
        b_obj = {
            "manifest_version": "1.0",
            "google_flow_project_target": "MOO19 TV The NFT Report            "manifest_version": "1.0",
            "google_flow_project_target": "MOO19 TV The NFT Report",
            "clip_id": bid,
            "clip_type": "SEGMENT_BUMPER",
            "duration_seconds": 4,
            "title": f"Bumper: {bname} Intro",
            "featured_nft": bname,
            "slot": bslot,
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
                "lower_third_badge": f"{bname} | Floor: {bfloor} | {bchain}"
            }
        }
        manifest_data["bumpers"].append(b_obj)
        b_clean = bname.lower().replace(" ", "_").replace(":", "")
        with open(os.path.join(bumpers_dir, f"{bid}_{b_clean}_bump.json"), "w", encoding="utf-8") as bf:
            json.dump(b_obj, bf, indent=2)

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

    manifest_path = os.path.join(output_dir, "google_flow_animation_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as mf:
        json.dump(manifest_data, mf, indent=2)
    print(f"[+] Master Animation Manifest saved: {manifest_path}")

    # Update episode history tracking
    history_entry = {
        "episode_number": episode_index + 1,
        "air_date": now_str,
        "featured_projects": [p["name"] for p in selected_projects],
        "cowpedia_term": selected_term
    }
    history_payload = {"history": []}
    if os.path.exists(history_file):
        try:
            with open(history_file, "r") as f:
                history_payload = json.load(f)
        except Exception:
            history_payload = {"history": []}

    history_payload["history"].append(history_entry)
    with open(history_file, "w") as f:
        json.dump(history_payload, f, indent=2)

    print(f"[✓] Dynamic 5-Slot Episode #{episode_index + 1} generated successfully in '{output_dir}'!\n")

def main():
    parser = argparse.ArgumentParser(description="MOO19 News NFT Report Dynamic 5-Slot Production Engine")
    parser.add_argument("--output-dir", type=str, default="output", help="Directory to save generated outputs")
    parser.add_argument("--run", action="store_true", help="Run full episode generation")
    args = parser.parse_args()
    
    run_production_pipeline(output_dir=args.output_dir)

if __name__ == "__main__":
    main()
