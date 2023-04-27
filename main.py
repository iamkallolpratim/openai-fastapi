from fastapi import FastAPI

from core.router import router as  core_router
from auth.router import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix='/api/v1/auth', tags=['Authentication'])
app.include_router(core_router, prefix='/api/v1', tags=['Application'])
