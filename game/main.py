from fastapi import FastAPI

from app.api.v1.rest.game import game_router
from app.api.v1.rest.game_participant import game_participant_router


app = FastAPI(title="Game Service")


app.include_router(game_router)
app.include_router(game_participant_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002, reload=True)