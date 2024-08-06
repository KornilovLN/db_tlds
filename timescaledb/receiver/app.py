import os
import psycopg2
from datetime import datetime
import time

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def create_status_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS status (
            id SERIAL PRIMARY KEY,
            flag VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def main():
    create_status_table()  # Создаем таблицу status, если она не существует

    time.sleep(10)  # Добавляем задержку в 10 секунд
    conn = get_db_connection()
    cur = conn.cursor()

    start_time = datetime.utcnow()
    cur.execute("SELECT COUNT(*) FROM data")
    initial_count = cur.fetchone()[0]
    print(f"Initial count: {initial_count}")

    while True:
        cur.execute("SELECT COUNT(*) FROM data")
        current_count = cur.fetchone()[0]
        print(f"Received {current_count - initial_count} new rows")
        
        if current_count - initial_count >= 9999:  # Ожидаем, пока все данные будут записаны
            print("Received all expected rows.")
            break
        
        # Проверка флага завершения
        cur.execute("SELECT flag FROM status WHERE flag = 'done'")
        flag_result = cur.fetchone()
        if flag_result:
            print("Completion flag detected.")
            break
        
        time.sleep(1)  # Добавляем задержку в 1 секунду

    end_time = datetime.utcnow()
    print(f"Data reception completed in {end_time - start_time}")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
