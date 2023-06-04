from fastapi import APIRouter, Query
from .views import hello_world, generate_text

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@router.get('/hello')
async def hello(q: str):
    return hello_world(q)


@router.get('/prompt')
async def prompt():
    return generate_text()
