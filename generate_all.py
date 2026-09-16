#!/usr/bin/env python3
"""
MOO19 News: All-in-One Automated Episode & Newsletter Generator
Features a 30-Project Curated Rotation Pool across 5 Web3 Pillars,
an 18-Term Cow-pedia Glossary, LRU rotation logic, and dynamic dated delivery.
"""

import os
import sys
import json
import shutil
import argparse
from datetime import datetime

def _p(pid, name, chain, floor, vol, std, storage, url, opensea, art, lore, tech, hype, tscore):
    return {
        "id": pid, "name": name, "chain": chain, "floor_price_eth": floor, "volume_24h_eth": vol,
        "contract_standard": std, "storage": storage, "official_url": url, "opensea_url": opensea,
        "art_description": art, "celeb_lore": lore, "science_tech": tech, "hype_score": hype, "tech_score": tscore
    }

PROJECT_POOL = {
    '1_HISTORICAL_BLUECHIP': [
        _p('cryptopunks', 'CryptoPunks', 'Ethereum', 30.3, 66.79, 'ERC-721 Custom', 'On-Chain', 'https://cryptopunks.app/', 'https://opensea.io/collection/cryptopunks', 'Iconic 24x24 pixel art portraits on vibrant solid background with rare punk traits like gold chains, wild hair, and shades', 'Darlings, CryptoPunks became digital status symbols when Jay-Z and Snoop Dogg flexed Punks #6095 and #3831! 66.79 ETH volume!', 'Fascinating! CryptoPunks code is stored 100% on Ethereum. Pure digital identity and blue-chip store of value.', 7.8, 9.5),
        _p('autoglyphs', 'Autoglyphs', 'Ethereum', 82.0, 15.4, 'ERC-721', 'On-Chain (Direct Bytecode)', 'https://www.larvalabs.com/autoglyphs', 'https://opensea.io/collection/autoglyphs', 'Minimalist text-based ASCII geometric algorithms generated directly inside Ethereum smart contract bytecode', 'Darlings, Autoglyphs are the ultimate ultra-rare flex! Only 512 exist, commanding an 82 ETH floor among museum collectors!', 'Fascinating! Autoglyphs are the first on-chain generative art on Ethereum where the rendering algorithm lives entirely inside the smart contract.', 6.5, 10.0),
        _p('moonbirds', 'Moonbirds', 'Ethereum', 1.85, 52.35, 'ERC-721', 'IPFS & Yuga Ecosystem', 'https://www.proof.xyz/moonbirds', 'https://opensea.io/collection/moonbirds-official', 'Charming 8-bit owl avatars featuring bespoke feathered plumage, glowing laser eyes, and wizard hats', 'Darlings, Moonbirds took flight under Kevin Rose and joined the Yuga Labs family! 52.35 ETH volume this week!', "Fascinating! Moonbirds pioneered soft-staking through 'nesting', unlocking utility and artwork upgrades without transferring custody.", 7.5, 8.5),
        _p('curio_cards', 'Curio Cards', 'Ethereum', 0.45, 12.8, 'ERC-20 Wrapped ERC-721', 'IPFS & Arweave', 'https://mycuriocards.com/', 'https://opensea.io/collection/curiocards', 'Vintage digital illustrated art cards created in 2017 representing some of the earliest art tokens on Ethereum', "Darlings, Christie's and Sotheby's auction houses auctioned full 31-card sets of Curio Cards as the dawn of NFT art history!", 'Fascinating! Created in May 2017 before the ERC-721 standard even existed, requiring smart contract wrappers to trade on modern AMMs.', 6.8, 9.2),
        _p('rare_pepe_series', 'Rare Pepe Series', 'Bitcoin (Counterparty)', 1.2, 8.4, 'Counterparty Assets', 'Bitcoin Blockchain', 'https://rarepepedirectory.com/', 'https://emblem.finance/', 'Underground satirical green frog trading cards minted on the Bitcoin blockchain between 2016 and 2018', 'Darlings, the legendary Homer Pepe sold for over $320,000, making Rare Pepes the holy grail of crypto underground culture!', "Fascinating! Built atop Counterparty protocol on Bitcoin's UTXO ledger. They established the cryptographic art movement years before Ethereum NFTs.", 7.0, 9.6),
        _p('cryptoadz_by_gremplin', 'CrypToadz by Gremplin', 'Ethereum', 0.65, 24.15, 'ERC-721', 'CC0 Public Domain / Arweave', 'https://cryptoadz.io/', 'https://opensea.io/collection/cryptoadz-by-gremplin', 'Quirky pixelated amphibians escaping the tyrannical reign of Evil King Gremplin in amphibious underground realms', 'Darlings, CrypToadz sparked the CC0 summer revolution! Anyone can build toys, games, and merchandise without paying licensing fees!', 'Fascinating! CrypToadz released under CC0 Public Domain dedication, providing zero IP restrictions and distributed metadata architecture.', 7.2, 8.8),
    ],
    '2_MAINSTREAM_BRAND_IP': [
        _p('pudgy_penguins', 'Pudgy Penguins', 'Ethereum', 6.05, 255.94, 'ERC-721', 'IPFS', 'https://pudgypenguins.com/', 'https://opensea.io/collection/pudgypenguins', 'Cute chubby penguin avatars in winter beanies, puffer jackets, bowties, and scarves on pastel backdrops', 'Darlings, Pudgy Penguins conquered Target, Walmart, and Amazon with over 1 million plush toys sold worldwide!', 'Fascinating! Pudgy Penguins uses ERC-721 with IPFS hosting, physical Pudgy Toys merch, and Overpass IP licensing.', 10.0, 8.0),
        _p('bored_ape_yacht_club', 'Bored Ape Yacht Club', 'Ethereum', 5.94, 42.34, 'ERC-721', 'IPFS', 'https://boredapeyachtclub.com/', 'https://opensea.io/collection/boredapeyachtclub', 'Expressive bored ape avatars with sailor caps, leather jackets, horn rims, and multicolored neon grins', 'Darlings, BAYC defined Web3 pop culture when Eminem, Madonna, and Steph Curry joined the club!', 'Fascinating! BAYC grants full commercial IP usage rights, ApeCoin allocations, and Otherside metaverse land access.', 7.3, 8.0),
        _p('doodles', 'Doodles', 'Ethereum', 1.42, 68.2, 'ERC-721', 'IPFS & Solana L2', 'https://doodles.app/', 'https://opensea.io/collection/doodles-official', 'Pastel hand-drawn cartoon characters by Burnt Toast featuring rainbows, ice cream cones, and space suits', 'Darlings, Pharrell Williams joined Doodles as Chief Brand Officer, orchestrating fashion shows and animation collabs!', 'Fascinating! Doodles has evolved into a multi-chain entertainment franchise with Doodles 2 enabling customizable dynamic off-chain wearables.', 8.4, 8.2),
        _p('azuki', 'Azuki', 'Ethereum', 4.1, 112.5, 'ERC-721A', 'IPFS & Arweave', 'https://www.azuki.com/', 'https://opensea.io/collection/azuki', 'Stylized anime warriors featuring samurais, cybernetic swords, red beanies, and skateboards', 'Darlings, Azuki brought anime streetwear to Paris Fashion Week and launched physical-backed token hoodies!', 'Fascinating! Azuki invented the gas-optimized ERC-721A contract standard, reducing batch minting gas fees by over 70%.', 8.8, 9.0),
        _p('cool_cats', 'Cool Cats', 'Ethereum', 0.38, 18.9, 'ERC-721', 'IPFS', 'https://coolcats.com/', 'https://opensea.io/collection/cool-cats-nft', 'Friendly blue feline characters drawn by Clon featuring hats, costumes, and whimsical expressions', "Darlings, Cool Cats marched in the Macy's Thanksgiving Day Parade as giant helium balloons!", 'Fascinating! Cool Cats introduced the Cooltopia gaming loop with Milk tokenomics and interactive pet evolution contracts.', 7.6, 8.1),
        _p('world_of_women', 'World of Women', 'Ethereum', 0.52, 21.4, 'ERC-721', 'IPFS', 'https://worldofwomen.art/', 'https://opensea.io/collection/world-of-women-nft', 'Diverse, colorful portraits of empowered women created by artist Yam Karkai celebrating global unity', 'Darlings, Reese Witherspoon and Eva Longoria champion World of Women to onboard diverse voices into Web3!', 'Fascinating! WoW established decentralized governance grants for female creators and sustainable royalty distributions.', 7.9, 8.3),
    ],
    '3_ONCHAIN_GENERATIVE_ART': [
        _p('chromie_squiggle_by_snowfro', 'Chromie Squiggle by Snowfro', 'Ethereum', 7.8, 88.4, 'ERC-721', '100% On-Chain', 'https://chromiesquiggle.artblocks.io/', 'https://opensea.io/collection/chromie-squiggle-by-snowfro', 'Hypnotic vibrant rainbow spectrum ribbon curves generated algorithmically on a clean neutral background', "Darlings, Chromie Squiggle is the beating heart of Art Blocks! Sotheby's auction records made it an essential collector flex!", "Fascinating! Snowfro's p5.js script lives entirely on Ethereum. The hash of the mint transaction seeds the generative ribbon curves.", 8.9, 9.8),
        _p('fidenza_by_tyler_hobbs', 'Fidenza by Tyler Hobbs', 'Ethereum', 48.5, 36.7, 'ERC-721', '100% On-Chain', 'https://tylerxhobbs.com/fidenza', 'https://opensea.io/collection/fidenza-by-tyler-hobbs', 'Smooth organic flow-field ribbons with non-overlapping vibrant rectangular geometries inspired by the town of Fidenza', "Darlings, Tyler Hobbs' Fidenza is hailed by art critics as the Mona Lisa of modern generative code art!", 'Fascinating! Uses a deterministic flow field algorithm with non-intersecting curved lines calculated directly from blockchain entropy.', 9.2, 9.9),
        _p('ringers_by_dmitri_cherniak', 'Ringers by Dmitri Cherniak', 'Ethereum', 28.0, 41.2, 'ERC-721', '100% On-Chain', 'https://dmitricherniak.com/', 'https://opensea.io/collection/ringers-by-dmitri-cherniak', 'Algorithmic strings wrapping around static pegs creating complex topological loops and harmonic geometries', "Darlings, Ringers #879, affectionately known as The Goose, sold for $6.2 million at Sotheby's 3AC liquidation!", "Fascinating! Cherniak's deterministic script evaluates string wrapping geometry using winding numbers and Euler path mathematical principles.", 9.0, 9.9),
        _p('archetype_by_kjetil_golid', 'Archetype by Kjetil Golid', 'Ethereum', 12.4, 19.8, 'ERC-721', '100% On-Chain', 'https://kgolid.art/', 'https://opensea.io/collection/archetype-by-kjetil-golid', 'Precise architectural grid divisions with high-contrast color palettes and structural block harmonies', 'Darlings, Archetype transformed geometric minimalism into one of the most prestigious Art Blocks Curated series!', 'Fascinating! Uses recursive partition algorithms dividing rectangular planes into balanced spatial compositions.', 8.2, 9.7),
        _p('gazers_by_matt_kane', 'Gazers by Matt Kane', 'Ethereum', 6.9, 14.3, 'ERC-721', 'Dynamic On-Chain', 'https://mattkane.com/', 'https://opensea.io/collection/gazers-by-matt-kane', 'Astrological lunar phases that synchronize with the actual celestial calendar, shifting visual color frequencies in real time', 'Darlings, Gazers transforms with the lunar calendar! Your artwork shifts alongside the phases of the real Moon!', 'Fascinating! Kane smart contracts read temporal block timestamps to recalculate moon phase angles and color palettes dynamically.', 8.5, 9.8),
        _p('meridian_by_matt_deslauriers', 'Meridian by Matt DesLauriers', 'Ethereum', 4.3, 11.6, 'ERC-721', '100% On-Chain', 'https://www.mattdesl.com/', 'https://opensea.io/collection/meridian-by-matt-deslauriers', 'Topographical landscapes composed of hundreds of thousands of colored strokes simulating mountain ranges and river basins', 'Darlings, Meridian creates breathtaking virtual mountain summits using pure mathematical code!', 'Fascinating! Generates multi-layered elevation heightmaps using Perlin noise shaders executed through on-chain SVG coordinates.', 8.0, 9.6),
    ],
    '4_DEFI_UTILITY_MODELS': [
        _p('infinex_patrons', 'Infinex Patrons', 'Ethereum', 1.79, 94.2, 'ERC-721', 'Off-Chain / S3', 'https://infinex.xyz/', 'https://opensea.io/collection/infinex-patrons', 'Sleek holographic patronage cards featuring tiered node insignias, metallic chrome borders, and geometric security patterns', 'Darlings, Kain Warwick raised over $65 million for Infinex to build the UX layer of crypto without seed phrases!', 'Fascinating! Infinex Patrons act as governance keys for decentralized account abstraction across EVM and Solana.', 8.2, 7.9),
        _p('hypurr', 'Hypurr', 'Hyperliquid', 0.95, 34.1, 'Hyperliquid L1 Native', 'Hyperliquid L1', 'https://hyperliquid.xyz/', 'https://hypurr.fun/', 'Dynamic futuristic cybernetic cat avatars representing native liquidity providers on Hyperliquid L1', 'Darlings, Hypurr represents the absolute frontier of on-chain perp DEX power users on Hyperliquid!', "Fascinating! Minted directly on Hyperliquid's custom Layer-1 Tendermint-based consensus engine with sub-second finality.", 7.8, 8.8),
        _p('propy_real_estate_nfts', 'Propy Real Estate NFTs', 'Ethereum / Base', 1.15, 16.5, 'ERC-721', 'Deed Vault & Legal On-Chain', 'https://propy.com/', 'https://opensea.io/collection/propy-real-estate', 'Architectural legal deeds and digital certificates representing real physical real estate properties and title rights', 'Darlings, imagine buying a beachfront villa or luxury condominium in 10 minutes by trading an NFT on Propy!', 'Fascinating! Links smart contract ownership with US legal title registry through corporate entity LLC wrappers.', 7.4, 9.4),
        _p('uniswap_v3_positions', 'Uniswap v3 Positions', 'Ethereum', 0.85, 45.1, 'ERC-721', 'Dynamic On-Chain SVG', 'https://uniswap.org/', 'https://opensea.io/collection/uniswap-v3-positions', 'Dynamic animated SVG cards displaying real-time price tick ranges, fee tiers, and liquidity curves', 'Darlings, trading fees generated by automated market makers represented as glowing financial NFT collectibles!', 'Fascinating! Each NFT stores concentrated liquidity tick boundaries, rendering dynamic SVG graphics generated entirely by bytecode.', 7.1, 9.8),
        _p('ethereum_name_service_(ens)', 'Ethereum Name Service (ENS)', 'Ethereum', 0.08, 120.4, 'ERC-721', 'On-Chain Registry', 'https://ens.domains/', 'https://opensea.io/collection/ens', 'Readable web3 domain identities (.eth) replacing hex hexadecimal wallet addresses with personalized human handles', 'Darlings, every crypto founder flexes their 3-digit or 4-digit .eth name across social media and on-chain messaging!', 'Fascinating! Decentralized domain naming architecture supporting multi-chain address resolution and decentralized IPFS web routing.', 8.6, 9.5),
        _p('sudoswap_amm_pools', 'SudoSwap AMM Pools', 'Ethereum', 0.35, 22.8, 'ERC-721', 'On-Chain Linear/Exponential AMM', 'https://sudoswap.xyz/', 'https://opensea.io/collection/sudoswap-pools', 'Algorithmic bonding curves and liquidity pool routing keys providing instant decentralized liquidity for NFT collections', 'Darlings, SudoSwap brought Uniswap-style bonding curves to digital art, eliminating illiquid orderbooks!', 'Fascinating! Automates price discovery using mathematical bonding curves (linear and exponential) executed directly in smart contract pools.', 6.9, 9.3),
    ],
    '5_MULTICHAIN_COMMUNITY': [
        _p('mad_lads', 'Mad Lads', 'Solana', 2.65, 148.1, 'Solana xNFT', 'Arweave', 'https://madlads.com/', 'https://magiceden.io/marketplace/madlads', 'Stylized hand-drawn rogue adventurers wearing leather aviator helmets, goggles, and rugged jackets', 'Darlings, Mad Lads revitalized the entire Solana ecosystem! Armani Ferrante built an unstoppable army of devs!', 'Fascinating! Mad Lads are xNFTs—executable tokenized programs running native code inside the Backpack wallet!', 9.4, 9.1),
        _p('milady_maker', 'Milady Maker', 'Ethereum', 1.95, 84.6, 'ERC-721', 'IPFS', 'https://miladymaker.net/', 'https://opensea.io/collection/milady', 'Neotenic anime chibi avatars in Tokyo cyber-streetwear, berets, and oversized sunglasses', 'Darlings, when Elon Musk tweeted a Milady meme, the entire crypto internet exploded into absolute mania!', 'Fascinating! Milady Maker established an ultra-loyal post-ironic culture with procedural algorithmic asset layering.', 8.7, 7.8),
        _p('mutant_ape_yacht_club', 'Mutant Ape Yacht Club', 'Ethereum', 1.18, 46.8, 'ERC-721', 'IPFS', 'https://boredapeyachtclub.com/', 'https://opensea.io/collection/mutant-ape-yacht-club', 'Mutated drippy primate avatars with neon slime, exposed ribcages, floating tentacles, and radioactive fangs', 'Darlings, mutating an ape with a Mega Zombie Serum created the wildest livestream auctions in NFT history!', 'Fascinating! MAYC pioneered the burning of ERC-20 Serums to trigger dynamic smart contract transmutation minting.', 7.8, 8.2),
        _p('nodemonkes', 'NodeMonkes', 'Bitcoin (Ordinals)', 0.165, 31.4, 'Bitcoin Inscriptions', '100% Bitcoin Ordinals', 'https://nodemonkes.com/', 'https://magiceden.io/ordinals/marketplace/nodemonkes', 'Charming 28x28 pixel art monkeys inscribed immutably into individual satoshis on the Bitcoin blockchain', "Darlings, NodeMonkes became the undisputed blue-chip king of Bitcoin Ordinals, rivaling Ethereum's top avatars!", 'Fascinating! Inscribed directly into the witness data of Bitcoin transactions, ensuring permanent survival alongside Bitcoin.', 8.9, 9.5),
        _p('degods', 'DeGods', 'Solana / Ethereum', 1.05, 38.9, 'ERC-721 / Metaplex', 'Arweave', 'https://degods.com/', 'https://opensea.io/collection/degods', 'God-tier deities wearing silk robes, laurel wreaths, and psychedelic sunglasses', 'Darlings, DeGods pioneered deflationary burning and multi-chain bridging under the charismatic leadership of Frank!', 'Fascinating! Built cross-chain Wormhole bridging contracts allowing non-custodial teleportation between Solana and Ethereum.', 8.1, 8.4),
        _p('sappy_seals', 'Sappy Seals', 'Ethereum', 0.42, 19.7, 'ERC-721', 'IPFS', 'https://sappyseals.io/', 'https://opensea.io/collection/sappy-seals', 'Lovable round seal avatars sporting bucket hats, fish snacks, and joyful expressions', 'Darlings, the Sappy Seals community conquered crypto Twitter with organic meme culture and positive energy!', 'Fascinating! Developed the Pixl open-world metaverse with gamified staking loops and community meme reward engines.', 7.9, 8.0),
    ],
}

