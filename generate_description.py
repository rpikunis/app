import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_description(prompt):
    response = openai.Completion.create(
        engine="davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
