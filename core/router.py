from fastapi import APIRouter
from .views import hello_world , generate_text

router = APIRouter()


@router.get('/hello')
async def hello(q: str):
    return hello_world(q)

@router.get('/prompt')
async def prompt():
    return generate_text()

