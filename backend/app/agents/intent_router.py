import json
import re
from app.services.llm_service import generate_response


def intent_router(code: str, user_query: str) -> dict:
    """
    Classifies user intent (fallback classifier).
    Hybrid rule-based routing is handled in pipeline.
    """

    model = "llama-3.3-70b-versatile"
    max_tokens = 140

    prompt = f"""
You are an AI intent classifier.

Classify the user's request into EXACTLY one of the following intents:

- analyze
- explain
- fix
- practice
- score
- full_review

Return STRICT JSON in this format:

{{
    "intent": "..."
}}

User request:
{user_query}
"""

    response = generate_response(prompt, model, max_tokens)

    # --------------------
    # JSON Fence Cleaning
    # --------------------
    response = response.strip()
    response = re.sub(r"^```json\s*", "", response, flags=re.MULTILINE)
    response = re.sub(r"^```\s*", "", response, flags=re.MULTILINE)
    response = re.sub(r"```\s*$", "", response, flags=re.MULTILINE)
    response = response.strip()

    # --------------------
    # Safe JSON Parsing
    # --------------------
    try:
        data = json.loads(response)

        intent = data.get("intent", "full_review")

        if isinstance(intent, str):
            intent = intent.strip().lower()
        else:
            intent = "full_review"

        # Safety clamp (only allow valid intents)
        allowed_intents = {
            "analyze",
            "explain",
            "fix",
            "practice",
            "score",
            "full_review"
        }

        if intent not in allowed_intents:
            intent = "full_review"

        return {"intent": intent}

    except json.JSONDecodeError:
        return {"intent": "full_review"}