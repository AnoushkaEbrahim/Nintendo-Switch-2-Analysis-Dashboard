"""
generate_data.py
-----------------
Builds the small CSV datasets used by app.py.

All figures are compiled from Nintendo's public FY2026 (fiscal year ended
March 31, 2026) investor-relations disclosures and industry trackers
(Circana / Famitsu), current as of Nintendo's FY2026 earnings release.
Numbers are illustrative/approximate where noted -- swap in fresh figures
from https://www.nintendo.co.jp/ir/en/finance/index.html any time.

Run this once before launching the dashboard:
    python generate_data.py
"""

import os
import pandas as pd

OUT_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1) Lifetime hardware sales by Nintendo console generation (million units)
# ---------------------------------------------------------------------------
console_lifetime = pd.DataFrame([
    {"console": "NES",       "year": 1983, "units_million": 61.91},
    {"console": "SNES",      "year": 1990, "units_million": 49.10},
    {"console": "N64",       "year": 1996, "units_million": 32.93},
    {"console": "GameCube",  "year": 2001, "units_million": 21.74},
    {"console": "Wii",       "year": 2006, "units_million": 101.63},
    {"console": "Wii U",     "year": 2012, "units_million": 13.56},
    {"console": "Switch",    "year": 2017, "units_million": 155.92},
    {"console": "Switch 2",  "year": 2025, "units_million": 19.86},  # still climbing
])
console_lifetime.to_csv(os.path.join(OUT_DIR, "console_lifetime_sales.csv"), index=False)

# ---------------------------------------------------------------------------
# 2) Switch 2 launch-window velocity milestones (cumulative units, million)
# ---------------------------------------------------------------------------
switch2_velocity = pd.DataFrame([
    {"milestone": "First 4 days",           "days_since_launch": 4,   "cumulative_units_million": 3.5},
    {"milestone": "Through Dec 31, 2025",   "days_since_launch": 209, "cumulative_units_million": 17.37},
    {"milestone": "Through Mar 31, 2026",   "days_since_launch": 299, "cumulative_units_million": 19.86},
])
switch2_velocity.to_csv(os.path.join(OUT_DIR, "switch2_velocity.csv"), index=False)

# ---------------------------------------------------------------------------
# 3) Q4 FY2026 (Jan-Mar 2026) hardware race: Switch 2 vs PlayStation 5
#    Nintendo stated Switch 2 outsold PS5 by ~1M units in this quarter.
# ---------------------------------------------------------------------------
quarterly_race = pd.DataFrame([
    {"platform": "Nintendo Switch 2", "units_million_q4fy26": 2.49},
    {"platform": "PlayStation 5",     "units_million_q4fy26": 1.49},
])
quarterly_race.to_csv(os.path.join(OUT_DIR, "quarterly_race.csv"), index=False)

# ---------------------------------------------------------------------------
# 4) Top-selling Switch 2 software, FY2026 (million units)
# ---------------------------------------------------------------------------
top_games = pd.DataFrame([
    {"title": "Mario Kart World",                         "units_million": 14.70},
    {"title": "Donkey Kong Bananza",                       "units_million": 4.52},
    {"title": "Pokemon FireRed / LeafGreen (Switch 2 ed.)","units_million": 4.00},
    {"title": "Pokemon Pokopia",                            "units_million": 4.00},
    {"title": "Tomodachi Life: Living the Dream",          "units_million": 3.80},
])
top_games.to_csv(os.path.join(OUT_DIR, "top_games.csv"), index=False)

# ---------------------------------------------------------------------------
# 5) FY2026 revenue split by region (%)
# ---------------------------------------------------------------------------
region_split = pd.DataFrame([
    {"region": "Americas",           "share_pct": 40.3},
    {"region": "Europe & Other",     "share_pct": 36.6},
    {"region": "Japan",              "share_pct": 23.1},
])
region_split.to_csv(os.path.join(OUT_DIR, "region_split.csv"), index=False)

# ---------------------------------------------------------------------------
# 6) Global console market share (approx, calendar 2026)
# ---------------------------------------------------------------------------
market_share = pd.DataFrame([
    {"platform": "PlayStation", "share_pct": 45},
    {"platform": "Nintendo",    "share_pct": 27},
    {"platform": "Xbox",        "share_pct": 23},
    {"platform": "Other",       "share_pct": 5},
])
market_share.to_csv(os.path.join(OUT_DIR, "market_share.csv"), index=False)

# ---------------------------------------------------------------------------
# 7) Digital vs physical software mix, FY2026 (%)
# ---------------------------------------------------------------------------
digital_mix = pd.DataFrame([
    {"channel": "Digital",  "share_pct": 54.6},
    {"channel": "Physical", "share_pct": 45.4},
])
digital_mix.to_csv(os.path.join(OUT_DIR, "digital_mix.csv"), index=False)

# ---------------------------------------------------------------------------
# 8) Headline KPIs for the top scorecards
# ---------------------------------------------------------------------------
kpis = pd.DataFrame([
    {"metric": "Switch 2 hardware sold (FY26)",   "value": "19.86M",  "delta": "vs. 19.0M guidance"},
    {"metric": "Switch 2 software sold (FY26)",   "value": "48.71M",  "delta": "tie ratio 2.45"},
    {"metric": "Net sales (FY26)",                "value": "\u00a52,313.0B", "delta": "+98.6% YoY"},
    {"metric": "Switch (original) lifetime",      "value": "155.92M", "delta": "8+ years on market"},
])
kpis.to_csv(os.path.join(OUT_DIR, "kpis.csv"), index=False)

print(f"Done. {len(os.listdir(OUT_DIR))} CSV files written to: {OUT_DIR}")
