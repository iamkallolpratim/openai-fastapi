from fastapi import FastAPI
from core.router import router as  core_router
from auth.router import router as auth_router

import uvicorn;

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)


app = FastAPI(debug=True)


app.include_router(auth_router, prefix='/api/v1/auth', tags=['Authentication'])
app.include_router(core_router, prefix='/api/v1', tags=['Application'])
