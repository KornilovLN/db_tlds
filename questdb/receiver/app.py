import os
import psycopg2
from datetime import datetime
import time
import numpy as np

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def main():
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
        
        if current_count - initial_count >= 9999:
            print("Received all expected rows.")
            break
        
        cur.execute("SELECT flag FROM status WHERE flag = 'done'")
        flag_result = cur.fetchone()
        if flag_result:
            print("Completion flag detected.")
            break
        
        # Убираем задержку, чтобы не влиять на замер времени
        # time.sleep(1)

    end_time = datetime.utcnow()
    elapsed_time = (end_time - start_time).total_seconds()
    print(f"Data reception completed in {elapsed_time} seconds")

    # Загружаем сгенерированные данные
    data = np.load('/app/data/generated_data.npy', allow_pickle=True)
    print(f"Loaded generated data: {data}")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()

