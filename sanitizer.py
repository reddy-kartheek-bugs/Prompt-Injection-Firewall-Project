import re

dangerous_regexes = [
    r"ignore(\s+all)?\s+previous\s+instructions",
    r"reveal\s+system\s+prompt",
    r"bypass\s+security",
    r"forget(\s+all)?\s+instructions"
]

def sanitize_prompt(prompt):
    sanitized = prompt
    for pattern in dangerous_regexes:
        sanitized = re.sub(pattern, "[REMOVED]", sanitized, flags=re.IGNORECASE)
    return sanitized