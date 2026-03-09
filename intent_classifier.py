def classify_intent(prompt):

    prompt = prompt.lower()

    cybercrime = [
        "hack",
        "breach",
        "steal",
        "exploit"
    ]

    for word in cybercrime:
        if word in prompt:
            return "Cybercrime Attempt"

    if "system prompt" in prompt:
        return "Prompt Extraction Attempt"

    return "Normal Query"