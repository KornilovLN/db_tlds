### Приложение для измерения скорости записи (сендер)
```
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

    # Вставка данных
    for i in range(10000):
        cur.execute("INSERT INTO data (column_name) VALUES (%s)", (i,))
    
    conn.commit()
    end_time = datetime.utcnow()

    print(f"Data insertion completed in {end_time - start_time}")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
```

### Приложение для измерения скорости чтения (ресивер)
```
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
    count = cur.fetchone()[0]

    end_time = datetime.utcnow()

    print(f"Data reading completed in {end_time - start_time}")
    print(f"Total rows read: {count}")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
```

### Объяснение:

**_Приложение для записи (сендер):_**

Подключается к базе данных.
Вставляет 10000 записей в таблицу data.
Измеряет время, затраченное на вставку данных.
Закрывает соединение с базой данных.

**_Приложение для чтения (ресивер):_**
    <br>Подключается к базе данных.
    <br>Считывает количество строк в таблице data.
    <br>Измеряет время, затраченное на чтение данных.
    <br>Закрывает соединение с базой данных.

**_Запуск приложений:_**
<br>Сначала запустите приложение для записи, чтобы вставить данные в базу данных:
```
python sender.py
```
<br>Затем запустите приложение для чтения, чтобы измерить скорость чтения данных:
```
python receiver.py
```

### Эти два независимых приложения позволят измерить 
    <br>производительность операций записи и чтения в базе данных отдельно,
    <br>без необходимости синхронизации между ними.