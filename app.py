

import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------------------------
# Page config + theme
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Switch 2 Analytics | Nintendo",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

NINTENDO_RED = "#E60012"
JOYCON_RED = "#FF3C28"
JOYCON_BLUE = "#00C3E3"
INK = "#1A1A1A"
PAPER = "#FFFFFF"
CREAM = "#F7F5F2"

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"]  {{
    font-family: 'Inter', sans-serif;
}}
h1, h2, h3, .hero-title {{
    font-family: 'Baloo 2', sans-serif !important;
}}

.stApp {{
    background: {CREAM};
}}

/* Hero banner */
.hero {{
    background: linear-gradient(120deg, {NINTENDO_RED} 0%, {JOYCON_RED} 60%, {JOYCON_BLUE} 160%);
    padding: 2.2rem 2rem;
    border-radius: 22px;
    color: white;
    margin-bottom: 1.6rem;
    box-shadow: 0 10px 30px rgba(230,0,18,0.25);
}}
.hero-title {{
    font-size: 2.4rem;
    font-weight: 800;
    margin: 0;
}}
.hero-sub {{
    font-size: 1.05rem;
    opacity: 0.92;
    margin-top: 0.3rem;
}}

/* KPI cards */
div[data-testid="stMetric"] {{
    background: {PAPER};
    border: 1px solid #eee;
    border-left: 6px solid {NINTENDO_RED};
    border-radius: 16px;
    padding: 1rem 1.1rem;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
}}
div[data-testid="stMetricLabel"] {{
    font-weight: 600;
    color: #555;
}}

/* Section headers */
.section-title {{
    font-family: 'Baloo 2', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: {INK};
    margin-top: 1.6rem;
    margin-bottom: 0.4rem;
    border-bottom: 3px solid {JOYCON_BLUE};
    display: inline-block;
    padding-bottom: 2px;
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background: {INK};
}}
section[data-testid="stSidebar"] * {{
    color: #f2f2f2 !important;
}}

footer {{visibility: hidden;}}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


@st.cache_data
def load_csv(name: str) -> pd.DataFrame:
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        st.error(
            f"Missing `{name}`. Run `python generate_data.py` first to build the "
            "data/ folder, then relaunch the dashboard."
        )
        st.stop()
    return pd.read_csv(path)


console_lifetime = load_csv("console_lifetime_sales.csv")
switch2_velocity = load_csv("switch2_velocity.csv")
quarterly_race = load_csv("quarterly_race.csv")
top_games = load_csv("top_games.csv")
region_split = load_csv("region_split.csv")
market_share = load_csv("market_share.csv")
digital_mix = load_csv("digital_mix.csv")
kpis = load_csv("kpis.csv")

PLOTLY_TEMPLATE = "plotly_white"

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🎮 Dashboard Controls")
    st.caption("Nintendo Switch 2 · FY2026 Performance Review")

    view = st.radio(
        "Focus area",
        ["Overview", "Hardware Race", "Software Hits", "Global Footprint"],
        index=0,
    )

    st.divider()
    st.markdown("**About this project**")
    st.caption(
        "Built as a portfolio piece for Nintendo's (Associate) Analyst - "
        "Marketing, Sales & Digital Business role. Data compiled from "
        "Nintendo's public FY2026 investor-relations disclosures and "
        "industry trackers (Circana / Famitsu)."
    )
    st.caption("Some figures are rounded / illustrative -- refresh from "
               "Nintendo IR for production use.")

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🍄 Nintendo Switch 2 — Year One, By the Numbers</div>
        <div class="hero-sub">
            A look at how Switch 2's launch year stacks up against Nintendo's own legacy
            hardware and the current console market — FY2026 (ended March 31, 2026).
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# KPI row (always visible)
# ---------------------------------------------------------------------------
kpi_cols = st.columns(len(kpis))
for col, (_, row) in zip(kpi_cols, kpis.iterrows()):
    col.metric(row["metric"], row["value"], row["delta"])

