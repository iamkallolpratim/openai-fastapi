from fastapi import Request, Response, status
from fastapi import APIRouter
from .views import login , callback

router = APIRouter()


@router.get('/login')
async def auth_login():
    return  login()

@router.get('/callback')
async def auth_callback(request: Request, code: str, state: str = None):
    return await  callback(request, code,state)

