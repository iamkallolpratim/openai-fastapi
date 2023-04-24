from fastapi import FastAPI
from fastapi import FastAPI, APIRouter
from ai import generate_text


app = FastAPI()
router = APIRouter(prefix="/api/v1")


@router.get("/hello")
async def root():
    return {"message": "Hello World"}


@router.get("/calculate")
async def calculate():
    text = generate_text("I love you")
    return {"message": text}

app.include_router(router)