# ---------------------------------------------------------------------------
# OVERVIEW
# ---------------------------------------------------------------------------
if view == "Overview":
    st.markdown('<div class="section-title">Console Legacy: Lifetime Hardware Sales</div>',
                unsafe_allow_html=True)
    st.caption("Switch 2 is ~10 months old and already the fastest-climbing bar on this chart.")

    fig = px.bar(
        console_lifetime.sort_values("units_million"),
        x="units_million", y="console", orientation="h",
        text="units_million",
        color="console",
        color_discrete_sequence=[JOYCON_BLUE, "#9AA5B1", "#9AA5B1", "#9AA5B1",
                                  "#9AA5B1", "#9AA5B1", NINTENDO_RED, JOYCON_RED],
        labels={"units_million": "Lifetime units sold (millions)", "console": ""},
    )
    fig.update_traces(texttemplate="%{text:.1f}M", textposition="outside")
    fig.update_layout(template=PLOTLY_TEMPLATE, showlegend=False, height=430,
                       margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Revenue by Region (FY2026)</div>',
                    unsafe_allow_html=True)
        fig_r = px.pie(region_split, names="region", values="share_pct", hole=0.55,
                        color_discrete_sequence=[NINTENDO_RED, JOYCON_BLUE, "#FFC94D"])
        fig_r.update_traces(textinfo="label+percent")
        fig_r.update_layout(template=PLOTLY_TEMPLATE, showlegend=False, height=360,
                             margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_r, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Digital vs. Physical Software</div>',
                    unsafe_allow_html=True)
        fig_d = px.pie(digital_mix, names="channel", values="share_pct", hole=0.55,
                        color_discrete_sequence=[JOYCON_BLUE, "#DADFE3"])
        fig_d.update_traces(textinfo="label+percent")
        fig_d.update_layout(template=PLOTLY_TEMPLATE, showlegend=False, height=360,
                             margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_d, use_container_width=True)

# ---------------------------------------------------------------------------
# HARDWARE RACE
# ---------------------------------------------------------------------------
elif view == "Hardware Race":
    st.markdown('<div class="section-title">Switch 2 Launch-Window Velocity</div>',
                unsafe_allow_html=True)
    st.caption("Cumulative hardware sold since the June 5, 2025 launch.")

    fig_v = px.area(
        switch2_velocity, x="days_since_launch", y="cumulative_units_million",
        markers=True,
        labels={"days_since_launch": "Days since launch",
                "cumulative_units_million": "Cumulative units (millions)"},
    )
    fig_v.update_traces(line_color=NINTENDO_RED, fillcolor="rgba(230,0,18,0.15)")
    for _, r in switch2_velocity.iterrows():
        fig_v.add_annotation(x=r["days_since_launch"], y=r["cumulative_units_million"],
                              text=f"{r['milestone']}<br><b>{r['cumulative_units_million']}M</b>",
                              showarrow=True, arrowhead=2, yshift=15)
    fig_v.update_layout(template=PLOTLY_TEMPLATE, height=420,
                         margin=dict(l=10, r=10, t=20, b=10))
    st.plotly_chart(fig_v, use_container_width=True)

    st.markdown('<div class="section-title">Q4 FY2026 Hardware Race: Switch 2 vs. PlayStation 5</div>',
                unsafe_allow_html=True)
    st.caption("Units sold to retailers, January–March 2026 quarter.")

    fig_race = px.bar(
        quarterly_race, x="platform", y="units_million_q4fy26",
        text="units_million_q4fy26", color="platform",
        color_discrete_map={"Nintendo Switch 2": NINTENDO_RED, "PlayStation 5": "#003791"},
        labels={"units_million_q4fy26": "Units sold (millions)", "platform": ""},
    )
    fig_race.update_traces(texttemplate="%{text}M", textposition="outside")
    fig_race.update_layout(template=PLOTLY_TEMPLATE, showlegend=False, height=380,
                            margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_race, use_container_width=True)

    st.info(
        "💡 Insight: Switch 2 sold ~1M more units than PS5 in the same quarter — "
        "notable given PS5 has a five-year installed-base head start.",
        icon="💡",
    )

