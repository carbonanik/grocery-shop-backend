import uvicorn as uv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.database import create_db_and_tables
from src.routers import category_routes, products

app = FastAPI(debug=True)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(category_routes.router)


@app.on_event("startup")
def on_startup():
    try:
        create_db_and_tables()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    uv.run("main:app", port=8000, host='0.0.0.0', log_level="info", reload=True)

# photo base url
# https://test-and-devops-environment.s3.amazonaws.com/photos/
