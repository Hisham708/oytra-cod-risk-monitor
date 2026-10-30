import streamlit as st
import pandas as pd
from pathlib import Path
from src.analysis import load_orders, add_risk_score, summarize, cohort_performance

st.set_page_config(page_title="COD Risk Monitor", page_icon="📦", layout="wide")
st.title("COD Delivery Risk Monitor")
st.caption("Oytra take-home assignment | Offline sample analysis | Customer identifiers excluded")
default_path = Path("data/orders_anonymized.csv")
uploaded = st.file_uploader("Optional: upload an anonymized CSV with the same columns", type=["csv"])
if uploaded:
    df = load_orders(uploaded)
elif default_path.exists():
    df = load_orders(default_path)
else:
    st.error("Place orders_anonymized.csv inside the data folder.")
    st.stop()

df = df[df.payment_method.eq("COD")].copy()
resolved = df[df.final_status.isin(["DELIVERED","RTO"])].copy()
if resolved.empty:
    st.warning("No delivered or RTO rows found in this file.")
    st.stop()
scored = add_risk_score(resolved)
m = summarize(df)
c1,c2,c3,c4 = st.columns(4)
c1.metric("COD orders", f"{m['orders']:,}")
c2.metric("Delivered", f"{m['delivered']:,}")
c3.metric("RTO", f"{m['rto']:,}")
c4.metric("RTO rate", f"{m['rto_rate']:.1%}")
st.divider()
left,right = st.columns(2)
with left:
    st.subheader("Outcome mix")
    st.bar_chart(pd.DataFrame({"Orders":[m["delivered"],m["rto"]]},index=["Delivered","RTO"]))
with right:
    st.subheader("Risk bands")
    st.bar_chart(scored["risk_band"].value_counts().reindex(["Low","Medium","High"],fill_value=0))
st.subheader("RTO rate by courier")
st.dataframe(cohort_performance(resolved,"courier").style.format({"rto_rate":"{:.1%}","average_order_value":"₹{:,.0f}"}),use_container_width=True)
st.subheader("RTO rate by acquisition source")
st.dataframe(cohort_performance(resolved,"utm_source").style.format({"rto_rate":"{:.1%}","average_order_value":"₹{:,.0f}"}),use_container_width=True)
st.subheader("Risk scoring logic")
st.markdown("""
This is a **transparent rule-based prioritisation score**, not a trained machine-learning model:
- Previous RTO recorded: +55
- No previous orders: +20
- Order value in the top quartile: +15
- Three or more items: +10

Low: 0–29 | Medium: 30–59 | High: 60–100. Validate the rules with operations before using them on live orders.
""")
st.subheader("Important limitations")
st.write("The sample contains historical outcomes, not live shipment events. One non-final status is excluded from the resolved-order RTO-rate denominator. Cohort differences are descriptive and do not prove that a courier, channel or customer attribute causes RTO.")
