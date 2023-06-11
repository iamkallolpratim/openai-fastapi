from fastapi import APIRouter, Query
from .views import hello_world, generate_text,process_url_handler

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Welcome to this fantastic app!"}

@router.post("/process_url")
async def process_urls(data:dict):
    result = await process_url_handler(data) 
    return result




@router.get('/hello')
async def hello(q: str):
    return hello_world(q)


@router.get('/prompt')
async def prompt():
    return generate_text()
