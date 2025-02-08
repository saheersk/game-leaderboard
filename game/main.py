from fastapi import FastAPI


app = FastAPI(title="Game Service")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002, reload=True)