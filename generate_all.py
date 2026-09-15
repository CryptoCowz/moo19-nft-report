#!/usr/bin/env python3
"""
MOO19 News: All-in-One Automated Episode & Newsletter Generator
Features a 30-Project Curated Rotation Pool across 5 Web3 Pillars,
an 18-Term Cow-pedia Educational Glossary, Least-Recently-Used (LRU)
rotation logic, dynamic newsroom hooks, and automated state tracking.
"""

import os
import sys
import json
import argparse
from datetime import datetime

# ---------------------------------------------------------------------------
# 1. Helper & 30-Project Curated Pool across 5 Pillars (6 per Pillar)
# ---------------------------------------------------------------------------
def _p(pid, name, chain, floor, vol, std, storage, url, opensea, art, lore, tech, hype, tscore):
    return {
        "id": pid, "name": name, "chain": chain, "floor_price_eth": floor, "volume_24h_eth": vol,
        "contract_standard": std, "storage": storage, "official_url": url, "opensea_url": opensea,
        "art_description": art, "celeb_lore": lore, "science_tech": tech, "hype_score": hype, "tech_score": tscore
    }

PROJECT_POOL = {
    "1_HISTORICAL_BLUECHIP": [
        _p("cryptopunks", "CryptoPunks", "Ethereum", 30.3, 66.79, "ERC-721 Custom", "On-Chain",
           "https://cryptopunks.app/", "https://opensea.io/collection/cryptopunks",
           "Iconic 24x24 pixel art portraits on vibrant solid background with rare punk traits like gold chains, wild hair, and shades",
           "Darlings, CryptoPunks became digital status symbols when Jay-Z and Snoop Dogg flexed Punks #6095 and #3831! 66.79 ETH volume!",
           "Fascinating! CryptoPunks code is stored 100% on Ethereum. Pure digital identity and blue-chip store of value.", 7.8, 9.5),
        _p("autoglyphs", "Autoglyphs", "Ethereum", 82.0, 15.40, "ERC-721", "On-Chain (Direct Bytecode)",
           "https://www.larvalabs.com/autoglyphs", "https://opensea.io/collection/autoglyphs",
           "Minimalist text-based ASCII geometric algorithms generated directly inside Ethereum smart contract bytecode",
           "Darlings, Autoglyphs are the ultimate ultra-rare flex! Only 512 exist, commanding an 82 ETH floor among museum collectors!",
           "Fascinating! Autoglyphs are the first on-chain generative art on Ethereum where the rendering algorithm lives entirely inside the smart contract.", 6.5, 10.0),
        _p("moonbirds", "Moonbirds", "Ethereum", 1.85, 52.35, "ERC-721", "IPFS & Yuga Ecosystem",
           "https://www.proof.xyz/moonbirds", "https://opensea.io/collection/moonbirds-official",
           "Charming 8-bit owl avatars featuring bespoke feathered plumage, glowing laser eyes, and wizard hats",
           "Darlings, Moonbirds took flight under Kevin Rose and joined the Yuga Labs family! 52.35 ETH volume this week!",
           "Fascinating! Moonbirds pioneered soft-staking through 'nesting', unlocking utility and artwork upgrades without transferring custody.", 7.5, 8.5),
        _p("curio_cards", "Curio Cards", "Ethereum", 0.45, 12.80, "ERC-20 Wrapped ERC-721", "IPFS & Arweave",
           "https://mycuriocards.com/", "https://opensea.io/collection/curiocards",
           "Vintage digital illustrated art cards created in 2017 representing some of the earliest art tokens on Ethereum",
           "Darlings, Christie's and Sotheby's auction houses auctioned full 31-card sets of Curio Cards as the dawn of NFT art history!",
           "Fascinating! Created in May 2017 before the ERC-721 standard even existed, requiring smart contract wrappers to trade on modern AMMs.", 6.8, 9.2),
        _p("rare_pepe", "Rare Pepe Series", "Bitcoin (Counterparty)", 1.20, 8.40, "Counterparty Assets", "Bitcoin Blockchain",
           "https://rarepepedirectory.com/", "https://emblem.finance/",
           "Underground satirical green frog trading cards minted on the Bitcoin blockchain between 2016 and 2018",
           "Darlings, the legendary Homer Pepe sold for over $320,000, making Rare Pepes the holy grail of crypto underground culture!",
           "Fascinating! Built atop Counterparty protocol on Bitcoin's UTXO ledger. They established the cryptographic art movement years before Ethereum NFTs.", 7.0, 9.6),
        _p("cryptoadz", "CrypToadz by Gremplin", "Ethereum", 0.65, 24.15, "ERC-721", "CC0 Public Domain / Arweave",
           "https://cryptoadz.io/", "https://opensea.io/collection/cryptoadz-by-gremplin",
           "Quirky pixelated amphibians escaping the tyrannical reign of Evil King Gremplin in amphibious underground realms",
           "Darlings, CrypToadz sparked the CC0 summer revolution! Anyone can build toys, games, and merchandise without paying licensing fees!",
           "Fascinating! CrypToadz released under CC0 Public Domain dedication, providing zero IP restrictions and distributed metadata architecture.", 7.2, 8.8)
    ],
    "2_MAINSTREAM_BRAND_IP": [
        _p("pudgy_penguins", "Pudgy Penguins", "Ethereum", 6.05, 255.94, "ERC-721", "IPFS",
           "https://pudgypenguins.com/", "https://opensea.io/collection/pudgypenguins",
           "Cute chubby penguin avatars in winter beanies, puffer jackets, bowties, and scarves on pastel backdrops",
           "Darlings, Pudgy Penguins conquered Target, Walmart, and Amazon with over 1 million plush toys sold worldwide!",
           "Fascinating! Pudgy Penguins uses ERC-721 with IPFS hosting, physical Pudgy Toys merch, and Overpass IP licensing.", 10.0, 8.0),
        _p("bored_ape_yacht_club", "Bored Ape Yacht Club", "Ethereum", 5.94, 42.34, "ERC-721", "IPFS",
           "https://boredapeyachtclub.com/", "https://opensea.io/collection/boredapeyachtclub",
           "Expressive bored ape avatars with sailor caps, leather jackets, horn rims, and multicolored neon grins",
           "Darlings, BAYC defined Web3 pop culture when Eminem, Madonna, and Steph Curry joined the club!",
           "Fascinating! BAYC grants full commercial IP usage rights, ApeCoin allocations, and Otherside metaverse land access.", 7.3, 8.0),
        _p("doodles", "Doodles", "Ethereum", 1.42, 68.20, "ERC-721", "IPFS & Solana L2",
           "https://doodles.app/", "https://opensea.io/collection/doodles-official",
           "Pastel hand-drawn cartoon characters by Burnt Toast featuring rainbows, ice cream cones, and space suits",
           "Darlings, Pharrell Williams joined Doodles as Chief Brand Officer, orchestrating fashion shows and animation collabs!",
           "Fascinating! Doodles has evolved into a multi-chain entertainment franchise with Doodles 2 enabling customizable dynamic off-chain wearables.", 8.4, 8.2),
        _p("azuki", "Azuki", "Ethereum", 4.10, 112.50, "ERC-721A", "IPFS & Arweave",
           "https://www.azuki.com/", "https://opensea.io/collection/azuki",
           "Stylized anime warriors featuring samurais, cybernetic swords, red beanies, and skateboards",
           "Darlings, Azuki brought anime streetwear to Paris Fashion Week and launched physical-backed token hoodies!",
           "Fascinating! Azuki invented the gas-optimized ERC-721A contract standard, reducing batch minting gas fees by over 70%.", 8.8, 9.0),
        _p("cool_cats", "Cool Cats", "Ethereum", 0.38, 18.90, "ERC-721", "IPFS",
           "https://coolcats.com/", "https://opensea.io/collection/cool-cats-nft",
           "Friendly blue feline characters drawn by Clon featuring hats, costumes, and whimsical expressions",
           "Darlings, Cool Cats marched in the Macy's Thanksgiving Day Parade as giant helium balloons!",
           "Fascinating! Cool Cats introduced the Cooltopia gaming loop with Milk tokenomics and interactive pet evolution contracts.", 7.6, 8.1),
        _p("world_of_women", "World of Women", "Ethereum", 0.52, 21.40, "ERC-721", "IPFS",
           "https://worldofwomen.art/", "https://opensea.io/collection/world-of-women-nft",
           "Diverse, colorful portraits of empowered women created by artist Yam Karkai celebrating global unity",
           "Darlings, Reese Witherspoon and Eva Longoria champion World of Women to onboard diverse voices into Web3!",
           "Fascinating! WoW established decentralized governance grants for female creators and sustainable royalty distributions.", 7.9, 8.3)
    ],
    "3_ONCHAIN_GENERATIVE_ART": [
        _p("chromie_squiggle", "Chromie Squiggle by Snowfro", "Ethereum", 7.80, 88.40, "ERC-721", "100% On-Chain",
           "https://chromiesquiggle.artblocks.io/", "https://opensea.io/collection/chromie-squiggle-by-snowfro",
           "Hypnotic vibrant rainbow spectrum ribbon curves generated algorithmically on a clean neutral background",
           "Darlings, Chromie Squiggle is the beating heart of Art Blocks! Sotheby's auction records made it an essential collector flex!",
           "Fascinating! Snowfro's p5.js script lives entirely on Ethereum. The hash of the mint transaction seeds the generative ribbon curves.", 8.9, 9.8),
        _p("fidenza", "Fidenza by Tyler Hobbs", "Ethereum", 48.5, 36.70, "ERC-721", "100% On-Chain",
           "https://tylerxhobbs.com/fidenza", "https://opensea.io/collection/fidenza-by-tyler-hobbs",
           "Smooth organic flow-field ribbons with non-overlapping vibrant rectangular geometries inspired by the town of Fidenza",
           "Darlings, Tyler Hobbs' Fidenza is hailed by art critics as the Mona Lisa of modern generative code art!",
           "Fascinating! Uses a deterministic flow field algorithm with non-intersecting curved lines calculated directly from blockchain entropy.", 9.2, 9.9),
        _p("ringers", "Ringers by Dmitri Cherniak", "Ethereum", 28.0, 41.20, "ERC-721", "100% On-Chain",
           "https://dmitricherniak.com/", "https://opensea.io/collection/ringers-by-dmitri-cherniak",
           "Algorithmic strings wrapping around static pegs creating complex topological loops and harmonic geometries",
           "Darlings, Ringers #879, affectionately known as The Goose, sold for $6.2 million at Sotheby's 3AC liquidation!",
           "Fascinating! Cherniak's deterministic script evaluates string wrapping geometry using winding numbers and Euler path mathematical principles.", 9.0, 9.9),
        _p("archetype", "Archetype by Kjetil Golid", "Ethereum", 12.4, 19.80, "ERC-721", "100% On-Chain",
           "https://kgolid.art/", "https://opensea.io/collection/archetype-by-kjetil-golid",
           "Precise architectural grid divisions with high-contrast color palettes and structural block harmonies",
           "Darlings, Archetype transformed geometric minimalism into one of the most prestigious Art Blocks Curated series!",
           "Fascinating! Uses recursive partition algorithms dividing rectangular planes into balanced spatial compositions.", 8.2, 9.7),
        _p("gazers", "Gazers by Matt Kane", "Ethereum", 6.90, 14.30, "ERC-721", "Dynamic On-Chain",
           "https://mattkane.com/", "https://opensea.io/collection/gazers-by-matt-kane",
           "Astrological lunar phases that synchronize with the actual celestial calendar, shifting visual color frequencies in real time",
           "Darlings, Gazers transforms with the lunar calendar! Your artwork shifts alongside the phases of the real Moon!",
           "Fascinating! Kane's smart contracts read temporal block timestamps to recalculate moon phase angles and color palettes dynamically.", 8.5, 9.8),
        _p("meridian", "Meridian by Matt DesLauriers", "Ethereum", 4.30, 11.60, "ERC-721", "100% On-Chain",
           "https://www.mattdesl.com/", "https://opensea.io/collection/meridian-by-matt-deslauriers",
           "Topographical landscapes composed of hundreds of thousands of colored strokes simulating mountain ranges and river basins",
           "Darlings, Meridian creates breathtaking virtual mountain summits using pure mathematical code!",
           "Fascinating! Generates multi-layered elevation heightmaps using Perlin noise shaders executed through on-chain SVG coordinates.", 8.0, 9.6)
    ],
    "4_DEFI_UTILITY_MODELS": [
        _p("infinex_patrons", "Infinex Patrons", "Ethereum", 1.79, 94.20, "ERC-721", "Off-Chain / S3",
           "https://infinex.xyz/", "https://opensea.io/collection/infinex-patrons",
           "Sleek holographic patronage cards featuring tiered node insignias, metallic chrome borders, and geometric security patterns",
           "Darlings, Kain Warwick raised over $65 million for Infinex to build the UX layer of crypto without seed seedphrases!",
           "Fascinating! Infinex Patrons act as governance keys for decentralized account abstraction across EVM and Solana.", 8.2, 7.9),
        _p("hypurr", "Hypurr", "Hyperliquid", 0.95, 34.10, "Hyperliquid L1 Native", "Hyperliquid L1",
           "https://hyperliquid.xyz/", "https://hypurr.fun/",
           "Dynamic futuristic cybernetic cat avatars representing native liquidity providers on Hyperliquid L1",
           "Darlings, Hypurr represents the absolute frontier of on-chain perp DEX power users on Hyperliquid!",
           "Fascinating! Minted directly on Hyperliquid's custom Layer-1 Tendermint-based consensus engine with sub-second finality.", 7.8, 8.8),
        _p("propy_rwa", "Propy Real Estate NFTs", "Ethereum / Base", 1.15, 16.50, "ERC-721", "Deed Vault & Legal On-Chain",
           "https://propy.com/", "https://opensea.io/collection/propy-real-estate",
           "Architectural legal deeds and digital certificates representing real physical real estate properties and title rights",
           "Darlings, imagine buying a beachfront villa or luxury condominium in 10 minutes by trading an NFT on Propy!",
           "Fascinating! Links smart contract ownership with US legal title registry through corporate entity LLC wrappers.", 7.4, 9.4),
        _p("uniswap_v3_positions", "Uniswap v3 Positions", "Ethereum", 0.85, 45.10, "ERC-721", "Dynamic On-Chain SVG",
           "https://uniswap.org/", "https://opensea.io/collection/uniswap-v3-positions",
           "Dynamic animated SVG cards displaying real-time price tick ranges, fee tiers, and liquidity curves",
           "Darlings, trading fees generated by automated market makers represented as glowing financial NFT collectibles!",
           "Fascinating! Each NFT stores concentrated liquidity tick boundaries, rendering dynamic SVG graphics generated entirely by bytecode.", 7.1, 9.8),
        _p("ens_domains", "Ethereum Name Service (ENS)", "Ethereum", 0.08, 120.40, "ERC-721", "On-Chain Registry",
           "https://ens.domains/", "https://opensea.io/collection/ens",
           "Readable web3 domain identities (.eth) replacing hex hexadecimal wallet addresses with personalized human handles",
           "Darlings, every crypto founder flexes their 3-digit or 4-digit .eth name across social media and on-chain messaging!",
           "Fascinating! Decentralized domain naming architecture supporting multi-chain address resolution and decentralized IPFS web routing.", 8.6, 9.5),
        _p("sudoswap_pools", "SudoSwap AMM Pools", "Ethereum", 0.35, 22.80, "ERC-721", "On-Chain Linear/Exponential AMM",
           "https://sudoswap.xyz/", "https://opensea.io/collection/sudoswap-pools",
           "Algorithmic bonding curves and liquidity pool routing keys providing instant decentralized liquidity for NFT collections",
           "Darlings, SudoSwap brought Uniswap-style bonding curves to digital art, eliminating illiquid orderbooks!",
           "Fascinating! Automates price discovery using mathematical bonding curves (linear and exponential) executed directly in smart contract pools.", 6.9, 9.3)
    ],
    "5_MULTICHAIN_COMMUNITY": [
        _p("mad_lads", "Mad Lads", "Solana", 2.65, 148.10, "Solana xNFT", "Arweave",
           "https://madlads.com/", "https://magiceden.io/marketplace/madlads",
           "Stylized hand-drawn rogue adventurers wearing leather aviator helmets, goggles, and rugged jackets",
           "Darlings, Mad Lads revitalized the entire Solana ecosystem! Armani Ferrante built an unstoppable army of devs!",
           "Fascinating! Mad Lads are xNFTs—executable tokenized programs running native code inside the Backpack wallet!", 9.4, 9.1),
        _p("milady_maker", "Milady Maker", "Ethereum", 1.95, 84.60, "ERC-721", "IPFS",
           "https://miladymaker.net/", "https://opensea.io/collection/milady",
           "Neotenic anime chibi avatars in Tokyo cyber-streetwear, berets, and oversized sunglasses",
           "Darlings, when Elon Musk tweeted a Milady meme, the entire crypto internet exploded into absolute mania!",
           "Fascinating! Milady Maker established an ultra-loyal post-ironic culture with procedural algorithmic asset layering.", 8.7, 7.8),
        _p("mutant_ape_yacht_club", "Mutant Ape Yacht Club", "Ethereum", 1.18, 46.80, "ERC-721", "IPFS",
           "https://boredapeyachtclub.com/", "https://opensea.io/collection/mutant-ape-yacht-club",
           "Mutated drippy primate avatars with neon slime, exposed ribcages, floating tentacles, and radioactive fangs",
           "Darlings, mutating an ape with a Mega Zombie Serum created the wildest livestream auctions in NFT history!",
           "Fascinating! MAYC pioneered the burning of ERC-20 Serums to trigger dynamic smart contract transmutation minting.", 7.8, 8.2),
        _p("nodemonkes", "NodeMonkes", "Bitcoin (Ordinals)", 0.165, 31.40, "Bitcoin Inscriptions", "100% Bitcoin Ordinals",
           "https://nodemonkes.com/", "https://magiceden.io/ordinals/marketplace/nodemonkes",
           "Charming 28x28 pixel art monkeys inscribed immutably into individual satoshis on the Bitcoin blockchain",
           "Darlings, NodeMonkes became the undisputed blue-chip king of Bitcoin Ordinals, rivaling Ethereum's top avatars!",
           "Fascinating! Inscribed directly into the witness data of Bitcoin transactions, ensuring permanent survival alongside Bitcoin.", 8.9, 9.5),
        _p("degods", "DeGods", "Solana / Ethereum", 1.05, 38.90, "ERC-721 / Metaplex", "Arweave",
           "https://degods.com/", "https://opensea.io/collection/degods",
           "God-tier deities wearing silk robes, laurel wreaths, and psychedelic sunglasses",
           "Darlings, DeGods pioneered deflationary burning and multi-chain bridging under the charismatic leadership of Frank!",
           "Fascinating! Built cross-chain Wormhole bridging contracts allowing non-custodial teleportation between Solana and Ethereum.", 8.1, 8.4),
        _p("sappy_seals", "Sappy Seals", "Ethereum", 0.42, 19.70, "ERC-721", "IPFS",
           "https://sappyseals.io/", "https://opensea.io/collection/sappy-seals",
           "Lovable round seal avatars sporting bucket hats, fish snacks, and joyful expressions",
           "Darlings, the Sappy Seals community conquered crypto Twitter with organic meme culture and positive energy!",
           "Fascinating! Developed the Pixl open-world metaverse with gamified staking loops and community meme reward engines.", 7.9, 8.0)
    ]
}

