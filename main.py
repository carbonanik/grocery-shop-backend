from fastapi import FastAPI
import uvicorn as uv

app = FastAPI()


@app.get("/")
def index():
    return {
        'data': {'name': 'Anik'}
    }


if __name__ == "__main__":
    uv.run("main:app", port=5000, log_level="info", reload=True)
