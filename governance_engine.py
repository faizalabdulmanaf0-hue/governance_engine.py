def calculate_governance_risk(system):
    risk_score = 0

    # Rule 1 — Low model confidence
    if system["model_confidence"] < 0.70:
        risk_score += 20

    # Rule 2 — Sensitive data processing
    if system["sensitive_data"] == True:
        risk_score += 20

    # Rule 3 — Bias detected
    if system["bias_detected"] == True:
        risk_score += 20

    # Rule 4 — No human oversight
    if system["human_oversight"] == False:
        risk_score += 25

    # Rule 5 — High-impact decision
    if system["high_impact_decision"] == True:
        risk_score += 15

    # Critical governance override
    if (
        system["sensitive_data"] == True
        and system["human_oversight"] == False
        and system["high_impact_decision"] == True
    ):
        risk_score = 100

    return min(risk_score, 100)