# ---------------------------------------------------------------------------
# 2. 18-Term Cow-pedia Educational Glossary
# ---------------------------------------------------------------------------
COWPEDIA_TERMS = [
    {"term": "Immutability (On-Chain Storage)", "definition": "Permanent, unalterable data written directly to decentralized blockchain state."},
    {"term": "Zero-Knowledge Proofs (ZKP)", "definition": "Cryptographic method to verify statement validity without revealing underlying data."},
    {"term": "xNFTs (Executable Tokens)", "definition": "Tokenized Web3 applications that execute native code directly inside digital wallets."},
    {"term": "On-Chain Generative Scripts", "definition": "Autonomous computer algorithms embedded in smart contract bytecode rendering art on demand."},
    {"term": "Soft-Staking (Nesting)", "definition": "Earning ecosystem yields or trait evolutions without transferring token custody out of your wallet."},
    {"term": "RWA (Real-World Asset) Tokenization)", "definition": "Bridging off-chain physical properties, commodities, or legal rights onto transparent blockchain ledgers."},
    {"term": "ERC-6551 (Token Bound Accounts)", "definition": "Transforming individual NFTs into smart contract wallets capable of owning tokens and assets."},
    {"term": "CC0 (Creative Commons Zero)", "definition": "Public domain dedication granting anyone total commercial rights to build and monetize brand assets."},
    {"term": "Decentralized Oracles", "definition": "Secure data feeds connecting external real-world information into deterministic smart contracts."},
    {"term": "Account Abstraction (ERC-4337)", "definition": "Smart contract wallets enabling gasless transactions, biometric recovery, and session keys."},
    {"term": "Fractionalization", "definition": "Dividing high-value non-fungible assets into fungible shares for distributed community ownership."},
    {"term": "Proof of Provenance & Royalties", "definition": "Verifiable on-chain historical ledger proving authenticity and routing creator fee distributions."},
    {"term": "Layer-2 Rollups", "definition": "Scalable execution networks bundling off-chain transactions to settle efficiently on Layer-1 Ethereum."},
    {"term": "Merkle Tree Whitelists", "definition": "Cryptographic leaf proof structures validating mint authorization with minimal on-chain gas costs."},
    {"term": "Bitcoin Ordinals & Inscriptions", "definition": "Inscribing raw digital data directly into individual satoshis inside Bitcoin witness blocks."},
    {"term": "Dynamic Metadata", "definition": "NFT properties that shift programmatically based on time, external feeds, or on-chain events."},
    {"term": "Soulbound Tokens (SBT)", "definition": "Non-transferable identity credentials bound permanently to a unique wallet address."},
    {"term": "AMM Bonding Curves", "definition": "Mathematical formulas automating continuous price discovery and liquidity pool balancing."}
]

