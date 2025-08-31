"# ads" 
# Ads Spend Analytics Pipeline

This repo contains:
- n8n workflow for automated data ingestion
- DuckDB ingestion script
- SQL/dbt models for reporting
- Results and demo

## Setup

### Prerequisites
- Python 3.8+
- DuckDB (`pip install duckdb pandas`)
- [Optional] n8n locally (`npm install n8n -g` or Docker)
- [Optional] dbt (`pip install dbt`)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ads-spend-pipeline.git
cd ads-spend-pipeline
```

### 2. Set Up DuckDB

```bash
python ingest_ads_spend.py
```

### 3. Run SQL Models

- Using DuckDB CLI:
```sql
duckdb warehouse.duckdb
.read models/ads_spend_metrics.sql
```
- Or via dbt (if using dbt):
```bash
dbt run
```

### 4. n8n Ingestion Workflow

- Import `n8n-workflow-export.json` into your n8n instance.
- Update any credentials or file paths as necessary.

---

## Results

[See `results/ads_spend_metrics.png` for table screenshot.]

---

## Loom Video

[Loom Video Link](https://www.loom.com/share/b23237b74ccb492c91d205177a2ae325?sid=98f8c754-9c68-4f49-b54f-11fabd503bc7)

---

## Key Decisions

- Used n8n for file automation to enable scheduled ingestion.
- Chose DuckDB for fast, local analytics.
- Used simple SQL models for metrics (CAC, ROAS) as required.

---
