import os
from time import sleep
import numpy as np
import psycopg2
from datetime import datetime

DATABASE_URL = os.getenv('DATABASE_URL')
#CONTAINER_ID = int(os.getenv('HOSTNAME').split('-')[-1])  # Получаем номер контейнера из имени хоста
CONTAINER_ID = os.getenv('HOSTNAME')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def main():
    sleep(10)  # Добавляем задержку в 10 секунд
    conn = get_db_connection()
    cur = conn.cursor()

    for i in range(100000):
        timestamp = datetime.utcnow()
        x = np.random.rand()
        y = np.random.rand()
        try:
            cur.execute(
                "INSERT INTO data (timestamp, container_id, x, y, counter) VALUES (%s, %s, %s, %s, %s)",
                (timestamp, CONTAINER_ID, x, y, i)
            )
            conn.commit()
            #print(f"Inserted row {i} from container {CONTAINER_ID}")
        except Exception as e:
            print(f"Error inserting row {i} from container {CONTAINER_ID}: {e}")
        #time.sleep(1.0)  # имитируем некоторую задержку

        # Установка флага завершения
    cur.execute("INSERT INTO status (flag) VALUES ('done')")
    conn.commit()
    print("Completion flag set.")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()