# ---------------------------------------------------------------------------
# 3. Dynamic Newsroom Hooks & Weather Regimes
# ---------------------------------------------------------------------------
NEWSROOM_INTROS = [
    {"celeb": "Welcome back to MOO19 News! Today on the NFT Report, we're reviewing top digital flexes and cultural heat across the blockchain!",
     "science": "And check your screen for Cow-pedia Pop-ups and Scam or Stampede Checks! Let me examine the code under our digital microscope!"},
    {"celeb": "Darlings, the digital runways are ablaze! Welcome to MOO19 News, your weekly front-row ticket to Web3 high fashion and blue-chip lore!",
     "science": "Indeed, Minty! We have calibrated our on-chain analyzers to verify contract standards, bytecode integrity, and cryptographic provenance!"},
    {"celeb": "Hold onto your diamond hooves! MOO19 News is live with the latest digital drops, runway flexes, and creator royalty movements!",
     "science": "Precisely! We are tracking blockchain throughput, verifiable randomness, and decentralized metadata across all major ecosystems!"},
    {"celeb": "Bonjour Web3 fashionistas! Daisy M. Ledger here with your weekly breakdown of the most stylish assets in the metaverse!",
     "science": "And Professor Hartmut von Schnurrbart is ready to dissect the technical execution, gas optimizations, and smart contract security!"}
]

