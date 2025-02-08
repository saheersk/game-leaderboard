FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /contestant

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 50051

CMD ["sh", "-c", "python main.py & python grpc_server.py"]
