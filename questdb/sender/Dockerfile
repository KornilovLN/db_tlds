FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Убираем CMD, чтобы приложение не запускалось автоматически
CMD ["python", "app.py"]