WEATHER_FORECASTS = [
    "Sunshine Innocent Nimbus reporting high-pressure bull surges sweeping across the digital plains! Low gas density and clear minting skies ahead!",
    "Sunshine Innocent Nimbus here! We are experiencing sideways crab-market consolidation with cool breezes across decentralized exchanges. Bundle up!",
    "Sunshine Innocent Nimbus reporting! Watch out for sudden thunderstorm spikes in Layer-1 gas fees! Recommend utilizing Layer-2 rollups until the storm passes!",
    "Sunshine Innocent Nimbus with your market forecast! Sunny skies, warm liquidity winds, and smooth floor prices brightening up the pasture all week!"
]

HISTORY_FILE = "episode_history.json"

# ---------------------------------------------------------------------------
# 4. LRU Rotation Logic & State Management
# ---------------------------------------------------------------------------
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    if "episodes" in data:
                        return data
                    elif "history" in data:
                        return {"episodes": data["history"]}
                    else:
                        data["episodes"] = []
                        return data
        except Exception:
            pass
    return {"episodes": []}

def save_history(history_data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history_data, f, indent=2)

def select_weekly_rotation():
    history = load_history()
    recent_episodes = history.get("episodes", [])
    episode_num = len(recent_episodes) + 1

    last_seen_episode = {}
    for ep_idx, ep in enumerate(recent_episodes):
        for pid in ep.get("featured_ids", []):
            last_seen_episode[pid] = ep_idx

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
        candidates_sorted = sorted(candidates, key=lambda c: last_seen_episode.get(c["id"], -1))
        selected_projects.append(candidates_sorted[0])

    term_idx = (episode_num - 1) % len(COWPEDIA_TERMS)
    selected_term = COWPEDIA_TERMS[term_idx]

    intro_template = NEWSROOM_INTROS[(episode_num - 1) % len(NEWSROOM_INTROS)]
    weather_text = WEATHER_FORECASTS[(episode_num - 1) % len(WEATHER_FORECASTS)]

    date_str = datetime.now().strftime("%Y-%m-%d")
    ep_record = {
        "episode_number": episode_num,
        "air_date": date_str,
        "featured_ids": [p["id"] for p in selected_projects],
        "featured_names": [p["name"] for p in selected_projects],
        "cowpedia_term": selected_term["term"]
    }
    history["episodes"].append(ep_record)
    save_history(history)

    return episode_num, selected_projects, selected_term, intro_template, weather_text