# ---------------------------------------------------------------------------
# SOFTWARE HITS
# ---------------------------------------------------------------------------
elif view == "Software Hits":
    st.markdown('<div class="section-title">Top-Selling Switch 2 Software (FY2026)</div>',
                unsafe_allow_html=True)

    top_games_sorted = top_games.sort_values("units_million")
    fig_g = px.bar(
        top_games_sorted, x="units_million", y="title", orientation="h",
        text="units_million",
        color="units_million", color_continuous_scale=[JOYCON_BLUE, NINTENDO_RED],
        labels={"units_million": "Units sold (millions)", "title": ""},
    )
    fig_g.update_traces(texttemplate="%{text:.2f}M", textposition="outside")
    fig_g.update_layout(template=PLOTLY_TEMPLATE, coloraxis_showscale=False, height=420,
                         margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_g, use_container_width=True)

    st.info(
        "💡 Insight: Mario Kart World alone accounts for ~30% of all Switch 2 software "
        "sold in FY2026 — a launch-title attach rate few franchises can match.",
        icon="💡",
    )

    st.markdown('<div class="section-title">Software Tie Ratio</div>', unsafe_allow_html=True)
    tie_ratio = 48.71 / 19.86
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(tie_ratio, 2),
        title={"text": "Games sold per console"},
        gauge={
            "axis": {"range": [0, 5]},
            "bar": {"color": NINTENDO_RED},
            "steps": [
                {"range": [0, 1.5], "color": "#F0F0F0"},
                {"range": [1.5, 3], "color": "#FCE1E3"},
            ],
        },
    ))
    fig_gauge.update_layout(height=320, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)

# ---------------------------------------------------------------------------
# GLOBAL FOOTPRINT
# ---------------------------------------------------------------------------
elif view == "Global Footprint":
    st.markdown('<div class="section-title">Global Console Market Share</div>',
                unsafe_allow_html=True)

    fig_m = px.pie(
        market_share, names="platform", values="share_pct", hole=0.5,
        color="platform",
        color_discrete_map={"PlayStation": "#003791", "Nintendo": NINTENDO_RED,
                             "Xbox": "#107C10", "Other": "#CCCCCC"},
    )
    fig_m.update_traces(textinfo="label+percent")
    fig_m.update_layout(template=PLOTLY_TEMPLATE, height=420,
                         margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_m, use_container_width=True)

    st.markdown('<div class="section-title">Revenue Split by Region</div>',
                unsafe_allow_html=True)
    fig_r2 = px.bar(
        region_split.sort_values("share_pct"), x="share_pct", y="region", orientation="h",
        text="share_pct", color="region",
        color_discrete_sequence=[JOYCON_BLUE, "#FFC94D", NINTENDO_RED],
        labels={"share_pct": "Share of FY2026 revenue (%)", "region": ""},
    )
    fig_r2.update_traces(texttemplate="%{text}%", textposition="outside")
    fig_r2.update_layout(template=PLOTLY_TEMPLATE, showlegend=False, height=340,
                          margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_r2, use_container_width=True)

    st.info(
        "💡 Insight: Sales outside Japan make up ~77% of Switch 2 revenue — "
        "underscoring how central international marketing & localization are "
        "to Nintendo's growth.",
        icon="💡",
    )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Sources: Nintendo Co., Ltd. FY2026 Financial Results & IR briefings; "
    "Circana; Famitsu. Compiled for a job-application portfolio piece — "
    "not an official Nintendo product."
    "Made by - Anoushka Ebrahim"
)
