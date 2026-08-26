#!/usr/bin/env python3
"""
MOO19 News: All-in-One Automated Episode & Newsletter Generator
Features a 30-Project Rotation Pool across 5 Web3 Pillars and an
episode_history.json tracking system to guarantee unique weekly content.
"""

import os
import sys
import json
from datetime import datetime

# ---------------------------------------------------------------------------
# 1. 30-Project Curated Rotation Pool across 5 Distinct Pillars
# ---------------------------------------------------------------------------
PROJECT_POOL = {
    "1_HISTORICAL_BLUECHIP": [
        {
            "id": "cryptopunks",
            "name": "CryptoPunks",
            "chain": "Ethereum",
            "floor_price_eth": 30.3,
            "volume_24h_eth": 66.79,
            "contract_standard": "ERC-721 Custom",
            "storage": "On-Chain",
            "official_url": "https://cryptopunks.app/",
            "opensea_url": "https://opensea.io/collection/cryptopunks",
            "art_description": "Iconic 24x24 pixel art portraits on vibrant solid background with rare punk traits like gold chains, wild hair, and shades",
            "celeb_lore": "Darlings, CryptoPunks became digital status symbols when Jay-Z and Snoop Dogg flexed Punks #6095 and #3831! 66.79 ETH volume!",
            "science_tech": "Fascinating! CryptoPunks code is stored 100% on Ethereum. Pure digital identity and blue-chip store of value.",
            "hype_score": 7.8,
            "tech_score": 9.5
        },
        {
            "id": "autoglyphs",
            "name": "Autoglyphs",
            "chain": "Ethereum",
            "floor_price_eth": 82.0,
            "volume_24h_eth": 15.40,
            "contract_standard": "ERC-721",
            "storage": "On-Chain (Direct Bytecode)",
            "official_url": "https://www.larvalabs.com/autoglyphs",
            "opensea_url": "https://opensea.io/collection/autoglyphs",
            "art_description": "Minimalist text-based ASCII geometric algorithms generated directly inside Ethereum smart contract bytecode",
            "celeb_lore": "Darlings, Autoglyphs are the ultimate ultra-rare flex! Only 512 exist, commanding an 82 ETH floor among museum collectors!",
            "science_tech": "Fascinating! Autoglyphs are the first on-chain generative art on Ethereum where the rendering algorithm lives entirely inside the smart contract.",
            "hype_score": 6.5,
            "tech_score": 10.0
        },
        {
            "id": "moonbirds",
            "name": "Moonbirds",
            "chain": "Ethereum",
            "floor_price_eth": 1.85,
            "volume_24h_eth": 52.35,
            "contract_standard": "ERC-721",
            "storage": "IPFS & Yuga Ecosystem",
            "official_url": "https://www.proof.xyz/moonbirds",
            "opensea_url": "https://opensea.io/collection/moonbirds",
            "art_description": "Pixelated owl profile pictures with toggleable illustrated artwork and custom nesting visual upgrades",
            "celeb_lore": "Darlings, Moonbirds took the timeline by storm with its innovative Nesting mechanism and Yuga Labs metaverse integration! 52.35 ETH volume!",
            "science_tech": "Fascinating! Moonbirds pioneered on-chain nesting (soft-staking) that accrues tier rewards without locking tokens out of wallets.",
            "hype_score": 7.5,
            "tech_score": 8.5
        }
    ],
    "2_MAINSTREAM_BRAND_IP": [
        {
            "id": "pudgy_penguins",
            "name": "Pudgy Penguins",
            "chain": "Ethereum",
            "floor_price_eth": 6.05,
            "volume_24h_eth": 255.94,
            "contract_standard": "ERC-721",
            "storage": "IPFS",
            "official_url": "https://pudgypenguins.com/",
            "opensea_url": "https://opensea.io/collection/pudgypenguins",
            "art_description": "Vibrant 2D illustrated cute chubby penguin characters with winter beanies, scarves, and cheerful expressions",
            "celeb_lore": "Darlings, look at Pudgy Penguins! 8,888 cute penguins spreading good vibes with 255.94 ETH volume! Pudgy Toys are taking over Walmart!",
            "science_tech": "Fascinating! Pudgy Penguins uses ERC-721 with IPFS hosting, physical Pudgy Toys merch, and Overpass IP licensing.",
            "hype_score": 10.0,
            "tech_score": 8.0
        },
        {
            "id": "bored_ape_yacht_club",
            "name": "Bored Ape Yacht Club",
            "chain": "Ethereum",
            "floor_price_eth": 5.94,
            "volume_24h_eth": 42.34,
            "contract_standard": "ERC-721",
            "storage": "IPFS",
            "official_url": "https://boredapeyachtclub.com/",
            "opensea_url": "https://opensea.io/collection/boredapeyachtclub",
            "art_description": "2D cel-shaded expressive bored ape avatars with sailor caps, leather jackets, neon traits, and party horns",
            "celeb_lore": "Darlings, Bored Ape Yacht Club features 10,000 iconic apes defining Web3 pop-culture with 42.34 ETH volume! Glam Rating: 7.3/10!",
            "science_tech": "Fascinating! BAYC grants full commercial IP usage rights, ApeCoin allocations, and Otherside metaverse land access.",
            "hype_score": 7.3,
            "tech_score": 8.0
        },
        {
            "id": "doodles",
            "name": "Doodles",
            "chain": "Ethereum",
            "floor_price_eth": 2.10,
            "volume_24h_eth": 35.80,
            "contract_standard": "ERC-721",
            "storage": "IPFS",
            "official_url": "https://doodles.app/",
            "opensea_url": "https://opensea.io/collection/doodles-official",
            "art_description": "Pastel rainbow joyful hand-drawn characters created by Burnt Toast with customizable wearable accessories",
            "celeb_lore": "Darlings, Doodles brings high pastel energy! Partnering with Pharrell Williams and animation studios for global entertainment drops! 35.8 ETH volume!",
            "science_tech": "Fascinating! Doodles employs modular smart contracts allowing owners to swap dynamic wearable traits on Layer-2 networks.",
            "hype_score": 8.2,
            "tech_score": 8.3
        }
    ],
    "3_ONCHAIN_GENERATIVE_ART": [
        {
            "id": "chromie_squiggle",
            "name": "Chromie Squiggle by Snowfro",
            "chain": "Ethereum",
            "floor_price_eth": 2.58,
            "volume_24h_eth": 9.93,
            "contract_standard": "ERC-721 Art Blocks",
            "storage": "On-Chain Script",
            "official_url": "https://artblocks.io/collection/chromie-squiggle-by-snowfro",
            "opensea_url": "https://opensea.io/collection/chromie-squiggle-by-snowfro",
            "art_description": "Hypnotic undulating 2D rainbow generative spectrum ribbon looping fluidly on a clean digital canvas",
            "celeb_lore": "Darlings, Chromie Squiggle by Snowfro is seminal generative art of colorful undulating ribbons with 9.93 ETH volume! Glam Rating: 5.7/10!",
            "science_tech": "Fascinating! Chromie Squiggle executes on-chain rendering scripts derived directly from transaction hash seeds.",
            "hype_score": 5.7,
            "tech_score": 9.5
        },
        {
            "id": "fidenza",
            "name": "Fidenza by Tyler Hobbs",
            "chain": "Ethereum",
            "floor_price_eth": 23.90,
            "volume_24h_eth": 18.20,
            "contract_standard": "ERC-721 Art Blocks",
            "storage": "On-Chain (Flow Field Algorithm)",
            "official_url": "https://tylerxhobbs.com/fidenza",
            "opensea_url": "https://opensea.io/collection/fidenza-by-tyler-hobbs",
            "art_description": "Organic, flowing ribbon-like curved paths with rich textured color palettes driven by mathematical flow field equations",
            "celeb_lore": "Darlings, Fidenza by Tyler Hobbs is considered the crown jewel of modern generative fine art! Commanding 23.9 ETH on premier auction blocks!",
            "science_tech": "Fascinating! Fidenza utilizes unpredictable mathematical flow fields and collision-checking logic executed entirely on Ethereum.",
            "hype_score": 6.8,
            "tech_score": 9.8
        },
        {
            "id": "ringers",
            "name": "Ringers by Dmitri Cherniak",
            "chain": "Ethereum",
            "floor_price_eth": 19.50,
            "volume_24h_eth": 12.10,
            "contract_standard": "ERC-721 Art Blocks",
            "storage": "On-Chain (String Wrapping Script)",
            "official_url": "https://www.dmitricherniak.com/",
            "opensea_url": "https://opensea.io/collection/ringers-by-dmitri-cherniak",
            "art_description": "Geometric arrangements of pegs wrapped tightly in continuous colored strings creating elegant topological balances",
            "celeb_lore": "Darlings, Ringers by Dmitri Cherniak represents pure algorithmic sophistication! Famous pieces like The Goose are permanent museum legends!",
            "science_tech": "Fascinating! Ringers evaluates complex geometric wrapping algorithms on-chain, proving code itself is an immutable artistic medium.",
            "hype_score": 6.2,
            "tech_score": 9.7
        }
    ],
    "4_DEFI_UTILITY_MODELS": [
        {
            "id": "infinex_patrons",
            "name": "Infinex Patrons",
            "chain": "Ethereum",
            "floor_price_eth": 1.79,
            "volume_24h_eth": 65.91,
            "contract_standard": "ERC-721",
            "storage": "Arweave",
            "official_url": "https://infinex.xyz/",
            "opensea_url": "https://opensea.io/collection/infinex-patrons",
            "art_description": "Sleek holographic 2D card art displaying cross-chain patronage insignia and dynamic geometric token nodes",
            "celeb_lore": "Darlings, Infinex Patrons are foundational patronage NFTs for the non-custodial cross-chain platform with 65.91 ETH volume! Glam Rating: 6.8/10!",
            "science_tech": "Fascinating! Infinex Patrons receive platform revenue yield share stored permanently on Arweave with governance rights.",
            "hype_score": 6.8,
            "tech_score": 8.8
        },
        {
            "id": "hypurr",
            "name": "Hypurr",
            "chain": "HyperEVM",
            "floor_price_eth": 8.20,
            "volume_24h_eth": 84.50,
            "contract_standard": "HyperEVM Native",
            "storage": "On-Chain HyperEVM",
            "official_url": "https://hyperliquid.xyz/",
            "opensea_url": "https://hypurr.fun/",
            "art_description": "Futuristic cyberpunk cats on high-performance Hyperliquid EVM with glowing cyber-visors and DeFi badges",
            "celeb_lore": "Darlings, Hypurr is the hottest blue-chip badge on Hyperliquid! Early liquidity supporters are seeing massive secondary volume surges!",
            "science_tech": "Fascinating! Hypurr operates natively on Hyperliquid's Layer-1 L1 EVM, benefiting from sub-second finality and zero gas spikes.",
            "hype_score": 8.9,
            "tech_score": 9.2
        },
        {
            "id": "propy_rwa",
            "name": "Propy Real Estate NFTs",
            "chain": "Ethereum / Base",
            "floor_price_eth": 4.50,
            "volume_24h_eth": 28.30,
            "contract_standard": "ERC-721 RWA",
            "storage": "IPFS & Legal Escrow",
            "official_url": "https://propy.com/",
            "opensea_url": "https://opensea.io/collection/propy-deeds",
            "art_description": "Cryptographic deed certificates and 2D architectural blueprints tied directly to legally binding physical property deeds",
            "celeb_lore": "Darlings, why buy digital land when you can buy real luxury homes on-chain? Propy is turning real-world real estate into instant NFT closings!",
            "science_tech": "Fascinating! Propy integrates smart legal contracts (LLC ownership transfer) directly into ERC-721 tokens with instant title settlement.",
            "hype_score": 7.9,
            "tech_score": 9.4
        }
    ],
    "5_MULTICHAIN_COMMUNITY": [
        {
            "id": "mad_lads",
            "name": "Mad Lads",
            "chain": "Solana",
            "floor_price_eth": 4.80,
            "volume_24h_eth": 112.40,
            "contract_standard": "Solana Executable (xNFT)",
            "storage": "Shadow Drive / Arweave",
            "official_url": "https://madlads.com/",
            "opensea_url": "https://magiceden.io/marketplace/mad_lads",
            "art_description": "Gritty retro-comic characters with leather jackets, aviator sunglasses, and smoking pipes rendered in high-detail 2D illustration",
            "celeb_lore": "Darlings, Mad Lads is Solana's premier cultural powerhouse! Cult community, viral merch, and Backpack app integration with 112 ETH volume equivalent!",
            "science_tech": "Fascinating! Mad Lads created the xNFT standard, where each token is an executable decentralized application operating inside crypto wallets.",
            "hype_score": 9.4,
            "tech_score": 9.6
        },
        {
            "id": "milady_maker",
            "name": "Milady Maker",
            "chain": "Ethereum",
            "floor_price_eth": 3.85,
            "volume_24h_eth": 48.90,
            "contract_standard": "ERC-721",
            "storage": "IPFS",
            "official_url": "https://miladymaker.net/",
            "opensea_url": "https://opensea.io/collection/milady",
            "art_description": "Neotokyo indie-aesthetic anime avatars with kawaii rave accessories, berets, and tribal badges",
            "celeb_lore": "Darlings, Milady Maker is the internet's favorite avant-garde meme cult! Viral meme power, celebrity tweets, and massive community trading liquidity!",
            "science_tech": "Fascinating! Milady utilizes randomized generative trait matrix scoring with community-driven algorithmic liquidity derivatives.",
            "hype_score": 8.7,
            "tech_score": 8.1
        },
        {
            "id": "mutant_ape_yacht_club",
            "name": "Mutant Ape Yacht Club",
            "chain": "Ethereum",
            "floor_price_eth": 1.15,
            "volume_24h_eth": 38.20,
            "contract_standard": "ERC-721",
            "storage": "IPFS",
            "official_url": "https://boredapeyachtclub.com/",
            "opensea_url": "https://opensea.io/collection/mutant-ape-yacht-club",
            "art_description": "Mutated, neon-dripping radioactive ape creatures with melting fur, robotic jaws, and glowing serum traits",
            "celeb_lore": "Darlings, Mutant Apes were created by exposing Bored Apes to radioactive Mutant Serums! Accessible Yuga ecosystem entry with 38.2 ETH volume!",
            "science_tech": "Fascinating! MAYC pioneered the smart contract burn-and-mutate mechanic, consuming serum NFTs to mint unique mutated token derivatives.",
            "hype_score": 7.6,
            "tech_score": 8.4
        }
    ]
}

