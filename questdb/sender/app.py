import os
import numpy as np
import psycopg2
from datetime import datetime
import time

DATABASE_URL = os.getenv('DATABASE_URL')
CONTAINER_ID = os.getenv('HOSTNAME')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def main():
    conn = get_db_connection()
    cur = conn.cursor()

    # Загружаем сгенерированные данные
    data = np.load('/app/data/generated_data.npy', allow_pickle=True)

    start_time = time.time()  # Начало замера времени

    for i, (x, y) in enumerate(data):
        timestamp = datetime.utcnow()
        try:
            cur.execute(
                "INSERT INTO data (timestamp, container_id, x, y, counter) VALUES (%s, %s, %s, %s, %s)",
                (timestamp, CONTAINER_ID, x, y, i)
            )
            conn.commit()
        except Exception as e:
            print(f"Error inserting row {i} from container {CONTAINER_ID}: {e}")

    end_time = time.time()  # Конец замера времени
    elapsed_time = end_time - start_time
    print(f"Time taken to insert data: {elapsed_time} seconds")

    cur.execute("INSERT INTO status (flag) VALUES ('done')")
    conn.commit()
    print("Completion flag set.")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()


