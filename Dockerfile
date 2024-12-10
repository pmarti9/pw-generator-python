FROM python:3.12-alpine

WORKDIR /app

RUN apk update && apk upgrade

COPY src /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    pip install --upgrade pip

CMD ["python", "main.py"]