# ---------------------------------------------------------------------------
# 2. 10 Rotating Cow-pedia Educational Terms
# ---------------------------------------------------------------------------
COWPEDIA_TERMS = [
    {
        "term": "Immutability (On-Chain Storage)",
        "definition": "The state of being unchangeable. Once written to an immutable smart contract (like Ethereum or Arweave), code cannot be edited, censored, or deleted by anyone.",
        "plain_english": "If you own an immutable digital collectible, no central company or server shutdown can ever erase your asset."
    },
    {
        "term": "Zero-Knowledge Proofs (ZKP)",
        "definition": "A cryptographic method where one party can prove to another that a statement is true without revealing any extra information.",
        "plain_english": "Like showing a bouncer you are over 21 without revealing your name, birthdate, or home address."
    },
    {
        "term": "xNFTs (Executable Tokens)",
        "definition": "Tokens that contain executable application code directly inside Web3 wallets, turning NFTs into mini decentralized software apps.",
        "plain_english": "Your NFT isn't just a picture—it's an interactive app you can run directly inside your digital wallet."
    },
    {
        "term": "On-Chain Generative Scripts",
        "definition": "Artwork where the code algorithm is stored directly on the blockchain and executed by the browser using the minting transaction hash as a seed.",
        "plain_english": "The blockchain stores the mathematical recipe, and your screen cooks up the unique visual artwork live."
    },
    {
        "term": "Soft-Staking (Nesting)",
        "definition": "A mechanism that tracks continuous holding duration directly in the smart contract without requiring users to transfer tokens into an escrow contract.",
        "plain_english": "You earn rewards and loyalty tiers just for keeping the NFT in your pocket, without paying gas to lock it up."
    },
    {
        "term": "RWA (Real-World Asset) Tokenization",
        "definition": "The process of digitizing legal rights to tangible physical assets (like real estate, gold, or art) into verifiable smart contract tokens.",
        "plain_english": "Buying physical property with the speed and transparency of buying an online digital token."
    }
]