COWPEDIA_TERMS = [
    {"term": 'Immutability (On-Chain Storage)', "definition": 'The mathematical state of being permanent and unchangeable once written into the blockchain distributed ledger.', "plain_english": 'Once minted on-chain, no CEO, government, or server crash can ever delete, modify, or seize your digital asset.'},
    {"term": 'Zero-Knowledge Proofs (ZKP)', "definition": 'Cryptographic algorithms that verify data authenticity without exposing private details.', "plain_english": 'Proving you possess the secret password or transaction balance without ever showing the numbers.'},
    {"term": 'xNFTs (Executable Tokens)', "definition": 'Non-fungible tokens packaged as runnable applications directly executed inside Web3 wallets.', "plain_english": 'Instead of a static JPEG, your token is a playable mini-game or decentralized app running inside your wallet.'},
    {"term": 'Decentralized Metadata (IPFS/Arweave)', "definition": 'Distributed peer-to-peer content addressing systems ensuring files cannot disappear if a centralized server goes offline.', "plain_english": 'Files pinned across a global network by cryptographic hash instead of relying on a company web server.'},
    {"term": 'On-Chain Generative Scripts', "definition": 'Algorithmic computer code stored directly in smart contract bytecode executing deterministic visuals.', "plain_english": 'Art rendered directly by the Ethereum network computing math equations on the fly.'},
    {"term": 'Soft-Staking (Nesting)', "definition": 'Ecosystem rewards earned while holding assets without transferring wallet custody.', "plain_english": 'Your tokens level up or accrue yield while safely sitting inside your hardware wallet.'},
    {"term": 'RWA (Real-World Asset) Tokenization', "definition": 'Bridging physical real estate, legal titles, or commodities onto blockchain ledgers.', "plain_english": 'Trading deeds to real homes or gold bars with instant digital settlement.'},
    {"term": 'ERC-6551 (Token Bound Accounts)', "definition": 'Assigning a decentralized smart contract wallet to each non-fungible token.', "plain_english": 'Your avatar NFT now owns its own cryptocurrency, wearables, and inventory.'},
    {"term": 'CC0 Public Domain Architecture', "definition": 'Waiving all copyright restrictions to allow open-source commercialization of brand IP.', "plain_english": 'Anyone can produce movies, apparel, or toys featuring the collection without paying royalties.'},
    {"term": 'Dynamic Metadata & Oracles', "definition": 'Smart contracts that alter token artwork based on real-world data or lunar cycles.', "plain_english": 'Art that shifts color when the stock market rises or when the moon enters a full phase.'},
    {"term": 'Fractionalized NFTs', "definition": 'Splitting non-fungible digital tokens into millions of fungible ERC-20 shares.', "plain_english": 'Allowing thousands of collectors to co-own a multi-million-dollar CryptoPunk.'},
    {"term": 'Layer-2 Rollups & Gas Optimization', "definition": 'Secondary blockchain layers executing transactions off-chain and posting compressed proofs.', "plain_english": 'Slashing transaction fees from fifty dollars down to fractions of a penny.'},
    {"term": 'Soulbound Tokens (SBT)', "definition": 'Non-transferable digital identity tokens bound permanently to a wallet address.', "plain_english": 'Digital diplomas and attendance certificates that cannot be bought or sold.'},
    {"term": 'Proof of Provenance', "definition": 'An unbroken cryptographic audit trail tracing an asset back to the creator wallet.', "plain_english": 'Digital certificates that verify the complete ownership history of fine art.'},
    {"term": 'Bitcoin Ordinals & Inscriptions', "definition": 'Inscribing digital artifacts directly into individual satoshis on the Bitcoin blockchain.', "plain_english": 'Writing digital files permanently into the core ledger of Bitcoin.'},
    {"term": 'Smart Contract Automated Market Makers (AMMs)', "definition": 'Mathematical liquidity pools replacing centralized order books for instant trading.', "plain_english": 'Automated mathematical vending machines that trade digital assets 24/7.'},
    {"term": 'Merkle Tree Proofs', "definition": 'Cryptographic data structures validating whitelist mint access with near-zero gas.', "plain_english": 'Ultra-efficient verification checks allowing millions of users to mint without network congestion.'},
    {"term": 'Decentralized Identifiers (DIDs)', "definition": 'Human-readable blockchain addresses replacing hexadecimal strings.', "plain_english": 'Using yourname.eth instead of a 42-character string of random letters and numbers.'},
]

