from fastapi import APIRouter
from .views import login , callback

router = APIRouter()


@router.get('/login')
async def auth_login():
    return  login()

@router.get('/callback')
async def callback():
    return callback()

