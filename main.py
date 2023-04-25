from fastapi import FastAPI

from core.router import router as  core_router

app = FastAPI()

app.include_router(core_router, prefix='/api/v1', tags=['Application'])
