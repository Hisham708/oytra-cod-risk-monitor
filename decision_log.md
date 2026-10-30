# Decision log

1. **Scope:** Focus on COD RTO prevention because the supplied dataset has 2,018 COD rows and Delivered/RTO outcomes.
2. **Outcome denominator:** Calculate RTO rate as RTO / (Delivered + RTO). Exclude 1 other-status row(s), rather than treating an in-transit/unknown order as delivered or RTO.
3. **Label normalization:** Strip whitespace and uppercase status/payment labels so `Rto`, `RTO`, and `rto` are treated consistently.
4. **Privacy:** Exclude customer name, phone and street address from the shareable dataset and repository. Keep order-level non-identifying fields needed for analysis.
5. **Risk approach:** Use an explainable points-based heuristic instead of claiming an ML model. The dataset has historical outcomes but no explicit confirmation-response or delivery-attempt features.
6. **Risk components:** Prior RTO +55; no prior orders +20; order value at/above the resolved-order 75th percentile +15; 3+ items +10. High risk is score >=60.
7. **Business impact:** Present 5/10/15% relative RTO-reduction scenarios as illustrative, and label recovered amount as associated order value—not profit or guaranteed savings.
8. **Messaging:** Provide mock WhatsApp copy only. No live API, customer contact or message sending is implemented.
9. **Dashboard:** Use Streamlit for a quick local, reproducible interactive view with a small dependency set.
10. **Limitations:** Cohort comparisons are descriptive, not causal. Validate group sizes and operational context before taking action.
