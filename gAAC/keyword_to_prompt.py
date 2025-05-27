# gAAC/keyword_to_prompt.py

import litellm
from dotenv import load_dotenv
from importlib import resources
import os


LLM_MODEL = "anthropic/claude-sonnet-4-20250514"
REASONING = "medium"


try:
    load_dotenv(override=True)
except FileNotFoundError:
    print("Environment file not found. Please ensure the .env file exists in the 'env' directory.")


_HERE = os.path.abspath(os.path.dirname(__file__))
_PROMPT_PATH = os.path.join(_HERE, "prompts", "keyword_to_prompt.md")

with open(_PROMPT_PATH, "r", encoding="utf-8") as f:
    prompt = f.read()


def keyword_to_prompt(keyword: str) -> str:
    """
    Convert a keyword to a prompt for the Image GenAI.

    Args:
        keyword (str): The keyword to convert.

    Returns:
        str: The prompt for the Image GenAI.
    """

    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": keyword
        }
    ]

    response = litellm.completion(
        model=LLM_MODEL,
        messages=messages,
        reasoning_effort=REASONING,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    keyword = "사과를 먹다"
    prompt = keyword_to_prompt(keyword)
    print()
    print(prompt)

