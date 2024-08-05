import os
import time
import numpy as np
import psycopg2
from datetime import datetime

DATABASE_URL = os.getenv('DATABASE_URL')
CONTAINER_ID = int(os.getenv('HOSTNAME').split('-')[-1])  # Получаем номер контейнера из имени хоста

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def main():
    conn = get_db_connection()
    cur = conn.cursor()

    for i in range(10000):
        timestamp = datetime.utcnow()
        x = np.random.rand()
        y = np.random.rand()
        cur.execute(
            "INSERT INTO data (timestamp, container_id, x, y, counter) VALUES (%s, %s, %s, %s, %s)",
            (timestamp, CONTAINER_ID, x, y, i)
        )
        conn.commit()
        time.sleep(0.01)  # имитируем некоторую задержку

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
