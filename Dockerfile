FROM python:3.11.2-alpine
LABEL Maintainer="CarbonAnik"

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ src/
COPY main.py main.py
COPY .env .env

EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--env-file", ".env"]