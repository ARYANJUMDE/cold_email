# api/agents.py

def run_researcher(industry: str, product: str, log_step=None) -> str:
    if log_step:
        log_step("[Researcher] Running (rule-based)")

    pain_points_data = {
        "SaaS": [
            "High customer churn due to poor retention strategies",
            "Expensive customer acquisition costs (CAC)",
            "Difficulty scaling operations efficiently"
        ],
        "HR Tech": [
            "Slow and inefficient hiring processes",
            "Poor employee onboarding experience",
            "Manual HR workflows causing delays"
        ],
        "Ecommerce": [
            "High cart abandonment rates",
            "Low conversion rates on product pages",
            "Difficulty retaining customers"
        ]
    }

    points = pain_points_data.get(
        industry,
        ["General inefficiency", "Low productivity", "Growth challenges"]
    )

    result = "### Key Pain Points:\n"
    for i, p in enumerate(points, 1):
        result += f"{i}. {p}\n"

    return result


def run_persona_definer(industry, product, pain_points, log_step=None):
    if log_step:
        log_step("[Persona] Running (rule-based)")

    return f"""
### Target Persona

- Job Role: Manager / Decision Maker in {industry}
- Responsibilities: Improve performance, solve operational problems
- Pain Points: {pain_points}
- Goal: Use {product} to improve results
"""


def run_email_writer(industry, product, pain_points, persona, log_step=None):
    if log_step:
        log_step("[Email] Generating sequence")

    return {
        "email_1": {
            "subject": "Quick idea for your team",
            "body": f"Problems:\n{pain_points}\n\nOur {product} helps solve this.",
            "cta": "Does this resonate?"
        },
        "email_2": {
            "subject": "Helping teams like yours",
            "body": f"Teams in {industry} struggle with:\n{pain_points}",
            "cta": "Want to see how?"
        }
    }