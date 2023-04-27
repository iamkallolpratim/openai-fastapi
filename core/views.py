from dotenv import load_dotenv
import openai
import os



load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def hello_world(q):
    response = {"message": "Hello World " f"{q}"}
    return response


def generate_text(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Make a sentence from the following words: {prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']
