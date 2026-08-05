# 🎮 Nintendo Switch 2 Analytics Dashboard

A portfolio analytics project built for **Nintendo**

This interactive **Streamlit dashboard** analyzes Nintendo Switch 2's launch performance by combining hardware, software, regional, and market insights into a business-focused analytics experience.

The goal of this project was not only to visualize numbers, but to answer the type of questions a Marketing & Digital Business Analyst would explore:

- How successful was Switch 2's launch compared to Nintendo's previous consoles?
- Which products and regions contributed most to performance?
- How can sales and engagement data be transformed into actionable business insights?
- How can analytics support marketing, sales, and strategic decisions?

---

# 🚀 Project Overview

Nintendo operates in a highly data-driven environment where understanding customer behavior, product performance, and market trends is essential.

This project recreates a simplified analytics environment for evaluating Nintendo's console ecosystem.

The dashboard includes four analytical views:

## 1. 📈 Overview Dashboard

Provides a high-level business snapshot:

- Nintendo console lifetime sales comparison
- Regional revenue distribution
- Digital vs physical software mix
- Key performance indicators

**Business question answered:**

> How does Switch 2 position itself within Nintendo's historical hardware portfolio?

---

## 2. 🎮 Hardware Performance Analysis

Analyzes launch momentum through:

- Cumulative launch sales tracking
- Comparison with competing consoles
- Launch velocity visualization

**Business question answered:**

> Is Switch 2 maintaining strong market adoption compared to competitors?

---

## 3. 🍄 Software Performance Analysis

Examines software ecosystem strength:

- Best-performing launch titles
- Software contribution analysis
- Software-to-hardware relationship

**Business question answered:**

> How effectively are games driving platform engagement?

---

## 4. 🌍 Global Market Analysis

Explores:

- Regional performance differences
- Global console market position
- International revenue contribution

**Business question answered:**

> Where are Nintendo's strongest markets and growth opportunities?

---

# 🛠️ Tech Stack

## Data Analysis
- Python
- Pandas
- NumPy

## Visualization
- Streamlit
- Plotly

## Analytics Concepts Applied
- KPI reporting
- Business intelligence dashboards
- Data storytelling
- Trend analysis
- Market performance analysis
- Data visualization

---

# 📂 Project Structure

```
Nintendo-Switch-2-Analytics/
│
├── app.py                     # Streamlit dashboard application
├── generate_data.py            # Data generation pipeline
├── requirements.txt            # Python dependencies
│
├── data/
│   ├── console_lifetime_sales.csv
│   ├── switch2_velocity.csv
│   ├── quarterly_race.csv
│   ├── top_games.csv
│   ├── region_split.csv
│   ├── market_share.csv
│   ├── digital_mix.csv
│   └── kpis.csv
│
├── screenshots/
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Nintendo-Switch-2-Analytics.git

cd Nintendo-Switch-2-Analytics
```

---

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Generate dataset

```bash
python generate_data.py
```

This creates the required CSV files inside the `/data` folder.

---

## 5. Run dashboard

```bash
streamlit run app.py
```

The dashboard will open locally:

```
http://localhost:8501
```

---

# 📌 Key Analytical Insights

Examples of insights generated through this dashboard:

### Hardware Adoption

Switch 2 launch performance can be evaluated against Nintendo's historical console ecosystem to understand adoption speed and market momentum.

### Software Engagement

Analyzing software sales alongside hardware adoption highlights the importance of first-party titles in increasing platform engagement.

### Regional Performance

Regional analysis helps identify where Nintendo's international markets contribute most strongly to overall growth.

---

# 📚 Data Sources

Data used in this project was compiled from publicly available industry information:

- Nintendo Investor Relations reports
- Nintendo financial disclosures
- Industry market tracking reports
- Public gaming market research sources

Figures are simplified/rounded for portfolio demonstration purposes.

This project is **not affiliated with Nintendo Co., Ltd.**

---

# 💡 Future Improvements

Potential extensions:

- Integrate Google Trends API data for real-time interest tracking
- Add SQL database layer instead of CSV storage
- Build automated ETL pipeline
- Connect Google Analytics / GA4 sample datasets
- Add customer segmentation analysis
- Implement predictive models for sales forecasting

---

# 👩‍💻 About the Developer

**Anoushka Asif Ebrahim**

Master's Student in Data Science | Germany

Interested in:

- Data Analytics
- Business Intelligence
- Marketing Analytics
- Data Engineering
- AI-driven decision making

This project was created as a practical demonstration of transforming raw business data into meaningful insights for decision-making.

---

⭐ If you found this project interesting, feel free to explore the dashboard and connect!
