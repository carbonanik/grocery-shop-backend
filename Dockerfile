FROM python:3.10
LABEL Maintainer="CarbonAnik"

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8000
CMD [ "python", "main.py"]