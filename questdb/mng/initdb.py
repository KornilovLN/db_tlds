import os
from time import sleep
import psycopg2

# Получаем информацию о базе данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:quest@db:8812/qstdb")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    '''
    Инициализация базы данных.
    Создает таблицу proba, если ее нет.
    '''
    sleep(10)  # Добавляем задержку в 10 секунд
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS proba (id INT, tstamp TIMESTAMP, creater VARCHAR, x DOUBLE, y DOUBLE)")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()

