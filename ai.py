import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_text(prompt):
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Make a sentence from the following words: {prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']