NEWSROOM_INTROS = [
    {"celeb": "Welcome back to MOO19 News! Today on Episode #{ep} of the NFT Report, we're reviewing top digital flexes and cultural heat across the blockchain!", "science": "And check your screen for Cow-pedia Pop-ups on {term}! Let me examine the bytecode under our digital microscope!"},
    {"celeb": "Darlings, the digital runways are ablaze! Welcome to MOO19 News Episode #{ep}, your weekly front-row ticket to Web3 high fashion and blue-chip lore!", "science": "Indeed, Minty! We have calibrated our on-chain analyzers to verify contract standards, bytecode integrity, and cryptographic provenance on {term}!"},
    {"celeb": "Hold onto your diamond hooves! MOO19 News Episode #{ep} is live with the latest digital drops, runway flexes, and creator royalty movements!", "science": "Precisely! We are tracking blockchain throughput, verifiable randomness, and decentralized metadata for {term} across all major ecosystems!"},
    {"celeb": "Bonjour Web3 fashionistas! Daisy M. Ledger here for Episode #{ep} with your weekly breakdown of the most stylish assets in the metaverse!", "science": "And Professor Hartmut von Schnurrbart is ready to dissect technical execution, gas optimizations, and smart contract security on {term}!"},
]

WEATHER_FORECASTS = [
    'Sunshine Innocent Nimbus reporting high-pressure bull surges sweeping across the digital plains! Low gas density and clear minting skies ahead!',
    'Sunshine Innocent Nimbus here! We are experiencing sideways crab-market consolidation with cool breezes across decentralized exchanges. Bundle up!',
    'Sunshine Innocent Nimbus reporting! Watch out for sudden thunderstorm spikes in Layer-1 gas fees! Recommend utilizing Layer-2 rollups until the storm passes!',
    'Sunshine Innocent Nimbus with your market forecast! Sunny skies, warm liquidity winds, and smooth floor prices brightening up the pasture all week!',
]

