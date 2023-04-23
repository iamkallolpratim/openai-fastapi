from fastapi import FastAPI
from ai import generate_text


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/calculate")
async def calculate():
    text = generate_text("I love you")
    return {"message": text}
