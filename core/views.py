from dotenv import load_dotenv
import openai
import os



load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")



def hello_world(q):
    try:
        if not q:
            raise ValueError("Parameter 'q' is required")
        response = {"message": "Hello World " + str(q)}
        return response
    except ValueError as e:
        error_message = "An error occurred: " + str(e)
        return {"error": error_message}




def generate_text(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Make a sentence from the following words: {prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']
