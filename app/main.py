from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="AI Operations Assistant",
    description="AI-powered operations support system",
    version="1.0.0"
)


app.include_router(router)