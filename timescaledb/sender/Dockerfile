FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py .

CMD ["sh", "-c", "sleep 10 && python app.py"]