# ---------------------------------------------------------------------------
# 5. Production Generation Pipeline
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="MOO19 News Automated Production Generator")
    parser.add_argument("--output-dir", default="output", help="Directory to save generated artifacts")
    args = parser.parse_args()

    out_dir = args.output_dir
    bumpers_dir = os.path.join(out_dir, "bumpers")
    clips_dir = os.path.join(out_dir, "standalone_clips")
    os.makedirs(bumpers_dir, exist_ok=True)
    os.makedirs(clips_dir, exist_ok=True)

    episode_num, projects, term_info, intro_template, weather_text = select_weekly_rotation()
    air_date = datetime.now().strftime("%B %d, %Y")

    print(f"[*] Generating MOO19 NFT Report Episode #{episode_num} for {air_date}...")
    print(f"[*] Featured Projects: {', '.join(p['name'] for p in projects)}")
    print(f"[*] Cow-pedia Term: {term_info['term']}")

    # 5.1 Generate Bumpers JSON
    for idx, p in enumerate(projects, 1):
        bump_id = f"bump_{idx:03d}_{p['id']}_bump"
        bump_payload = {
            "bumper_id": bump_id,
            "project_name": p["name"],
            "duration_seconds": 4,
            "audio_sting": "Upbeat electronic bass drop with cheerful cowbell accent",
            "voiceover": f"Up next on the NFT Report: {p['name']}! Scan the code to inspect!",
            "visual_cue": f"Dynamic 2D graphic card displaying {p['name']} art ({p['art_description']}), floor price ({p['floor_price_eth']} ETH), and scannable QR Code linking to {p['official_url']}.",
            "on_screen_elements": {
                "collection_title": p["name"],
                "chain": p["chain"],
                "floor_price": f"{p['floor_price_eth']} ETH",
                "qr_target_url": p["official_url"],
                "network_logo": "MOO19 News - The Pasture"
            }
        }
        with open(os.path.join(bumpers_dir, f"{bump_id}.json"), "w", encoding="utf-8") as f:
            json.dump(bump_payload, f, indent=2)

    # 5.2 Generate Standalone Clips JSON
    all_clips = []
    # Clip 1: Intro
    c1 = {
        "clip_id": "clip_001_clip_01_studio_intro",
        "title": "Clip 01: Studio Intro",
        "duration_seconds": 10,
        "setting": "MOO19 News Studio - Newsroom01_Large copy.jpg",
        "dialogue": [
            {"speaker": "Daisy M. (Minty) Ledger", "line": intro_template["celeb"]},
            {"speaker": "Professor Hartmut von Schnurrbart", "line": intro_template["science"]}
        ],
        "visual_fx": "Wide newsroom camera shot, dual anchors behind modern desk, animated digital ticker below."
    }
    all_clips.append(c1)

    clip_counter = 2
    for p in projects:
        # Lore Clip
        c_lore = {
            "clip_id": f"clip_{clip_counter:03d}_clip_{clip_counter:02d}_{p['id']}_(celeb_lore)",
            "title": f"Clip {clip_counter:02d}: {p['name']} (Celeb Lore)",
            "duration_seconds": 10,
            "setting": "MOO19 News Studio (Anchor Left Focus)",
            "on_screen_graphic": f"{p['name']} | Floor: {p['floor_price_eth']} ETH | Vol: {p['volume_24h_eth']} ETH",
            "dialogue": [
                {"speaker": "Daisy M. (Minty) Ledger", "line": p["celeb_lore"]},
                {"speaker": "Daisy M. (Minty) Ledger", "line": f"Glam & Hype Rating: {p['hype_score']}/10!"}
            ],
            "visual_fx": "Glamour sparkle particles overlay, digital portrait framed in golden borders."
        }
        all_clips.append(c_lore)
        clip_counter += 1

        # Tech Clip
        c_tech = {
            "clip_id": f"clip_{clip_counter:03d}_clip_{clip_counter:02d}_{p['id']}_(science_tech)",
            "title": f"Clip {clip_counter:02d}: {p['name']} (Science Tech)",
            "duration_seconds": 10,
            "setting": "MOO19 News Studio (Anchor Right Focus next to Microscope)",
            "cowpedia_popup": f"{term_info['term']} — {term_info['definition']}",
            "dialogue": [
                {"speaker": "Professor Hartmut von Schnurrbart", "line": p["science_tech"]},
                {"speaker": "Professor Hartmut von Schnurrbart", "line": f"Code & Security Rating: {p['tech_score']}/10!"}
            ],
            "visual_fx": "Digital holographic microscope laser projection displaying smart contract hex code."
        }
        all_clips.append(c_tech)
        clip_counter += 1

    # Weather Clip
    c_weather = {
        "clip_id": f"clip_{clip_counter:03d}_clip_{clip_counter:02d}_weather_forecast",
        "title": f"Clip {clip_counter:02d}: Market Weather Forecast",
        "duration_seconds": 10,
        "setting": "MOO19 Weather Center - Green Screen Map",
        "dialogue": [
            {"speaker": "Sunshine Innocent Nimbus", "line": weather_text}
        ],
        "visual_fx": "Animated satellite radar displaying gas isobar cloud fronts over Ethereum and Solana."
    }
    all_clips.append(c_weather)
    clip_counter += 1

    # Outro Clip
    c_outro = {
        "clip_id": f"clip_{clip_counter:03d}_clip_{clip_counter:02d}_studio_outro",
        "title": f"Clip {clip_counter:02d}: Studio Outro",
        "duration_seconds": 10,
        "setting": "MOO19 News Studio - Wide Shot",
        "dialogue": [
            {"speaker": "Daisy M. (Minty) Ledger", "line": "That wraps today's NFT Report darlings! Stay glamorous and protect your private keys!"},
            {"speaker": "Professor Hartmut von Schnurrbart", "line": "Subscribe to The Pasture newsletter for complete technical audits! Auf Wiedersehen!"}
        ],
        "visual_fx": "Wide studio camera pull-back with end-credits banner rolling across the screen."
    }
    all_clips.append(c_outro)

    for c in all_clips:
        with open(os.path.join(clips_dir, f"{c['clip_id']}.json"), "w", encoding="utf-8") as f:
            json.dump(c, f, indent=2)

    # 5.3 Generate Google Flow Animation Manifest
    flow_manifest = {
        "production_title": f"MOO19 NFT Report - Episode #{episode_num}",
        "episode_number": episode_num,
        "air_date": air_date,
        "aspect_ratio": "16:9",
        "target_engine": "Google Flow & Veo Video Pipeline",
        "characters": [
            {"name": "Daisy M. (Minty) Ledger", "role": "Celebrity Anchor", "voice": "Mid-Atlantic glamorous, expressive"},
            {"name": "Professor Hartmut von Schnurrbart", "role": "Chief Scientist", "voice": "Bavarian academic, analytical"},
            {"name": "Sunshine Innocent Nimbus", "role": "Meteorologist", "voice": "Cheerful, upbeat, enthusiastic"}
        ],
        "timeline_sequence": []
    }

    seq_order = 1
    # Studio Intro
    flow_manifest["timeline_sequence"].append({
        "sequence_id": seq_order,
        "type": "studio_clip",
        "ref_id": all_clips[0]["clip_id"],
        "prompt": f"Wide shot of animated cow newsroom. Daisy M. Ledger and Professor Hartmut von Schnurrbart reporting. Dialogue: {all_clips[0]['dialogue'][0]['line']}"
    })
    seq_order += 1

    # Segments & Bumpers
    for idx, p in enumerate(projects, 1):
        bump_id = f"bump_{idx:03d}_{p['id']}_bump"
        flow_manifest["timeline_sequence"].append({
            "sequence_id": seq_order,
            "type": "bumper_card",
            "ref_id": bump_id,
            "prompt": f"2D animated title card for {p['name']}. Visual: {p['art_description']}. QR code and floor price {p['floor_price_eth']} ETH visible."
        })
        seq_order += 1

        lore_clip = all_clips[1 + (idx - 1) * 2]
        flow_manifest["timeline_sequence"].append({
            "sequence_id": seq_order,
            "type": "anchor_clip",
            "ref_id": lore_clip["clip_id"],
            "prompt": f"Close-up of Daisy M. Ledger animated talking passionately. Dialogue: {p['celeb_lore']}"
        })
        seq_order += 1

        tech_clip = all_clips[2 + (idx - 1) * 2]
        flow_manifest["timeline_sequence"].append({
            "sequence_id": seq_order,
            "type": "anchor_clip",
            "ref_id": tech_clip["clip_id"],
            "prompt": f"Medium shot of Professor Hartmut examining {p['name']} on digital microscope. Cow-pedia popup displayed. Dialogue: {p['science_tech']}"
        })
        seq_order += 1

    # Weather & Outro
    flow_manifest["timeline_sequence"].append({
        "sequence_id": seq_order,
        "type": "weather_clip",
        "ref_id": all_clips[-2]["clip_id"],
        "prompt": f"Animated weather anchor Sunshine Innocent Nimbus gesturing at colorful crypto market satellite map. Dialogue: {weather_text}"
    })
    seq_order += 1

    flow_manifest["timeline_sequence"].append({
        "sequence_id": seq_order,
        "type": "studio_outro",
        "ref_id": all_clips[-1]["clip_id"],
        "prompt": "Both anchors waving goodbye at the news desk as camera pans up to MOO19 Newsroom ceiling monitors."
    })

    with open(os.path.join(out_dir, "google_flow_animation_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(flow_manifest, f, indent=2)

    # 5.4 Generate Full Show Script Markdown
    script_lines = [
        f"# MOO19 NEWS: THE NFT REPORT (EPISODE #{episode_num})",
        f"**Air Date:** {air_date}  ",
        f"**Hosts:** Daisy M. (Minty) Ledger & Professor Hartmut von Schnurrbart  ",
        f"**Specialist:** Sunshine Innocent Nimbus (Market Weather)  \n",
        "============================================================",
        "### [CLIP 01: STUDIO INTRO (10s)]",
        f"**DAISY:** \"{intro_template['celeb']}\"",
        f"**PROFESSOR:** \"{intro_template['science']}\"\n",
        "============================================================"
    ]

    for idx, p in enumerate(projects, 1):
        script_lines.extend([
            f"### [BUMPER {idx:02d}: {p['name'].upper()} INTRO BUMP (4s)]",
            f"**VISUAL CUE:** Dynamic 2D graphic card displaying {p['name']} art ({p['art_description']}), floor price ({p['floor_price_eth']} ETH), and scannable QR Code linking to {p['official_url']}.",
            f"**AUDIO STING & VO:** \"Up next on the NFT Report: {p['name']}! Scan to explore!\"\n",
            f"### [CLIP {2 + (idx-1)*2:02d}: {p['name'].upper()} - LORE & GLAM (10s)]",
            f"**ON-SCREEN GRAPHIC:** {p['name']} | Floor: {p['floor_price_eth']} ETH | Vol: {p['volume_24h_eth']} ETH",
            f"**DAISY:** \"{p['celeb_lore']}\"",
            f"**DAISY:** \"Glam & Hype Rating: {p['hype_score']}/10!\"\n",
            f"### [CLIP {3 + (idx-1)*2:02d}: {p['name'].upper()} - TECH & CODE (10s)]",
            f"**[COW-PEDIA POP-UP]:** **{term_info['term']}** — {term_info['definition']}",
            f"**PROFESSOR:** \"{p['science_tech']}\"",
            f"**PROFESSOR:** \"Code & Security Rating: {p['tech_score']}/10!\"\n",
            "------------------------------------------------------------"
        ])

    script_lines.extend([
        "### [MARKET WEATHER FORECAST (10s)]",
        f"**SUNSHINE:** \"{weather_text}\"\n",
        "### [STUDIO OUTRO (10s)]",
        "**DAISY:** \"That wraps today's NFT Report darlings! Stay glamorous and protect your private keys!\"",
        "**PROFESSOR:** \"Subscribe to The Pasture newsletter for complete technical audits! Auf Wiedersehen!\""
    ])

    with open(os.path.join(out_dir, "weekly_nft_report_script.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(script_lines))

    # 5.5 Generate YouTube Shorts Script Markdown
    shorts_lines = [
        f"# MOO19 SHORTS: TOP 3 DIGITAL FLEXES THIS WEEK (EPISODE #{episode_num})",
        f"**Air Date:** {air_date} | **Format:** 9:16 Vertical Video (58s Total)\n",
        "00:00 - 00:05 | Hook: Daisy & Professor welcome viewers to this week's rapid-fire NFT Report!",
        f"00:05 - 00:20 | Segment 1: {projects[0]['name']} ({projects[0]['floor_price_eth']} ETH floor) - {projects[0]['celeb_lore']}",
        f"00:20 - 00:35 | Segment 2: {projects[1]['name']} ({projects[1]['floor_price_eth']} ETH floor) - {projects[1]['celeb_lore']}",
        f"00:35 - 00:50 | Segment 3: {projects[2]['name']} ({projects[2]['floor_price_eth']} ETH floor) - {projects[2]['science_tech']}",
        f"00:50 - 00:58 | Outro: Cow-pedia Term '{term_info['term']}' highlighted! Subscribe to MOO19 News!"
    ]
    with open(os.path.join(out_dir, "weekly_nft_report_shorts_script.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(shorts_lines))

    # 5.6 Generate The Pasture Post Newsletter Markdown
    newsletter_lines = [
        f"# The Pasture Post — Issue #{episode_num}",
        f"**Date:** {air_date}  ",
        "**From:** The Pasture Editorial Board  \n",
        "## Executive Summary",
        f"Welcome to Issue #{episode_num} of *The Pasture Post*. This week our newsroom investigated five distinct sectors of the decentralized ecosystem, evaluating both cultural momentum and contract architecture.\n",
        "## Featured Collections & Architectural Audits",
    ]

    for p in projects:
        newsletter_lines.extend([
            f"### {p['name']} ({p['chain']})",
            f"- **Floor Price:** {p['floor_price_eth']} ETH | **24h Volume:** {p['volume_24h_eth']} ETH",
            f"- **Contract Standard:** `{p['contract_standard']}` | **Storage Architecture:** {p['storage']}",
            f"- **Official Link:** [{p['name']} Website]({p['official_url']}) | **OpenSea:** [Marketplace Listing]({p['opensea_url']})",
            f"- **Cultural Commentary (Daisy M. Ledger):** {p['celeb_lore']} *(Hype Rating: {p['hype_score']}/10)*",
            f"- **Technical Analysis (Prof. Hartmut von Schnurrbart):** {p['science_tech']} *(Code Rating: {p['tech_score']}/10)*\n"
        ])

    newsletter_lines.extend([
        f"## Cow-pedia Educational Spotlight: {term_info['term']}",
        f"> **{term_info['term']}:** {term_info['definition']}\n",
        "## Pasture Market Weather Outlook",
        f"> *\"{weather_text}\"* — Sunshine Innocent Nimbus\n",
        "---",
        "*The Pasture Post is an educational publication by MOO19 News. Not financial advice. Always verify smart contract bytecode before transacting.*"
    ])

    with open(os.path.join(out_dir, "weekly_pasture_post_newsletter.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(newsletter_lines))

    print(f"[✓] Episode #{episode_num} generated with fresh projects: {[p['name'] for p in projects]}")

if __name__ == "__main__":
    main()
