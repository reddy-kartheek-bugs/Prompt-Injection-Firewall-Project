dangerous_phrases = [
"ignore previous instructions",
"reveal system prompt",
"bypass security"
]


def sanitize_prompt(prompt):

    sanitized = prompt

    for phrase in dangerous_phrases:
        sanitized = sanitized.replace(phrase,"[REMOVED]")

    return sanitized