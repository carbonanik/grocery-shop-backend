source venv/Scripts/activate
uvicorn main:app --host '0.0.0.0' --log-level info --reload --env-file .env