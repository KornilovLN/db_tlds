FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "sleep 10 && python initdb.py && python generator.py"]