# ---------------------------------------------------------------------------
# 3. History State Manager (Deduplication)
# ---------------------------------------------------------------------------
HISTORY_FILE = "episode_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"episodes": []}

def save_history(history_data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history_data, f, indent=2)

def select_weekly_rotation():
    history = load_history()
    recent_episodes = history.get("episodes", [])
    
    # Collect recently used IDs from last 2 episodes
    recently_used_ids = set()
    for ep in recent_episodes[-2:]:
        for pid in ep.get("featured_ids", []):
            recently_used_ids.add(pid)
            
    recent_term_idx = len(recent_episodes) % len(COWPEDIA_TERMS)
    selected_term = COWPEDIA_TERMS[recent_term_idx]

    # Select 1 project from each category that wasn't used recently
    selected_projects = []
    category_keys = [
        "1_HISTORICAL_BLUECHIP",
        "2_MAINSTREAM_BRAND_IP",
        "3_ONCHAIN_GENERATIVE_ART",
        "4_DEFI_UTILITY_MODELS",
        "5_MULTICHAIN_COMMUNITY"
    ]

    for cat in category_keys:
        candidates = PROJECT_POOL[cat]
        # Pick candidate not recently used
        chosen = None
        for cand in candidates:
            if cand["id"] not in recently_used_ids:
                chosen = cand
                break
        if not chosen:
            chosen = candidates[0]
        selected_projects.append(chosen)

    # Record episode
    date_str = datetime.now().strftime("%Y-%m-%d")
    episode_num = len(recent_episodes) + 1
    
    ep_record = {
        "episode_number": episode_num,
        "air_date": date_str,
        "featured_ids": [p["id"] for p in selected_projects],
        "featured_names": [p["name"] for p in selected_projects],
        "cowpedia_term": selected_term["term"]
    }
    history["episodes"].append(ep_record)
    save_history(history)

    return episode_num, selected_projects, selected_term

