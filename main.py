import uvicorn as uv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.database import create_db_and_tables
from src.apis.public import public_router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(public_router)

@app.on_event("startup")
def on_startup():
    a = os.getenv('TEST_ENV')
    print(a)
    try:
        create_db_and_tables()
    except Exception as e:
        print(e)


# if __name__ == "__main__":
    # uv.run("main:app", port=8000, host='0.0.0.0', log_level="info", reload=True)

# photo base url
# https://test-and-devops-environment.s3.amazonaws.com/photos/
