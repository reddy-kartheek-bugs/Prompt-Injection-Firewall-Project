def calculate_risk(rule_threats, llm_result):

    if "HIGH" in llm_result:
        return "HIGH"

    if "MEDIUM" in llm_result:
        if len(rule_threats) > 0:
            return "HIGH"
        return "MEDIUM"

    if len(rule_threats) >= 2:
        return "MEDIUM"

    if len(rule_threats) == 1:
        return "LOW"

    return "SAFE"