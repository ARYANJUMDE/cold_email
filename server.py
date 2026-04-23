from flask import Flask, request, jsonify
from agents import run_researcher, run_persona_definer, run_email_writer
from judge import run_judge
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json or {}

    industry = data.get("industry")
    product = data.get("product")

    pain = run_researcher(industry, product)
    persona = run_persona_definer(industry, product, pain)
    emails = run_email_writer(industry, product, pain, persona)
    judge = run_judge(industry, product, pain, persona, emails)

    return jsonify({
        "pain_points": pain,
        "persona": persona,
        "emails": emails,
        "judge": judge
    })

app = app