import json
import os
from datetime import datetime

LOG_FILE = "attack_logs.json"

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

attack_log = load_logs()

def log_attack(prompt, risk, threats=None):
    if threats is None:
        threats = []
    
    new_log = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "prompt": prompt,
        "risk": risk,
        "threats": threats
    }
    
    attack_log.append(new_log)
    
    try:
        with open(LOG_FILE, "w") as f:
            json.dump(attack_log, f, indent=4)
    except Exception as e:
        print(f"Error saving logs: {e}")

def get_logs():
    return attack_log