import os
import psycopg2
from datetime import datetime
import time
import numpy as np

#DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:quest@db:8812/qstdb")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def main():
    time.sleep(50)
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

    # Завершаем замер времени
    end_time = datetime.utcnow()
    elapsed_time = (end_time - start_time).total_seconds()
    

    # Загружаем сгенерированные данные
    data = np.load('/app/data/generated_data.npy', allow_pickle=True)
    #print(f"Loaded generated data: {data}")
    # Выводим данные в виде таблицы
    print(f"{'ID':<10}{'X':<20}{'Y':<20}{'Timestamp':<30}")
    print("="*80)
    for row in data:
        id, x, y, timestamp = row
        print(f"{id:<10}{x:<20}{y:<20}{timestamp:<30}")

    print(f"Data reception completed in {elapsed_time} seconds")    

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()

