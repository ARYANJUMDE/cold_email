from google import genai
import json
import os
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def clean_json(text):
    text = text.strip()

    if "```" in text:
        text = text.split("```")[1]

    if text.startswith("json"):
        text = text[4:].strip()

    return text


def run_judge(industry, product, pain_points, persona, emails, log_step=None):
    if log_step:
        log_step("Judge: using Gemini (correct format)")

    prompt = f"""
Evaluate this cold email campaign.

Return ONLY valid JSON in this EXACT format:

{{
  "scores": {{
    "pain_point_accuracy": {{"score": 1, "reasoning": "..."}},
    "persona_fit": {{"score": 1, "reasoning": "..."}},
    "personalization": {{"score": 1, "reasoning": "..."}},
    "clarity": {{"score": 1, "reasoning": "..."}},
    "cta_strength": {{"score": 1, "reasoning": "..."}}
  }},
  "overall_score": 1,
  "summary": "...",
  "top_strength": "...",
  "top_improvement": "..."
}}

Industry: {industry}
Product: {product}

Emails:
{emails}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        raw = response.text
        clean = clean_json(raw)

        result = json.loads(clean)
        return result

    except Exception as e:
        if log_step:
            log_step("Gemini failed, using fallback")

        return {
            "overall_score": 3,
            "summary": "Fallback result",
            "top_strength": "Basic structure",
            "top_improvement": "Needs improvement",
            "scores": {
                "pain_point_accuracy": {"score": 3, "reasoning": ""},
                "persona_fit": {"score": 2, "reasoning": ""},
                "personalization": {"score": 3, "reasoning": ""},
                "clarity": {"score": 3, "reasoning": ""},
                "cta_strength": {"score": 3, "reasoning": ""}
            }
        }


