FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade --no-cache-dir -r /app/requirements.txt

COPY s3.py /app/
COPY funcs.py /app/

ENTRYPOINT python3 ./s3.py