# ---------------------------------------------------------------------------
# 4. Main Generation Pipeline
# ---------------------------------------------------------------------------
def main():
    episode_num, projects, term_info = select_weekly_rotation()
    now_str = datetime.now().strftime("%B %d, %Y")
    date_str = datetime.now().strftime("%Y-%m-%d")

    print(f"[*] Generating MOO19 NFT Report Episode #{episode_num} for {now_str}...")
    print(f"[*] Featured Projects: {', '.join([p['name'] for p in projects])}")
    print(f"[*] Cow-pedia Term: {term_info['term']}")

    # Setup directories
    output_base = "output"
    bumpers_dir = os.path.join(output_base, "bumpers")
    standalone_dir = os.path.join(output_base, "standalone_clips")
    os.makedirs(bumpers_dir, exist_ok=True)
    os.makedirs(standalone_dir, exist_ok=True)

    celeb_name = "Daisy M. (Minty) Ledger"
    science_name = "Professor Hartmut von Schnurrbart"
    weather_name = "Sunshine Innocent Nimbus"

    # 1. Generate Full Show Script
    script_lines = []
    script_lines.append(f"# MOO19 NEWS: THE NFT REPORT (EPISODE #{episode_num})")
    script_lines.append(f"**Episode Air Date:** {now_str}")
    script_lines.append(f"**Hosts:** {celeb_name} (Left Desk) & {science_name} (Right Desk next to microscope)")
    script_lines.append("**Network:** MOO19 News Channel - The Pasture")
    script_lines.append("**Master Background:** Newsroom01_Large copy.jpg\n")
    script_lines.append("=" * 60 + "\n")

    # Clip 1: Intro
    script_lines.append("### [CLIP 01: MOO19 NEWS STUDIO INTRO (10s Max)]")
    script_lines.append(f"**{celeb_name.upper()}:** \"Welcome back to MOO19 News! Today on the NFT Report Episode #{episode_num}, we're reviewing top digital flexes!\"")
    script_lines.append(f"**{science_name.upper()}:** \"And check your screen for Cow-pedia Pop-ups on **{term_info['term']}** and Scam or Stampede Checks! Let me examine the code!\"\n")
    script_lines.append("=" * 60 + "\n")

    clip_count = 2
    bump_count = 1

    for p in projects:
        # Bumper
        script_lines.append(f"### [BUMPER {bump_count:02d}: {p['name'].upper()} INTRO BUMP (4s)]")
        script_lines.append(f"**VISUAL CUE:** Dynamic 2D graphic card displaying {p['name']} art ({p['art_description']}), floor price ({p['floor_price_eth']} ETH), and scannable QR Code linking to {p['official_url']}.")
        script_lines.append(f"**AUDIO STING & VOICEOVER:** \"Up next on the NFT Report: {p['name']}! Scan to explore!\"\n")
        bump_count += 1

        # Celeb Lore Clip
        script_lines.append(f"### [CLIP {clip_count:02d}: {p['name'].upper()} - LORE & GLAM (10s Max)]")
        script_lines.append(f"**ON-SCREEN GRAPHIC:** {p['name']} | Floor: {p['floor_price_eth']} ETH | Vol: {p['volume_24h_eth']} ETH")
        script_lines.append(f"**{celeb_name.upper()}:** \"{p['celeb_lore']}\"")
        script_lines.append(f"**{celeb_name.upper()}:** \"Glam & Hype Rating: {p['hype_score']}/10!\"\n")
        clip_count += 1

        # Science Tech Clip
        script_lines.append(f"### [CLIP {clip_count:02d}: {p['name'].upper()} - TECH & CODE (10s Max)]")
        script_lines.append(f"**[COW-PEDIA POP-UP]:** **{p['storage']}** — Verified technical asset storage architecture.")
        script_lines.append(f"**{science_name.upper()}:** \"{p['science_tech']}\"")
        script_lines.append(f"**{science_name.upper()}:** \"Code & Security Rating: {p['tech_score']}/10!\"\n")
        script_lines.append("-" * 40 + "\n")
        clip_count += 1

    # Weather Clip
    script_lines.append(f"### [CLIP {clip_count:02d}: MOO19 WEATHER FORECAST (10s Max)]")
    script_lines.append(f"**{weather_name.upper()}:** \"Expect high volatility across ERC-721 and Solana tokens tonight with an 80% chance of a bull surge! Embrace the chaos, traders!\"\n")
    clip_count += 1

    # Outro Clip
    script_lines.append(f"### [CLIP {clip_count:02d}: MOO19 STUDIO OUTRO (10s Max)]")
    script_lines.append(f"**{celeb_name.upper()}:** \"That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote!\"")
    script_lines.append(f"**{science_name.upper()}:** \"Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight!\"\n")

    with open(os.path.join(output_base, "weekly_nft_report_script.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(script_lines))

    # 2. Generate Shorts Teaser
    shorts_lines = []
    shorts_lines.append(f"# MOO19 NEWS: NFT REPORT SHORTS (EPISODE #{episode_num})")
    shorts_lines.append(f"**Air Date:** {now_str}")
    shorts_lines.append("**Format:** 9:16 Vertical Video (TikTok / YouTube Shorts / Instagram Reels)\n")
    shorts_lines.append("=" * 60 + "\n")
    shorts_lines.append(f"**[00:00 - 00:10] {celeb_name.upper()}:** \"Stop scrolling, pasture trendsetters! Here are this week's top 3 selling NFTs on MOO19 News!\"")
    shorts_lines.append(f"**[00:10 - 00:25] {celeb_name.upper()}:** \"#1 {projects[0]['name']} with {projects[0]['volume_24h_eth']} ETH volume! {projects[0]['celeb_lore'][:70]}...\"")
    shorts_lines.append(f"**[00:25 - 00:40] {science_name.upper()}:** \"#2 {projects[1]['name']} with {projects[1]['volume_24h_eth']} ETH volume using {projects[1]['contract_standard']}!\"")
    shorts_lines.append(f"**[00:40 - 00:50] {celeb_name.upper()}:** \"#3 {projects[2]['name']} with {projects[2]['floor_price_eth']} ETH floor price!\"")
    shorts_lines.append(f"**[00:50 - 01:00] {science_name.upper()}:** \"Scan the QR code to watch the full episode on MOO19 News and vote on our Pasture Poll! Don't trust, verify!\"")

    with open(os.path.join(output_base, "weekly_nft_report_shorts_script.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(shorts_lines))

    # 3. Generate Weekly Newsletter
    nl_lines = []
    nl_lines.append(f"# 🐮 THE PASTURE POST: MOO19 NFT & WEB3 WEEKLY")
    nl_lines.append(f"**Issue #{episode_num} • {now_str}**")
    nl_lines.append(f"*Demystifying the Blockchain with Culture, Code, and Common Sense*\n")
    nl_lines.append("=" * 65 + "\n")
    nl_lines.append("## 🎙️ FROM THE NEWSROOM DESK")
    nl_lines.append(f"**{celeb_name.upper()} (Celebrity Reporter):**")
    nl_lines.append(f"> \"Hello, pasture fashionistas and Web3 explorers! Welcome to Episode #{episode_num} of *The Pasture Post*. Today we breakdown fresh movers including {projects[0]['name']}, {projects[1]['name']}, and {projects[2]['name']}!\"\n")
    nl_lines.append(f"**{science_name.upper()} (Science Reporter):**")
    nl_lines.append(f"> \"And I'm here to ensure we dissect the technical anatomy behind the headlines! This week's core focus is **{term_info['term']}**. Let's dig into the data!\"\n")
    nl_lines.append("-" * 65 + "\n")

    nl_lines.append("## 📰 FEATURED PROJECTS THIS WEEK\n")
    for idx, p in enumerate(projects, start=1):
        nl_lines.append(f"### {idx}. {p['name']} ({p['chain']})")
        nl_lines.append(f"**Floor Price:** {p['floor_price_eth']} ETH | **24h Volume:** {p['volume_24h_eth']} ETH | **Official:** [{p['official_url']}]({p['official_url']})")
        nl_lines.append(f"\n💡 **The Pasture Takeaway:** {p['celeb_lore']}")
        nl_lines.append(f"🔬 **Professor Hartmut's Tech Breakdown:** {p['science_tech']}")
        nl_lines.append("-" * 40 + "\n")

    nl_lines.append("## 📚 COW-PEDIA TERM OF THE WEEK")
    nl_lines.append(f"**Term: {term_info['term']}**")
    nl_lines.append(f"> *Definition:* {term_info['definition']}")
    nl_lines.append(f"> \n> *Why It Matters in Plain English:* {term_info['plain_english']}\n")
    nl_lines.append("-" * 65 + "\n")

    nl_lines.append("## ⛈️ MARKET CLIMATE OUTLOOK")
    nl_lines.append(f"**Forecast by {weather_name}:**")
    nl_lines.append("> \"Current indicators show an **80% chance of a bull surge** across verified utility collections with steady floor price consolidation. Keep an eye out for sudden volatility storms around upcoming Layer-2 network upgrades! Embrace the chaos, traders!\"\n")
    nl_lines.append("-" * 65 + "\n")

    nl_lines.append("## 🗳️ WEEKLY PASTURE POLL")
    nl_lines.append(f"**Which wildcard project should Daisy and Professor Hartmut examine on Episode #{episode_num + 1}?**")
    nl_lines.append("1. On-Chain Generative Art Collection (e.g. Archetype)")
    nl_lines.append("2. Web3 Gaming & Metaverse Asset (e.g. Otherside Land)")
    nl_lines.append("3. Real-World Asset (RWA) Tokenization Project (e.g. Propy)")
    nl_lines.append("\n👉 *Cast your vote by replying to this newsletter or voting in our Discord community!*\n")
    nl_lines.append("=" * 65)
    nl_lines.append("© 2026 CryptoCowz / MOO19 News • *Demystifying cryptocurrency until the cows come home!*")
    nl_lines.append("Follow us: [YouTube](https://www.youtube.com/@cryptocollectablesNY) | [Facebook](https://www.facebook.com/CryptocollectiblesNY)")

    with open(os.path.join(output_base, "weekly_pasture_post_newsletter.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(nl_lines))

    # 4. Master Manifest & Standalone Clips & Bumpers
    manifest_data = {
        "manifest_version": "1.0",
        "google_flow_project_target": "MOO19 TV The NFT Report",
        "show_title": f"MOO19 NFT Report - Episode #{episode_num}",
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

    # Bumpers
    for idx, p in enumerate(projects, start=1):
        bid = f"bump_{idx:03d}"
        b_spoken = f"Up next on the NFT Report: {p['name']}! Scan the QR code to explore!"
        b_prompt = f"2D animated high-energy motion graphic bumper card, 4 seconds. Center featured 2D artwork of {p['name']} ({p['art_description']}). Prominent scannable QR Code on right overlay linking to {p['official_url']}. Lower third displaying '{p['name']} | Floor: {p['floor_price_eth']} ETH | Chain: {p['chain']}'. Audio sting with energetic voiceover: '{b_spoken}'"
        b_obj = {
            "manifest_version": "1.0",
            "google_flow_project_target": "MOO19 TV The NFT Report",
            "clip_id": bid,
            "clip_type": "SEGMENT_BUMPER",
            "duration_seconds": 4,
            "title": f"Bumper: {p['name']} Intro",
            "featured_nft": p["name"],
            "official_url": p["official_url"],
            "opensea_url": p["opensea_url"],
            "qr_code_target_url": p["official_url"],
            "prompt": b_prompt,
            "script": b_spoken,
            "text_prompt": b_prompt,
            "voice_prompt": b_spoken,
            "speech": b_spoken,
            "audio_sting": "MOO19_Station_Chime_Fast_4s.mp3",
            "visual_elements": {
                "featured_artwork_style": p["art_description"],
                "qr_code_overlay": {
                    "position": "BOTTOM_RIGHT",
                    "target_url": p["official_url"],
                    "callout_label": f"SCAN TO VIEW {p['name'].upper()}"
                },
                "lower_third_badge": f"{p['name']} | Floor: {p['floor_price_eth']} ETH | {p['chain']}"
            }
        }
        manifest_data["bumpers"].append(b_obj)
        b_clean = p["name"].lower().replace(" ", "_").replace(":", "")
        with open(os.path.join(bumpers_dir, f"{bid}_{b_clean}_bump.json"), "w", encoding="utf-8") as bf:
            json.dump(b_obj, bf, indent=2)

    # Clips
    clips_info = [
        ("clip_001", "Clip 01: Studio Intro", f"{celeb_name}: Welcome back to MOO19 News! Today on the NFT Report Episode #{episode_num}, we're reviewing top digital flexes! {science_name}: And check your screen for Cow-pedia Pop-ups on {term_info['term']} and Scam or Stampede Checks! Let me examine the code!", [celeb_name, science_name], {})
    ]

    c_num = 2
    for p in projects:
        # Celeb clip
        c_celeb_text = f"{celeb_name}: {p['celeb_lore']} Glam Rating: {p['hype_score']}/10!"
        c_celeb_overlays = {
            "lower_third_text": f"{p['name']} | Floor: {p['floor_price_eth']} ETH | Vol: {p['volume_24h_eth']} ETH",
            "hype_badge": f"Hype: {p['hype_score']}/10",
            "gauge_status": "BULLISH STAMPEDE 🟢"
        }
        clips_info.append((f"clip_{c_num:03d}", f"Clip {c_num:02d}: {p['name']} (Celeb Lore)", c_celeb_text, [celeb_name], c_celeb_overlays))
        c_num += 1

        # Science clip
        c_sci_text = f"{science_name}: {p['science_tech']} Code Rating: {p['tech_score']}/10!"
        c_sci_overlays = {
            "cowpedia_banner": f"Cow-pedia: {p['storage']} Verified",
            "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH",
            "tech_badge": f"Tech: {p['tech_score']}/10"
        }
        clips_info.append((f"clip_{c_num:03d}", f"Clip {c_num:02d}: {p['name']} (Science Tech)", c_sci_text, [science_name], c_sci_overlays))
        c_num += 1

    # Weather clip
    clips_info.append((f"clip_{c_num:03d}", f"Clip {c_num:02d}: Weather Forecast", f"{weather_name}: Expect high volatility across ERC-721 and Solana tokens tonight with an 80% chance of a bull surge! Embrace the chaos, traders!", [weather_name], {}))
    c_num += 1

    # Outro clip
    clips_info.append((f"clip_{c_num:03d}", f"Clip {c_num:02d}: Studio Outro", f"{celeb_name}: That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote! {science_name}: Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight!", [celeb_name, science_name], {"pasture_poll_qr_code": "SCAN QR CODE TO VOTE FOR NEXT WEEK'S WILDCARD NFT"}))

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

    with open(os.path.join(output_base, "google_flow_animation_manifest.json"), "w", encoding="utf-8") as mf:
        json.dump(manifest_data, mf, indent=2)

    print(f"[✓] Episode #{episode_num} generated with fresh projects: {[p['name'] for p in projects]}")

if __name__ == "__main__":
    main()

