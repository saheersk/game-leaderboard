from fastapi import FastAPI

from app.api.v1.rest.contestant import router

app = FastAPI(title="Contestant Service")

app.include_router(router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
