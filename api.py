from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from firewall_rules import detect_rule_threats
from gemini_analyzer import analyze_prompt_llm
from intent_classifier import classify_intent
from risk_engine import calculate_risk
from sanitizer import sanitize_prompt
from logger import log_attack, get_logs

app = FastAPI(title="AI Prompt Firewall API")

# Add CORS middleware to allow React frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/analyze")
def analyze(request: PromptRequest):
    prompt = request.prompt
    
    rule_threats = detect_rule_threats(prompt)
    intent = classify_intent(prompt)
    llm_result = analyze_prompt_llm(prompt)
    risk = calculate_risk(rule_threats, llm_result)
    sanitized = sanitize_prompt(prompt)
    
    log_attack(prompt, risk, rule_threats)
    
    return {
        "rule_threats": rule_threats,
        "intent": intent,
        "llm_result": llm_result,
        "risk_level": risk,
        "sanitized_prompt": sanitized
    }

@app.get("/logs")
def logs():
    return get_logs()

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