HISTORY_FILE = "episode_history.json"

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

def main():
    parser = argparse.ArgumentParser(description="MOO19 News NFT Report Generator")
    parser.add_argument("--output-dir", type=str, default="output", help="Directory to save outputs")
    parser.add_argument("--run", action="store_true", help="Run generator")
    args, _ = parser.parse_known_args()

    episode_num, projects, term_info, intro_template, weather_text = select_weekly_rotation()
    now_str = datetime.now().strftime("%B %d, %Y")

    print(f"[*] Generating MOO19 NFT Report Episode #{episode_num} for {now_str}...")
    print(f"[*] Featured Projects: {', '.join([p['name'] for p in projects])}")
    print(f"[*] Cow-pedia Term: {term_info['term']}")

    # Setup directories (clean previous run output buffers)
    output_base = args.output_dir
    bumpers_dir = os.path.join(output_base, "bumpers")
    standalone_dir = os.path.join(output_base, "standalone_clips")
    if os.path.exists(bumpers_dir):
        shutil.rmtree(bumpers_dir)
    if os.path.exists(standalone_dir):
        shutil.rmtree(standalone_dir)
    os.makedirs(bumpers_dir, exist_ok=True)
    os.makedirs(standalone_dir, exist_ok=True)

    celeb_name = "Daisy M. (Minty) Ledger"
    science_name = "Professor Hartmut von Schnurrbart"
    weather_name = "Sunshine Innocent Nimbus"

    intro_celeb = intro_template["celeb"].format(ep=episode_num, term=term_info["term"])
    intro_science = intro_template["science"].format(ep=episode_num, term=term_info["term"])

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
    script_lines.append(f'**{celeb_name.upper()}:** "{intro_celeb}"')
    script_lines.append(f'**{science_name.upper()}:** "{intro_science}"\n')
    script_lines.append("=" * 60 + "\n")

    clip_count = 2
    bump_count = 1

    for p in projects:
        # Bumper
        script_lines.append(f"### [BUMPER {bump_count:02d}: {p['name'].upper()} INTRO BUMP (4s)]")
        script_lines.append(f"**VISUAL CUE:** Dynamic 2D graphic card displaying {p['name']} art ({p['art_description']}), floor price ({p['floor_price_eth']} ETH), and scannable QR Code linking to {p['official_url']}.")
        script_lines.append(f'**AUDIO STING & VOICEOVER:** "Up next on the NFT Report: {p["name"]}! Scan to explore!"\n')
        bump_count += 1

        # Celeb Lore Clip
        script_lines.append(f"### [CLIP {clip_count:02d}: {p['name'].upper()} - LORE & GLAM (10s Max)]")
        script_lines.append(f"**ON-SCREEN GRAPHIC:** {p['name']} | Floor: {p['floor_price_eth']} ETH | Vol: {p['volume_24h_eth']} ETH")
        script_lines.append(f'**{celeb_name.upper()}:** "{p["celeb_lore"]}"')
        script_lines.append(f'**{celeb_name.upper()}:** "Glam & Hype Rating: {p["hype_score"]}/10!"\n')
        clip_count += 1

        # Science Tech Clip
        script_lines.append(f"### [CLIP {clip_count:02d}: {p['name'].upper()} - TECH & CODE (10s Max)]")
        script_lines.append(f"**[COW-PEDIA POP-UP]:** **{term_info['term']}** — {term_info['definition']}")
        script_lines.append(f'**{science_name.upper()}:** "{p["science_tech"]}"')
        script_lines.append(f'**{science_name.upper()}:** "Code & Security Rating: {p["tech_score"]}/10!"\n')
        script_lines.append("-" * 40 + "\n")
        clip_count += 1

    # Weather Clip
    script_lines.append("### [MARKET WEATHER FORECAST (10s Max)]")
    script_lines.append(f'**{weather_name.upper()}:** "{weather_text}"\n')
    script_lines.append("=" * 60 + "\n")

    # Studio Outro
    script_lines.append("### [CLIP 13: STUDIO OUTRO & NEXT WEEK TEASER (10s Max)]")
    script_lines.append(f'**{celeb_name.upper()}:** "That wraps today\'s digital flexes! Remember: not your private keys, not your runway!"')
    script_lines.append(f'**{science_name.upper()}:** "Read the full bytecode report in The Pasture Post newsletter! Auf Wiedersehen!"')

    with open(os.path.join(output_base, "weekly_nft_report_script.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(script_lines))

    # 2. Bumpers JSON
    for idx, p in enumerate(projects, 1):
        bump_id = f"bump_{idx:03d}_{p['id']}_bump"
        bump_obj = {
            "bumper_id": bump_id,
            "project_name": p["name"],
            "chain": p["chain"],
            "floor_price_eth": p["floor_price_eth"],
            "official_url": p["official_url"],
            "art_description": p["art_description"],
            "audio_sting": "Upbeat techno cowbell crescendo with sparkling synths",
            "voiceover_script": f"Up next on MOO19 News: {p['name']}! Floor price {p['floor_price_eth']} ETH! Scan the QR code to verify on-chain!",
            "duration_seconds": 4,
            "google_flow_prompt": f"High energy broadcast motion graphics card for {p['name']}. Visual: {p['art_description']}. Floating holographic Ethereum diamond and QR code in lower third corner. Broadcast standard 16:9 4K."
        }
        with open(os.path.join(bumpers_dir, f"{bump_id}.json"), "w", encoding="utf-8") as f:
            json.dump(bump_obj, f, indent=2)

    # 3. Standalone Clips JSON
    clips_data = [
        {
            "clip_id": "clip_001_clip_01_studio_intro",
            "clip_number": 1,
            "title": "MOO19 News Studio Intro",
            "characters": [celeb_name, science_name],
            "setting": "MOO19 Broadcast Desk - Newsroom01_Large copy.jpg",
            "dialogue": [
                {"speaker": celeb_name, "line": intro_celeb},
                {"speaker": science_name, "line": intro_science}
            ],
            "camera_angle": "Wide 2-shot anchor desk view",
            "target_duration_seconds": 10,
            "google_flow_prompt": f"Dual anchor anthropomorphic cow newscasters behind sleek glass desk. {celeb_name} wearing luxury pearl necklace and pink blazer on left. {science_name} wearing white lab coat and pince-nez spectacles on right. Lip sync dialogue."
        }
    ]

    clip_seq = 2
    for p in projects:
        clips_data.append({
            "clip_id": f"clip_{clip_seq:03d}_clip_{clip_seq:02d}_{p['id']}_(celeb_lore)",
            "clip_number": clip_seq,
            "title": f"{p['name']} - Lore & Glam Review",
            "characters": [celeb_name],
            "setting": "MOO19 Anchor Desk (Anchor Left Focus)",
            "on_screen_graphic": f"{p['name']} | Floor: {p['floor_price_eth']} ETH | Vol: {p['volume_24h_eth']} ETH",
            "dialogue": [
                {"speaker": celeb_name, "line": p["celeb_lore"]},
                {"speaker": celeb_name, "line": f"Glam & Hype Rating: {p['hype_score']}/10!"}
            ],
            "camera_angle": "Medium close-up on Daisy M. Ledger with graphics overlay",
            "target_duration_seconds": 10,
            "google_flow_prompt": f"Glamorous cow anchor {celeb_name} gesturing enthusiastically toward holographic floating art display of {p['name']}. Visual art: {p['art_description']}. High fashion lighting."
        })
        clip_seq += 1

        clips_data.append({
            "clip_id": f"clip_{clip_seq:03d}_clip_{clip_seq:02d}_{p['id']}_(science_tech)",
            "clip_number": clip_seq,
            "title": f"{p['name']} - Technical & Code Audit",
            "characters": [science_name],
            "setting": "MOO19 Anchor Desk (Anchor Right Focus with Microscope)",
            "cowpedia_popup": {"term": term_info["term"], "definition": term_info["definition"]},
            "dialogue": [
                {"speaker": science_name, "line": p["science_tech"]},
                {"speaker": science_name, "line": f"Code & Security Rating: {p['tech_score']}/10!"}
            ],
            "camera_angle": "Medium close-up on Professor Hartmut adjusting brass microscope",
            "target_duration_seconds": 10,
            "google_flow_prompt": f"Professor Hartmut von Schnurrbart examining smart contract data under glowing digital microscope. Holographic Cow-pedia popup for {term_info['term']} displayed on screen."
        })
        clip_seq += 1

    clips_data.append({
        "clip_id": f"clip_{clip_seq:03d}_clip_{clip_seq:02d}_weather_forecast",
        "clip_number": clip_seq,
        "title": "Market Weather Forecast",
        "characters": [weather_name],
        "setting": "MOO19 Weather Center (Chroma Key Radar Map)",
        "dialogue": [{"speaker": weather_name, "line": weather_text}],
        "camera_angle": "Wide weather map presentation shot",
        "target_duration_seconds": 10,
        "google_flow_prompt": f"Cheerful young heifer meteorologist {weather_name} holding pointer stick in front of dynamic 3D satellite map of crypto blockchains with weather isobar fronts."
    })
    clip_seq += 1

    clips_data.append({
        "clip_id": f"clip_{clip_seq:03d}_clip_{clip_seq:02d}_studio_outro",
        "clip_number": clip_seq,
        "title": "Studio Outro & Teaser",
        "characters": [celeb_name, science_name],
        "setting": "MOO19 Broadcast Desk - Newsroom01_Large copy.jpg",
        "dialogue": [
            {"speaker": celeb_name, "line": "That wraps today's digital flexes! Remember: not your private keys, not your runway!"},
            {"speaker": science_name, "line": "Read the full bytecode report in The Pasture Post newsletter! Auf Wiedersehen!"}
        ],
        "camera_angle": "Wide studio pull-back shot with lower-third credits scrolling",
        "target_duration_seconds": 10,
        "google_flow_prompt": f"Both cow anchors smiling and waving at news desk as studio camera cranes upward showing full MOO19 television broadcast facility."
    })

    for c in clips_data:
        with open(os.path.join(standalone_dir, f"{c['clip_id']}.json"), "w", encoding="utf-8") as f:
            json.dump(c, f, indent=2)

    # 4. Google Flow Animation Manifest
    flow_manifest = {
        "production_title": f"MOO19 NFT Report - Episode #{episode_num}",
        "episode_number": episode_num,
        "air_date": now_str,
        "aspect_ratio": "16:9",
        "target_engine": "Google Flow & Veo Video Pipeline",
        "characters": [
            {"name": celeb_name, "role": "Celebrity Anchor", "voice": "Mid-Atlantic glamorous, expressive"},
            {"name": science_name, "role": "Chief Scientist", "voice": "Bavarian academic, analytical"},
            {"name": weather_name, "role": "Meteorologist", "voice": "Cheerful, upbeat, enthusiastic"}
        ],
        "timeline_sequence": []
    }

    seq_idx = 1
    flow_manifest["timeline_sequence"].append({
        "sequence_id": seq_idx,
        "type": "studio_clip",
        "ref_id": clips_data[0]["clip_id"],
        "prompt": clips_data[0]["google_flow_prompt"]
    })
    seq_idx += 1

    for idx, p in enumerate(projects, 1):
        bump_id = f"bump_{idx:03d}_{p['id']}_bump"
        flow_manifest["timeline_sequence"].append({
            "sequence_id": seq_idx,
            "type": "bumper_card",
            "ref_id": bump_id,
            "prompt": f"Motion graphics bumper for {p['name']}. Visual: {p['art_description']}. QR code and floor price {p['floor_price_eth']} ETH."
        })
        seq_idx += 1

        lore_clip = clips_data[1 + (idx - 1) * 2]
        flow_manifest["timeline_sequence"].append({
            "sequence_id": seq_idx,
            "type": "anchor_clip",
            "ref_id": lore_clip["clip_id"],
            "prompt": lore_clip["google_flow_prompt"]
        })
        seq_idx += 1

        tech_clip = clips_data[2 + (idx - 1) * 2]
        flow_manifest["timeline_sequence"].append({
            "sequence_id": seq_idx,
            "type": "anchor_clip",
            "ref_id": tech_clip["clip_id"],
            "prompt": tech_clip["google_flow_prompt"]
        })
        seq_idx += 1

    flow_manifest["timeline_sequence"].append({
        "sequence_id": seq_idx,
        "type": "weather_clip",
        "ref_id": clips_data[-2]["clip_id"],
        "prompt": clips_data[-2]["google_flow_prompt"]
    })
    seq_idx += 1

    flow_manifest["timeline_sequence"].append({
        "sequence_id": seq_idx,
        "type": "studio_outro",
        "ref_id": clips_data[-1]["clip_id"],
        "prompt": clips_data[-1]["google_flow_prompt"]
    })

    with open(os.path.join(output_base, "google_flow_animation_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(flow_manifest, f, indent=2)

    # 5. YouTube Shorts Script
    shorts_lines = [
        f"# MOO19 SHORTS: TOP 3 DIGITAL FLEXES THIS WEEK (EPISODE #{episode_num})",
        f"**Air Date:** {now_str} | **Format:** 9:16 Vertical Video (58s Total)\n",
        f"00:00 - 00:05 | Hook: {celeb_name} & {science_name} welcome viewers to this week's rapid-fire NFT Report!",
        f"00:05 - 00:20 | Segment 1: {projects[0]['name']} ({projects[0]['floor_price_eth']} ETH floor) - {projects[0]['celeb_lore']}",
        f"00:20 - 00:35 | Segment 2: {projects[1]['name']} ({projects[1]['floor_price_eth']} ETH floor) - {projects[1]['celeb_lore']}",
        f"00:35 - 00:50 | Segment 3: {projects[2]['name']} ({projects[2]['floor_price_eth']} ETH floor) - {projects[2]['science_tech']}",
        f"00:50 - 00:58 | Outro: Cow-pedia Term '{term_info['term']}' highlighted! Subscribe to MOO19 News!"
    ]
    with open(os.path.join(output_base, "weekly_nft_report_shorts_script.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(shorts_lines))

    # 6. The Pasture Post Newsletter
    nl_lines = [
        f"# The Pasture Post — Issue #{episode_num}",
        f"**Date:** {now_str}  ",
        "**From:** The Pasture Editorial Board  \n",
        "## Executive Summary",
        f"Welcome to Issue #{episode_num} of *The Pasture Post*. This week our newsroom investigated five distinct sectors of the decentralized ecosystem, evaluating both cultural momentum and contract architecture.\n",
        "## Featured Collections & Architectural Audits"
    ]
    for p in projects:
        nl_lines.extend([
            f"### {p['name']} ({p['chain']})",
            f"- **Floor Price:** {p['floor_price_eth']} ETH | **24h Volume:** {p['volume_24h_eth']} ETH",
            f"- **Contract Standard:** `{p['contract_standard']}` | **Storage Architecture:** {p['storage']}",
            f"- **Official Link:** [{p['name']} Website]({p['official_url']}) | **OpenSea:** [Marketplace Listing]({p['opensea_url']})",
            f"- **Cultural Commentary ({celeb_name}):** {p['celeb_lore']} *(Hype Rating: {p['hype_score']}/10)*",
            f"- **Technical Analysis ({science_name}):** {p['science_tech']} *(Code Rating: {p['tech_score']}/10)*\n"
        ])
    nl_lines.extend([
        f"## Cow-pedia Educational Spotlight: {term_info['term']}",
        f"> **{term_info['term']}:** {term_info['definition']}\n",
        "## Pasture Market Weather Outlook",
        f"> *\"{weather_text}\"* — {weather_name}\n",
        "---",
        "*The Pasture Post is an educational publication by MOO19 News. Not financial advice. Always verify smart contract bytecode before transacting.*"
    ])
    with open(os.path.join(output_base, "weekly_pasture_post_newsletter.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(nl_lines))

    # 7. Deliver to /clips and /bumpers in dated folders
    date_subfolder = datetime.now().strftime("%Y-%m-%d")
    target_clips_dir = os.path.join("clips", date_subfolder)
    target_bumpers_dir = os.path.join("bumpers", date_subfolder)

    try:
        if os.path.exists(target_clips_dir):
            shutil.rmtree(target_clips_dir)
        if os.path.exists(target_bumpers_dir):
            shutil.rmtree(target_bumpers_dir)
        os.makedirs(target_clips_dir, exist_ok=True)
        os.makedirs(target_bumpers_dir, exist_ok=True)

        for fname in sorted(os.listdir(standalone_dir)):
            if fname.endswith(".json"):
                shutil.copy2(os.path.join(standalone_dir, fname), os.path.join(target_clips_dir, fname))
        
        for fname in sorted(os.listdir(bumpers_dir)):
            if fname.endswith(".json"):
                shutil.copy2(os.path.join(bumpers_dir, fname), os.path.join(target_bumpers_dir, fname))
        print(f"[✓] Delivered episode JSON files to {target_clips_dir}/ and {target_bumpers_dir}/")
    except Exception as e:
        print(f"[!] Note on root delivery: {e}")

    print(f"[✓] Episode #{episode_num} generated with fresh projects: {[p['name'] for p in projects]}")

if __name__ == "__main__":
    main()
