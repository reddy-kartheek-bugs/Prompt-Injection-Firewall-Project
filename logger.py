from datetime import datetime

attack_log = []


def log_attack(prompt, risk):

    attack_log.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "prompt": prompt,
        "risk": risk
    })


def get_logs():
    return attack_log