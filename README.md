# TSDB - во временных рядах

## Архитектура данных в TSDB

**_1. InfluxDB:_**
* Хранение данных:
     <br>InfluxDB использует временные серии, организованные по измерениям, тегам и полям.
     <br>Данные хранятся в формате "time-series",
     <br>оптимизированном для высокопроизводительных операций записи и чтения.
* Типы данных:
     <br>Поддерживает int64, float64, bool, string и временные метки.
* Управление данными:
     <br>Данные организованы в теги (индексированные) и поля (неиндексированные),
     <br>что позволяет эффективно выполнять запросы по временным диапазонам и тегам.


**_2. TimescaleDB:_**
* Хранение данных:
     <br>Расширение для PostgreSQL, которое использует гибридную архитектуру
     <br>"chunked hypertable" для горизонтального масштабирования.
* Типы данных:
     <br>Наследует типы данных PostgreSQL,
     <br>включая int16, int32, int64, float32, float64, text, timestamp и другие.
* Управление данными:
     <br>Использует индексы PostgreSQL, включая B-Tree и GiST индексы,
     <br>что обеспечивает высокую производительность для временных запросов.


**_3. QuestDB:_**
* Хранение данных:
     <br>Использует колоночную архитектуру хранения данных,
     <br>оптимизированную для быстрого чтения и записи временных рядов.
* Типы данных:
     <br>Поддерживает int16, int32, int64, float32, float64, string и временные метки.
* Управление данными:
     <br>Использует бинарные поисковые деревья и
     <br>SIMD инструкции для ускорения операций чтения и записи.

## Программы управления TSDB и интерфейсы для Python

**_1. InfluxDB:_**
* Python клиент:
     <br>influxdb-client или influxdb-python.
* Пример использования:
```
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, username='user', password='password', database='exampledb')

# Запись данных
data = [
    {
        "measurement": "temperature",
        "tags": {
            "location": "office"
        },
        "fields": {
            "value": 23.5
        },
        "time": "2024-08-05T23:00:00Z"
    }
]
client.write_points(data)

# Чтение данных
result = client.query('SELECT value FROM temperature WHERE time > now() - 1h')
print(result.raw)
```

**_2. TimescaleDB:_**
* Python клиент:
     <br> psycopg2 или SQLAlchemy.
* Пример использования:
```
import psycopg2

conn = psycopg2.connect("dbname=exampledb user=user password=password host=localhost")
cur = conn.cursor()

# Запись данных
cur.execute("INSERT INTO temperature (time, location, value) VALUES (NOW(), 'office', 23.5)")
conn.commit()

# Чтение данных
cur.execute("SELECT time, value FROM temperature WHERE time > NOW() - INTERVAL '1 hour'")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
```

**_3. QuestDB:_**
* Python клиент:
     <br> pandas и requests.
* Пример использования:
```
import pandas as pd
import requests

# Запись данных
line_protocol = "temperature,location=office value=23.5"
requests.post('http://localhost:9000/imp', data=line_protocol)

# Чтение данных
query = 'SELECT time, value FROM temperature WHERE time > now() - 3600s'
response = requests.get(f'http://localhost:9000/exp?query={query}')
data = pd.read_csv(pd.compat.StringIO(response.text))
print(data)
```  

## Резюме

**_Каждая из рассмотренных TSDB имеет свои преимущества и особенности_**

- Выбор конкретной базы данных зависит от ваших требований к:
* типам данных,
* производительности
* удобству интеграции с Python.
 
- InfluxDB и QuestDB это - простые и эффективные интерфейсы для работы с временными рядами,
- TimescaleDB предлагает мощные возможности PostgreSQL, расширенные для временных данных.