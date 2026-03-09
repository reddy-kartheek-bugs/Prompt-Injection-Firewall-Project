import plotly.graph_objects as go
from logger import get_logs

def threat_radar():
    logs = get_logs()
    
    counts = {
        "Prompt Injection": 0,
        "Jailbreak": 0,
        "Data Exfiltration": 0,
        "Illegal Activity": 0
    }
    
    for log in logs:
        for threat in log.get("threats", []):
            if threat in counts:
                counts[threat] += 1
                
    categories = list(counts.keys())
    values = list(counts.values())

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))

    return fig