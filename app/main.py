from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import api, root

def build_app() -> FastAPI:
    app = FastAPI()
    
    app.include_router(
        router=root.router,
        prefix="",
        tags="テスト"
    )
    
    app.include_router(
        router=api.router,
        prefix="/api"
    )

    return app

app = build_app()