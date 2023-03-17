FROM python:3.11.2-alpine
LABEL Maintainer="CarbonAnik"

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ src/
COPY main.py main.py

EXPOSE 8000
CMD [ "python", "main.py"]