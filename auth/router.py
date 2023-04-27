from fastapi import APIRouter
from .views import login , callback

router = APIRouter()


@router.get('/login')
async def login():
    return login()

@router.get('/callback')
async def callback():
    return callback()

