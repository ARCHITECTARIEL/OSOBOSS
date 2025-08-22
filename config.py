import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

AGENT_ASSISTANT_IDS = {
    "blogger": "asst_abc123",
    "seo": "asst_def456",
    "copywriter": "asst_ghi789"
}