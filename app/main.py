# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
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