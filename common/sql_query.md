# SQL запросы

## SQL-запросы реляционных СУБД (PostgreSQL, MySQL, SQLite)

**_Создание таблицы_**
```
-- sql
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    column1 VARCHAR(100),
    column2 INTEGER,
    column3 TIMESTAMP
);
```

**_Вставка данных_**
```
-- sql

INSERT INTO table_name (column1, column2, column3)
VALUES ('value1', 123, '2024-08-05 12:00:00');
```

**_Выборка данных_**
```
sql

SELECT * FROM table_name WHERE column2 > 100;
```

**_Обновление данных_**
```
sql

UPDATE table_name
SET column1 = 'new_value'
WHERE id = 1;
```

**_Удаление данных_**
```
sql

DELETE FROM table_name WHERE id = 1;
```

**_Создание индекса_**
```
sql

CREATE INDEX idx_column2 ON table_name (column2);
```

**_Агрегатные функции_**
```
sql

SELECT COUNT(*), AVG(column2), MAX(column2)
FROM table_name
GROUP BY column1;
```

**_Объединение таблиц (JOIN)_**
```
sql

    SELECT a.column1, b.column2
    FROM table1 a
    JOIN table2 b ON a.id = b.table1_id;
```

## SQL-запросы СУБД временных рядов (TimescaleDB, QuestDB, InfluxDB)

### TimescaleDB

<br>(Надстройка над PostgreSQL, большинство стандартных SQL-запросов применимо)

**_Создание таблицы с временными рядами_**
```
-- sql
CREATE TABLE metrics (
    time TIMESTAMPTZ NOT NULL,
    device_id TEXT,
    temperature DOUBLE PRECISION
);
SELECT create_hypertable('metrics', 'time');
```

**_Вставка данных_**
```
-- sql
INSERT INTO metrics (time, device_id, temperature)
VALUES (NOW(), 'device_1', 23.5);
```

**_Агрегатные запросы_**
```
-- sql
SELECT time_bucket('1 minute', time) AS bucket,
       AVG(temperature)
FROM metrics
WHERE time > NOW() - INTERVAL '1 hour'
GROUP BY bucket;
```

**_Удаление старых данных_**
```
-- sql
SELECT drop_chunks(interval '1 month', 'metrics');
```

### QuestDB

<br>(QuestDB использует SQL с поддержкой временных рядов)

**_Создание таблицы_**
```
-- sql
CREATE TABLE metrics (
    time TIMESTAMP,
    device_id SYMBOL,
    temperature DOUBLE
) timestamp(time);
```

**_Вставка данных_**
```
-- sql
INSERT INTO metrics VALUES ('2024-08-05T12:00:00Z', 'device_1', 23.5);
```

**_Агрегатные запросы_**
```
-- sql
SELECT ts, AVG(temperature)
FROM metrics
SAMPLE BY 1m;
```

**_Фильтрация по времени_**
```
-- sql
SELECT * FROM metrics WHERE time > now() - 1h;
```

### InfluxDB

<br>(InfluxDB использует собственный язык запросов — InfluxQL)

**_Создание измерения и вставка данных_**
```
-- sql
INSERT temperature,device_id=device_1 value=23.5
```

**_Выборка данных_**
```
-- sql
SELECT * FROM temperature WHERE time > now() - 1h;
```

**_Агрегация по времени_**
```
-- sql
SELECT MEAN(value) FROM temperature
WHERE time > now() - 1h
GROUP BY time(1m);
```

**_Удаление данных_**
```
-- sql
DELETE FROM temperature WHERE time < now() - 30d;
```

**_Где найти информацию в сжатой форме:_**
```
    PostgreSQL/MySQL/SQLite
        SQL Tutorial                        https://www.sqltutorial.org/
        PostgreSQL Documentation            https://www.postgresql.org/docs/
        MySQL Documentation                 https://dev.mysql.com/doc/
        SQLite Documentation                https://www.sqlite.org/docs.html

    TimescaleDB
        TimescaleDB Documentation           https://docs.timescale.com/
        Quick Start Guide for TimescaleDB   https://docs.timescale.com/getting-started/latest/

    QuestDB
        QuestDB Documentation               QuestDB Documentation
        QuestDB SQL Reference               https://dbdb.io/db/questdb
                                            https://questdb.io/docs/

    InfluxDB
        InfluxDB Documentation              https://docs.influxdata.com/
        InfluxQL Reference                  https://docs.influxdata.com/enterprise_influxdb/v1/query_language/spec/
```
