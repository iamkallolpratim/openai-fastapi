from fastapi import APIRouter
from .views import hello_world

router = APIRouter()


@router.get('/hello')
async def hello():
    return hello_world()

