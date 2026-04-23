from flask import Flask, request, jsonify
from api.agents import run_researcher, run_persona_definer, run_email_writer
from api.judge import run_judge

app = Flask(__name__)

# Home route (to avoid 404)
@app.route("/")
def home():
    return "API is running"

# Main API route
@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json or {}

    industry = data.get("industry")
    product = data.get("product")

    pain = run_researcher(industry, product)
    persona = run_persona_definer(industry, product)
    email = run_email_writer(pain, persona)
    result = run_judge(email)

    return jsonify({
        "pain": pain,
        "persona": persona,
        "email": email,
        "judge": result
    })

# 🔥 REQUIRED for Vercel
def handler(request):
    return app(request.environ, lambda *args: None)