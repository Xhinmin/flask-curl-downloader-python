FROM python:3.11-slim

# 安裝 curl
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 複製程式碼
COPY . /app

# 安裝 Python 套件
RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "app.py"]