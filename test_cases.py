from governance_engine import calculate_governance_risk


test_cases = [
    {
        "name": "Test 1 - Low Risk AI System",
        "data": {
            "model_confidence": 0.95,
            "sensitive_data": False,
            "bias_detected": False,
            "human_oversight": True,
            "high_impact_decision": False
        },
        "expected": 0
    },

    {
        "name": "Test 2 - Low Model Confidence",
        "data": {
            "model_confidence": 0.60,
            "sensitive_data": False,
            "bias_detected": False,
            "human_oversight": True,
            "high_impact_decision": False
        },
        "expected": 20
    },

    {
        "name": "Test 3 - Sensitive Data",
        "data": {
            "model_confidence": 0.95,
            "sensitive_data": True,
            "bias_detected": False,
            "human_oversight": True,
            "high_impact_decision": False
        },
        "expected": 20
    },

    {
        "name": "Test 4 - Bias Detected",
        "data": {
            "model_confidence": 0.95,
            "sensitive_data": False,
            "bias_detected": True,
            "human_oversight": True,
            "high_impact_decision": False
        },
        "expected": 20
    },

    {
        "name": "Test 5 - No Human Oversight",
        "data": {
            "model_confidence": 0.95,
            "sensitive_data": False,
            "bias_detected": False,
            "human_oversight": False,
            "high_impact_decision": False
        },
        "expected": 25
    },

    {
        "name": "Test 6 - Multiple Risk Indicators",
        "data": {
            "model_confidence": 0.60,
            "sensitive_data": True,
            "bias_detected": True,
            "human_oversight": False,
            "high_impact_decision": False
        },
        "expected": 85
    },

    {
        "name": "Test 7 - Critical Governance Override",
        "data": {
            "model_confidence": 0.60,
            "sensitive_data": True,
            "bias_detected": True,
            "human_oversight": False,
            "high_impact_decision": True
        },
        "expected": 100
    }
]


print("=== AI GOVERNANCE RISK ENGINE TEST ===\n")

passed = 0

for test in test_cases:
    actual = calculate_governance_risk(test["data"])

    if actual == test["expected"]:
        status = "PASSED"
        passed += 1
    else:
        status = "FAILED"

    print(test["name"])
    print(f"Expected: {test['expected']}")
    print(f"Actual:   {actual}")
    print(f"Status:   {status}")
    print()


print(f"Result: {passed}/{len(test_cases)} tests passed")