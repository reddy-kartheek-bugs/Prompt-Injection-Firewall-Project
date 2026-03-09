import plotly.graph_objects as go


def threat_radar():

    categories = [
        "Prompt Injection",
        "Jailbreak",
        "Data Exfiltration",
        "Illegal Activity"
    ]

    values = [7,5,6,8]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))

    return fig