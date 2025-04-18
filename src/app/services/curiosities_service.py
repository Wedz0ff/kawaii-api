import json
from openai import OpenAI
from src.app.config import Settings
from fastapi import HTTPException
from pydantic import BaseModel

settings = Settings()

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_API_URL,
)


class CuriosityRequest(BaseModel):
    theme: str | None = None


SYSTEM_PROMPT = """
You are a historical/scientific/curiosity fact API. Return JSON with:
- "title": Catchy 5-8 word headline
- "text": Detailed 150-250 word explanation covering:
  1. Origin (who/when/where)
  2. Unexpected aspects
  3. Lasting impact
Format text in 2-3 concise paragraphs.
Previously generated curiosities:
1. The invention of the printing press revolutionized knowledge sharing.
2. The discovery of penicillin saved millions of lives.
Ensure the new curiosity is unique and not similar to the above.
"""

USER_PROMPT_TEMPLATE = """
Generate one detailed curiosity about {theme} using this exact JSON structure:
{{
  "title": "",
  "text": ""
}}
Theme: {theme}
Avoid introductory phrases - start directly with facts.
"""


async def generate_curiosity(request: CuriosityRequest):
    try:
        theme = request.theme or "history, technology, japanese anime or science"
        specific_theme = f"{theme}, unique discoveries, rare events"
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": USER_PROMPT_TEMPLATE.format(theme=specific_theme),
                },
            ],
            response_format={"type": "json_object"},
            max_tokens=600,
            temperature=0.9,
            top_p=0.9,
            stream=False,
        )
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API error: {str(e)}")
