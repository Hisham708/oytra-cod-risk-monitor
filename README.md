# COD Delivery Risk Monitor

A small, reproducible Python + Streamlit project built for the Oytra Associate Software Engineer take-home assignment.

## What is included
- `app.py`: interactive dashboard.
- `src/analysis.py`: reusable cleaning, transparent risk scoring and cohort summaries.
- `data/orders_anonymized.csv`: sample data with customer name, phone and street address removed.
- `reports/`: metrics, courier/source/state summaries and scenario assumptions.
- `business_memo.pdf`: 1–2 page business memo.
- `decision_log.md` and `ai_usage_log.md`: project decisions and AI assistance disclosure.

## Run locally (Python 3.10+)
1. Extract the ZIP.
2. Open a terminal in the extracted `oytra_cod_risk_project` folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the dashboard:
   ```bash
   python -m streamlit run app.py
   ```
5. Streamlit opens a local browser tab. If it does not, open the local URL printed in the terminal (usually `http://localhost:8501`).

## Data privacy
The original input contains personal data. It is intentionally **not** included. The provided `orders_anonymized.csv` removes customer name, phone and street address. Do not publish the original CSV or upload it to a public repository. If Oytra needs the original source file, share it only through the company's approved private channel.

## Method
Only COD orders are analyzed. RTO rate = RTO / (Delivered + RTO). Other statuses are excluded from this denominator. Status labels are normalized to uppercase. The risk score is a transparent heuristic, not a validated prediction model; see the dashboard for its components and limitations.

## Scenario estimates
The memo's recovery estimates are illustrative scenarios. They assume a 5%, 10% or 15% relative reduction in historical RTO count and use the resolved orders' average order value as a proxy. They are not profit, cash savings or guaranteed outcomes; actual economics require shipping, reverse-logistics, product-margin and contact costs.

## Suggested next step
Before any live rollout, test confirmation messages on a small randomized COD cohort, record confirmation/delivery outcomes, and compare against a control group.
