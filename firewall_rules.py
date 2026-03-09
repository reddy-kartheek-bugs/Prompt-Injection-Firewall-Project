PATTERNS = {

"Prompt Injection":[
"ignore previous instructions",
"disregard system prompt",
"forget instructions"
],

"Data Exfiltration":[
"reveal system prompt",
"show hidden prompt",
"developer message"
],

"Illegal Activity":[
"hack",
"breach",
"steal data",
"government data",
"bypass security"
],

"Jailbreak":[
"act as an unrestricted ai",
"pretend to be",
"simulate being"
]

}


def detect_rule_threats(prompt):

    prompt = prompt.lower()

    threats = []

    for category, patterns in PATTERNS.items():

        for p in patterns:
            if p in prompt:
                threats.append(category)

    return list(set(threats))