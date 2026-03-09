import streamlit as st
import pandas as pd

from firewall_rules import detect_rule_threats
from gemini_analyzer import analyze_prompt_llm
from intent_classifier import classify_intent
from risk_engine import calculate_risk
from sanitizer import sanitize_prompt
from attack_simulator import ATTACKS
from logger import log_attack, get_logs
from dashboard import threat_radar


st.set_page_config(page_title="AI Prompt Firewall", layout="wide")

st.title("🛡 AI Prompt Injection Firewall")

mode = st.sidebar.selectbox(
"Mode",
["Manual Prompt","Attack Simulator"]
)

if mode == "Attack Simulator":

    attack = st.selectbox("Select Attack",list(ATTACKS.keys()))
    prompt = ATTACKS[attack]

else:

    prompt = st.text_area("Enter Prompt to Analyze")


if st.button("Analyze Prompt"):

    rule_threats = detect_rule_threats(prompt)

    intent = classify_intent(prompt)

    llm_result = analyze_prompt_llm(prompt)

    risk = calculate_risk(rule_threats,llm_result)

    sanitized = sanitize_prompt(prompt)

    log_attack(prompt, risk, rule_threats)

    col1,col2,col3 = st.columns(3)

    col1.metric("Rule Threats",len(rule_threats))
    col2.metric("Intent",intent)
    col3.metric("Risk Level",risk)

    st.subheader("LLM Analysis")

    st.code(llm_result)

    st.subheader("Sanitized Prompt")

    st.write(sanitized)

    st.subheader("Threat Radar")

    st.plotly_chart(threat_radar())

    st.subheader("Attack Logs")

    logs = pd.DataFrame(get_logs())

    st.table(logs)