import os
import psycopg2
from datetime import datetime

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def main():
    conn = get_db_connection()
    cur = conn.cursor()

    start_time = datetime.utcnow()
    cur.execute("SELECT COUNT(*) FROM data")
    initial_count = cur.fetchone()[0]

    while True:
        cur.execute("SELECT COUNT(*) FROM data")
        current_count = cur.fetchone()[0]
        print(f"Received {current_count - initial_count} new rows")
        time.sleep(1)
        if current_count - initial_count >= 100000:  # Ожидаем, пока все данные будут записаны
            break

    end_time = datetime.utcnow()
    print(f"Data reception completed in {end_time - start_time}")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
