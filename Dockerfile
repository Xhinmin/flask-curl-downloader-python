FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 5001

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]