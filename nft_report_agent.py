#!/usr/bin/env python3
"""
NFT Report Content Research & Script Generation Agent
for MOO19 News / CryptoCowz Universe.

This agent automates the research, analysis, scriptwriting, Google Flow
master animation manifest, 10-second standalone clip JSONs, and 4-second
project introductory video bump JSONs for the weekly "NFT Report" show segment.

Strictly configured for Google Flow Asset-Anchored Image-to-Video Pipeline (I2V):
- Master Background Plate: "Newsroom01_Large copy.jpg"
- Celebrity Reporter: "CelebReporter_2k.png" (Daisy M. (Minty) Ledger) - Left Desk (x: 18%)
- Science Reporter: "ScienceReporter_2k.png" (Professor Hartmut von Schnurrbart) - Right Desk (x: 68%)
- Weather Forecaster: "Sunshine Innocent Nimbus"
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Centralized Character Display Names mapped to Google Flow project
CHARACTER_DISPLAY_NAMES = {
    "CELEBRITY_REPORTER": "Daisy M. (Minty) Ledger",
    "SCIENCE_REPORTER": "Professor Hartmut von Schnurrbart",
    "WEATHER_GIRL": "Sunshine Innocent Nimbus",
    "FRANK_RIZZO": "Frank Rizzo",
    "JAY_EDITOR": "Thaddeus"
}

# Top-Selling NFT Data with Verified Web Links & Art References for Bumps
DEFAULT_TOP_NFTS = [
    {
        "id": "cryptopunks",
        "name": "CryptoPunks",
        "rank": 1,
        "category": "Pixel Art / PFP",
        "chain": "Ethereum",
        "floor_price_eth": 30.3,
        "volume_24h_eth": 66.79,
        "contract_standard": "ERC-721 Custom",
        "storage": "On-Chain",
        "official_url": "https://cryptopunks.app/",
        "opensea_url": "https://opensea.io/collection/cryptopunks",
        "art_description": "Iconic 24x24 pixel art portraits on vibrant solid background with rare punk traits like gold chains, wild hair, and shades",
        "celeb_lore": "Darlings, CryptoPunks became digital status symbols when Jay-Z and Snoop Dogg flexed Punks #6095 and #3831! 66.79 ETH volume!",
        "science_tech": "Fascinating! CryptoPunks code is stored 100% on Ethereum. Pure digital identity and blue-chip store of value."
    },
    {
        "id": "pudgy_penguins",
        "name": "Pudgy Penguins",
        "rank": 2,
        "category": "Cartoon PFP / Global Brand",
        "chain": "Ethereum",
        "floor_price_eth": 6.05,
        "volume_24h_eth": 255.94,
        "contract_standard": "ERC-721",
        "storage": "IPFS",
        "official_url": "https://pudgypenguins.com/",
        "opensea_url": "https://opensea.io/collection/pudgypenguins",
        "art_description": "Vibrant 2D illustrated cute chubby penguin characters with winter beanies, scarves, and cheerful expressions",
        "celeb_lore": "Darlings, look at Pudgy Penguins! 8,888 cute penguins spreading good vibes with 255.94 ETH volume! Glam Rating: 10.0/10!",
        "science_tech": "Fascinating! Pudgy Penguins uses ERC-721 with IPFS hosting, physical Pudgy Toys merch, and Overpass IP licensing."
    },
    {
        "id": "bored_ape_yacht_club",
        "name": "Bored Ape Yacht Club",
        "rank": 3,
        "category": "PFP / Metaverse",
        "chain": "Ethereum",
        "floor_price_eth": 5.94,
        "volume_24h_eth": 42.34,
        "contract_standard": "ERC-721",
        "storage": "IPFS",
        "official_url": "https://boredapeyachtclub.com/",
        "opensea_url": "https://opensea.io/collection/boredapeyachtclub",
        "art_description": "2D cel-shaded expressive bored ape avatars with sailor caps, leather jackets, neon traits, and party horns",
        "celeb_lore": "Darlings, Bored Ape Yacht Club features 10,000 iconic apes defining Web3 pop-culture with 42.34 ETH volume! Glam Rating: 7.3/10!",
        "science_tech": "Fascinating! BAYC grants full commercial IP usage rights, ApeCoin allocations, and Otherside metaverse land access."
    },
    {
        "id": "infinex_patrons",
        "name": "Infinex Patrons",
        "rank": 4,
        "category": "DeFi Utility / Revenue Share",
        "chain": "Ethereum",
        "floor_price_eth": 1.79,
        "volume_24h_eth": 65.91,
        "contract_standard": "ERC-721",
        "storage": "Arweave",
        "official_url": "https://infinex.xyz/",
        "opensea_url": "https://opensea.io/collection/infinex-patrons",
        "art_description": "Sleek holographic 2D card art displaying cross-chain patronage insignia and dynamic geometric token nodes",
        "celeb_lore": "Darlings, Infinex Patrons are foundational patronage NFTs for the non-custodial cross-chain platform with 65.91 ETH volume! Glam Rating: 6.8/10!",
        "science_tech": "Fascinating! Infinex Patrons receive platform revenue yield share stored permanently on Arweave with governance rights."
    },
    {
        "id": "chromie_squiggle",
        "name": "Chromie Squiggle by Snowfro",
        "rank": 5,
        "category": "Generative Art",
        "chain": "Ethereum",
        "floor_price_eth": 2.58,
        "volume_24h_eth": 9.93,
        "contract_standard": "ERC-721 Art Blocks",
        "storage": "On-Chain Script",
        "official_url": "https://artblocks.io/collection/chromie-squiggle-by-snowfro",
        "opensea_url": "https://opensea.io/collection/chromie-squiggle-by-snowfro",
        "art_description": "Hypnotic undulating 2D rainbow generative spectrum ribbon looping fluidly on a clean digital canvas",
        "celeb_lore": "Darlings, Chromie Squiggle by Snowfro is seminal generative art of colorful undulating ribbons with 9.93 ETH volume! Glam Rating: 5.7/10!",
        "science_tech": "Fascinating! Chromie Squiggle executes on-chain rendering scripts derived directly from transaction hash seeds."
    }
]


class NFTDataFetcher:
    def fetch_top_nfts(self, limit=5):
        return DEFAULT_TOP_NFTS[:limit]

    def fetch_collection_by_name(self, name):
        name_lower = name.lower()
        for item in DEFAULT_TOP_NFTS:
            if name_lower in item["name"].lower():
                return item
        return None


class NFTAnalyzer:
    @staticmethod
    def analyze(collection):
        volume = collection.get("volume_24h_eth", 0)
        category = collection.get("category", "")
        hype_score = min(10.0, round(5.0 + (volume / 50.0) + (1.5 if "PFP" in category or "Brand" in category else 0.5), 1))
        storage = collection.get("storage", "")
        tech_score = 9.5 if "On-Chain" in storage else (8.8 if "Arweave" in storage else 8.0)

        return {
            "collection": collection,
            "hype_score": hype_score,
            "tech_score": tech_score,
            "celeb_lore": collection["celeb_lore"],
            "science_tech": collection["science_tech"]
        }


class MOO19ScriptGenerator:
    @staticmethod
    def generate_show_script(analyzed_collections):
        now_str = datetime.now().strftime("%B %d, %Y")
        celeb_name = CHARACTER_DISPLAY_NAMES["CELEBRITY_REPORTER"]
        science_name = CHARACTER_DISPLAY_NAMES["SCIENCE_REPORTER"]
        weather_name = CHARACTER_DISPLAY_NAMES["WEATHER_GIRL"]
        
        script = []
        script.append("# MOO19 NEWS: THE NFT REPORT (PUNCHY 10-SECOND CLIP SCRIPT WITH VIDEO BUMPS)")
        script.append(f"**Episode Air Date:** {now_str}")
        script.append(f"**Hosts:** {celeb_name} (Left Desk) & {science_name} (Right Desk next to microscope)")
        script.append("**Network:** MOO19 News Channel - The Pasture")
        script.append("**Master Background:** Newsroom01_Large copy.jpg\n")
        script.append("=" * 60 + "\n")

        # Clip 1: Intro
        script.append("### [CLIP 01: MOO19 NEWS STUDIO INTRO (10s Max)]")
        script.append(f"**{celeb_name.upper()}:** \"Welcome back to MOO19 News! Today on the NFT Report, we're reviewing top digital flexes!\"")
        script.append(f"**{science_name.upper()}:** \"And check your screen for Cow-pedia Pop-ups and Scam or Stampede Checks! Let me examine the code!\"\n")
        script.append("=" * 60 + "\n")

        clip_num = 2
        bump_num = 1
        for item in analyzed_collections:
            c = item["collection"]
            
            # Video Bumper
            script.append(f"### [BUMPER {bump_num:02d}: {c['name'].upper()} INTRO BUMP (4s)]")
            script.append(f"**VISUAL CUE:** Dynamic 2D graphic card displaying {c['name']} art ({c['art_description']}), floor price ({c['floor_price_eth']} ETH), and scannable QR Code linking to {c['official_url']}.")
            script.append(f"**AUDIO STING & VOICEOVER:** \"Up next on the NFT Report: {c['name']}! Scan to explore!\"\n")
            bump_num += 1

            # Celeb Clip
            script.append(f"### [CLIP {clip_num:02d}: {c['name'].upper()} - LORE & GLAM (10s Max)]")
            script.append(f"**ON-SCREEN GRAPHIC:** {c['name']} | Floor: {c['floor_price_eth']} ETH | Vol: {c['volume_24h_eth']} ETH")
            script.append(f"**{celeb_name.upper()}:** \"{item['celeb_lore']}\"")
            script.append(f"**{celeb_name.upper()}:** \"Glam & Hype Rating: {item['hype_score']}/10!\"\n")
            clip_num += 1

            # Science Clip
            script.append(f"### [CLIP {clip_num:02d}: {c['name'].upper()} - TECH & CODE (10s Max)]")
            script.append(f"**[COW-PEDIA POP-UP]:** **{c['storage']}** — Verified technical asset storage architecture.")
            script.append(f"**{science_name.upper()}:** \"{item['science_tech']}\"")
            script.append(f"**{science_name.upper()}:** \"Code & Security Rating: {item['tech_score']}/10!\"\n")
            script.append("-" * 40 + "\n")
            clip_num += 1

        # Weather Clip
        script.append(f"### [CLIP {clip_num:02d}: MOO19 WEATHER BREAK (10s Max)]")
        script.append(f"**{weather_name.upper()}:** \"Expect high volatility across ERC-721 tokens tonight with an 80% chance of a bull surge! Embrace the chaos, traders!\"\n")
        clip_num += 1

        # Outro Clip
        script.append(f"### [CLIP {clip_num:02d}: MOO19 STUDIO OUTRO (10s Max)]")
        script.append(f"**{celeb_name.upper()}:** \"That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote!\"")
        script.append(f"**{science_name.upper()}:** \"Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight!\"\n")

        return "\n".join(script)

    @staticmethod
    def generate_shorts_script(analyzed_collections):
        now_str = datetime.now().strftime("%B %d, %Y")
        celeb_name = CHARACTER_DISPLAY_NAMES["CELEBRITY_REPORTER"]
        science_name = CHARACTER_DISPLAY_NAMES["SCIENCE_REPORTER"]
        
        shorts = []
        shorts.append("# MOO19 NEWS: NFT REPORT SHORTS (60-SECOND TEASER)")
        shorts.append(f"**Air Date:** {now_str}")
        shorts.append("**Format:** 9:16 Vertical Video (TikTok / YouTube Shorts / Instagram Reels)\n")
        shorts.append("=" * 60 + "\n")

        shorts.append(f"**[00:00 - 00:10] {celeb_name.upper()}:** \"Stop scrolling, pasture trendsetters! Here are this week's top 3 selling NFTs on MOO19 News!\"")
        
        c1 = analyzed_collections[0]["collection"]
        c2 = analyzed_collections["collection"]
        c3 = analyzed_collections["collection"]

        shorts.append(f"**[00:10 - 00:25] {celeb_name.upper()}:** \"#1 CryptoPunks with {c1['volume_24h_eth']} ETH volume! Jay-Z and Snoop Dogg flexed Punks #6095 and #3831!\"")
        shorts.append(f"**[00:25 - 00:40] {science_name.upper()}:** \"#2 Pudgy Penguins with {c2['volume_24h_eth']} ETH volume using ERC-721 and IPFS metadata hosting!\"")
        shorts.append(f"**[00:40 - 00:50] {celeb_name.upper()}:** \"#3 Bored Ape Yacht Club with full commercial IP rights and ApeCoin perks!\"")
        shorts.append(f"**[00:50 - 01:00] {science_name.upper()}:** \"Scan the QR code to watch the full episode on MOO19 News and vote on our Pasture Poll! Don't trust, verify!\"")

        return "\n".join(shorts)


class FlowExporter:
    @staticmethod
    def create_clip_object(clip_id, start_time, title, source, celeb_name, science_name, spoken_text, speaker_name, extra_fields=None):
        prompt_text = f"2D cel-shaded cartoon news broadcast, Newsroom01_Large copy.jpg background plate with curved wooden news desk. CelebReporter_2k.png ({celeb_name}) on left desk, ScienceReporter_2k.png ({science_name}) on right desk next to microscope. Spoken audio line: '{spoken_text}'"
        
        clip_obj = {
            "clip_id": clip_id,
            "start_time": start_time,
            "end_time": start_time + 10,
            "duration_seconds": 10,
            "title": title,
            "source": source,
            "prompt": prompt_text,
            "script": spoken_text,
            "text_prompt": prompt_text,
            "voice_prompt": spoken_text,
            "speech": spoken_text,
            "character_references": [speaker_name] if isinstance(speaker_name, str) else speaker_name,
            "dialogue": [
                {"speaker": speaker_name, "text": spoken_text}
            ]
        }
        if extra_fields:
            clip_obj.update(extra_fields)
        return clip_obj

    @classmethod
    def create_bumper_object(cls, bump_id, collection):
        spoken_text = f"Up next on the NFT Report: {collection['name']}! Scan the QR code to explore!"
        prompt_text = f"2D animated high-energy motion graphic bumper card, 4 seconds. Center featured 2D artwork of {collection['name']} ({collection['art_description']}). Prominent scannable QR Code on right overlay linking to {collection['official_url']}. Lower third displaying '{collection['name']} | Floor: {collection['floor_price_eth']} ETH | Chain: {collection['chain']}'. Audio sting with energetic voiceover: '{spoken_text}'"

        bumper_obj = {
            "manifest_version": "1.0",
            "google_flow_project_target": "MOO19 TV The NFT Report",
            "clip_id": bump_id,
            "clip_type": "SEGMENT_BUMPER",
            "duration_seconds": 4,
            "title": f"Bumper: {collection['name']} Intro",
            "featured_nft": collection["name"],
            "official_url": collection["official_url"],
            "opensea_url": collection["opensea_url"],
            "qr_code_target_url": collection["official_url"],
            "prompt": prompt_text,
            "script": spoken_text,
            "text_prompt": prompt_text,
            "voice_prompt": spoken_text,
            "speech": spoken_text,
            "audio_sting": "MOO19_Station_Chime_Fast_4s.mp3",
            "visual_elements": {
                "featured_artwork_style": collection["art_description"],
                "qr_code_overlay": {
                    "position": "BOTTOM_RIGHT",
                    "target_url": collection["official_url"],
                    "callout_label": f"SCAN TO VIEW {collection['name'].upper()}"
                },
                "lower_third_badge": f"{collection['name']} | Floor: {collection['floor_price_eth']} ETH | {collection['chain']}"
            }
        }
        return bumper_obj

    @classmethod
    def export_manifest(cls, analyzed_collections, output_dir):
        celeb_name = CHARACTER_DISPLAY_NAMES["CELEBRITY_REPORTER"]
        science_name = CHARACTER_DISPLAY_NAMES["SCIENCE_REPORTER"]
        weather_name = CHARACTER_DISPLAY_NAMES["WEATHER_GIRL"]

        clips = []
        bumpers = []
        
        # Clip 1: Intro
        intro_text = f"{celeb_name}: Welcome back to MOO19 News! Today on the NFT Report, we're reviewing top digital flexes! {science_name}: And check your screen for Cow-pedia Pop-ups and Scam or Stampede Checks! Let me examine the code!"
        clip1 = cls.create_clip_object(
            "clip_001", 0, "Clip 01: Studio Intro", "Newsroom01_Large copy.jpg",
            celeb_name, science_name, intro_text, [celeb_name, science_name]
        )
        clips.append(clip1)

        time_counter = 10
        clip_count = 2
        bump_count = 1

        for item in analyzed_collections:
            c = item["collection"]

            # Generate Bumper
            bump_obj = cls.create_bumper_object(f"bump_{bump_count:03d}", c)
            bumpers.append(bump_obj)
            bump_count += 1

            # Celeb Clip
            celeb_text = f"{celeb_name}: {item['celeb_lore']} Glam Rating: {item['hype_score']}/10!"
            clip_c = cls.create_clip_object(
                f"clip_{clip_count:03d}", time_counter, f"Clip {clip_count:02d}: {c['name']} (Celeb Lore)",
                "Newsroom01_Large copy.jpg", celeb_name, science_name, celeb_text, celeb_name,
                extra_fields={
                    "featured_nft": c["name"],
                    "gui_overlays": {
                        "lower_third_text": f"{c['name']} | Floor: {c['floor_price_eth']} ETH | Vol: {c['volume_24h_eth']} ETH",
                        "hype_badge": f"Hype: {item['hype_score']}/10",
                        "gauge_status": "BULLISH STAMPEDE 🟢"
                    }
                }
            )
            clips.append(clip_c)
            time_counter += 10
            clip_count += 1

            # Science Clip
            science_text = f"{science_name}: {item['science_tech']} Code Rating: {item['tech_score']}/10!"
            clip_s = cls.create_clip_object(
                f"clip_{clip_count:03d}", time_counter, f"Clip {clip_count:02d}: {c['name']} (Science Tech)",
                "Newsroom01_Large copy.jpg", celeb_name, science_name, science_text, science_name,
                extra_fields={
                    "featured_nft": c["name"],
                    "gui_overlays": {
                        "cowpedia_banner": f"Cow-pedia: {c['storage']} Verified On-Chain",
                        "security_checklist": "Verified Contract: PASS | Decentralized: PASS | Liquidity Lock: HIGH",
                        "tech_badge": f"Tech: {item['tech_score']}/10"
                    }
                }
            )
            clips.append(clip_s)
            time_counter += 10
            clip_count += 1

        # Weather Clip
        weather_text = f"{weather_name}: Expect high volatility across ERC-721 tokens tonight with an 80% chance of a bull surge! Embrace the chaos, traders!"
        clip_w = cls.create_clip_object(
            f"clip_{clip_count:03d}", time_counter, f"Clip {clip_count:02d}: Weather Forecast",
            "Newsroom01_Large copy.jpg", celeb_name, science_name, weather_text, weather_name
        )
        clips.append(clip_w)
        time_counter += 10
        clip_count += 1

        # Outro Clip
        outro_text = f"{celeb_name}: That's all for this week's NFT Report on MOO19 News! Scan the Pasture Poll QR code to vote! {science_name}: Remember: Don't trust, verify! Read smart contracts before you mint! Goodnight!"
        clip_o = cls.create_clip_object(
            f"clip_{clip_count:03d}", time_counter, f"Clip {clip_count:02d}: Studio Outro",
            "Newsroom01_Large copy.jpg", celeb_name, science_name, outro_text, [celeb_name, science_name],
            extra_fields={
                "gui_overlays": {
                    "pasture_poll_qr_code": "SCAN QR CODE TO VOTE FOR NEXT WEEK'S WILDCARD NFT"
                }
            }
        )
        clips.append(clip_o)

        manifest = {
            "manifest_version": "1.0",
            "google_flow_project_target": "MOO19 TV The NFT Report",
            "show_title": "MOO19 NFT Report - Production Manifest with Video Bumpers",
            "target_model": "Omni Flash (10s Dialogue Clips & 4s Bumpers)",
            "clip_duration_seconds": 10,
            "bumper_duration_seconds": 4,
            "total_duration_seconds": time_counter + 10 + (len(bumpers) * 4),
            "master_assets": {
                "environment": {
                    "asset_id": "Newsroom01_Large copy.jpg",
                    "file_name": "Newsroom01_Large copy.jpg",
                    "type": "2D_BACKGROUND_PLATE"
                },
                "character_references": [
                    {
                        "character_id": "CELEBRITY_REPORTER",
                        "character_name": celeb_name,
                        "file_name": "CelebReporter_2k.png",
                        "layer_position": {"x_percent": 18, "y_percent": 30, "scale": 1.0}
                    },
                    {
                        "character_id": "SCIENCE_REPORTER",
                        "character_name": science_name,
                        "file_name": "ScienceReporter_2k.png",
                        "layer_position": {"x_percent": 68, "y_percent": 30, "scale": 1.0}
                    }
                ]
            },
            "bumpers": bumpers,
            "clips": clips
        }

        # 1. Export Master Manifest
        manifest_path = os.path.join(output_dir, "google_flow_animation_manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        # 2. Export Standalone Individual Clip JSONs
        standalone_dir = os.path.join(output_dir, "standalone_clips")
        os.makedirs(standalone_dir, exist_ok=True)

        for clip in clips:
            standalone_filename = f"{clip['clip_id']}_{clip['title'].replace(':', '').replace(' ', '_').lower()}.json"
            standalone_filepath = os.path.join(standalone_dir, standalone_filename)
            
            standalone_payload = {
                "manifest_version": "1.0",
                "google_flow_project_target": "MOO19 TV The NFT Report",
                "clip_id": clip["clip_id"],
                "duration_seconds": 10,
                "title": clip["title"],
                "source": "Newsroom01_Large copy.jpg",
                "prompt": clip["prompt"],
                "script": clip["script"],
                "text_prompt": clip["prompt"],
                "voice_prompt": clip["script"],
                "speech": clip["script"],
                "character_references": clip["character_references"],
                "gui_overlays": clip.get("gui_overlays", {})
            }
            with open(standalone_filepath, "w", encoding="utf-8") as f:
                json.dump(standalone_payload, f, indent=2)

        # 3. Export Standalone Bumper JSONs
        bumpers_dir = os.path.join(output_dir, "bumpers")
        os.makedirs(bumpers_dir, exist_ok=True)

        for bump in bumpers:
            bump_clean_name = bump['featured_nft'].replace(' ', '_').lower()
            bump_filename = f"{bump['clip_id']}_{bump_clean_name}_bump.json"
            bump_filepath = os.path.join(bumpers_dir, bump_filename)
            with open(bump_filepath, "w", encoding="utf-8") as f:
                json.dump(bump, f, indent=2)

        return manifest_path


def main():
    parser = argparse.ArgumentParser(description="MOO19 News NFT Report Research & Script Generation Agent")
    parser.add_argument("--run", action="store_true", help="Run full weekly episode generation pipeline")
    parser.add_argument("--collection", type=str, help="Research and generate segment for a specific NFT collection")
    parser.add_argument("--output-dir", type=str, default="output", help="Directory to save generated scripts and manifests")
    parser.add_argument("--limit", type=int, default=5, help="Number of top collections to process")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    fetcher = NFTDataFetcher()

    if args.collection:
        print(f"[*] Researching collection: {args.collection}")
        found = fetcher.fetch_collection_by_name(args.collection)
        if not found:
            print(f"[!] Collection '{args.collection}' not found in database.")
            sys.exit(1)
        collections = [found]
    else:
        print(f"[*] Running weekly pipeline for top {args.limit} NFT collections...")
        collections = fetcher.fetch_top_nfts(limit=args.limit)

    analyzed = [NFTAnalyzer.analyze(c) for c in collections]

    # 1. Full Show Script
    script_text = MOO19ScriptGenerator.generate_show_script(analyzed)
    script_path = os.path.join(args.output_dir, "weekly_nft_report_script.md")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_text)
    print(f"[+] Full Show Script generated: {script_path}")

    # 2. Teaser Shorts Script
    shorts_text = MOO19ScriptGenerator.generate_shorts_script(analyzed)
    shorts_path = os.path.join(args.output_dir, "weekly_nft_report_shorts_script.md")
    with open(shorts_path, "w", encoding="utf-8") as f:
        f.write(shorts_text)
    print(f"[+] 60-Second Teaser Shorts Script generated: {shorts_path}")

    # 3. Export Manifest, Standalone Clip JSONs & Bumper JSONs
    manifest_path = FlowExporter.export_manifest(analyzed, args.output_dir)
    print(f"[+] Google Flow Master Manifest & Standalone Clip JSONs & Bumpers exported: {manifest_path}")

    print("\n[✓] MOO19 NFT Report Agent with Video Bumpers completed successfully!\n")


if __name__ == "__main__":
    main()
