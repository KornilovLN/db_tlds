### Создание таблицы в базе данных
**_Запустите контейнер PostgreSQL и создайте таблицу для хранения данных:_**
```
CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    -- container_id INT NOT NULL,
    container_id VARCHAR(255) NOT NULL,
    x DOUBLE PRECISION NOT NULL,
    y DOUBLE PRECISION NOT NULL,
    counter INT NOT NULL
);
```

**_Для этого подключитесь к контейнеру PostgreSQL:_**
```
docker exec -it postgres psql -U user -d exampledb
```

**_И выполните команду создания таблицы уже в контейнере с базой:_**
```
CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    container_id VARCHAR(255) NOT NULL,
    x DOUBLE PRECISION NOT NULL,
    y DOUBLE PRECISION NOT NULL,
    counter INT NOT NULL
);
```

**_Запуск Docker Compose_**

<br>Теперь, когда все файлы созданы, запустите Docker Compose для развертывания приложений:
```
docker-compose up --build
```

**_Тестирование_**

<br>Система будет генерировать данные в течение определенного времени и
<br>записывать их в базу данных PostgreSQL.
<br>Принимающий контейнер будет периодически проверять количество полученных данных
<br>и выводить результат в консоль.

#----------------------------------------------------------------------------------

Скорость в 250 записей в секунду (или полторы) может показаться медленной для PostgreSQL в определённых случаях, особенно если рассматривать использование в высоконагруженных системах. Однако, производительность зависит от множества факторов, включая конфигурацию базы данных, аппаратные ресурсы, сложность запросов, оптимизацию индексов и другие аспекты.

Вот несколько факторов, которые могут повлиять на производительность и способы их улучшения:
1. Оптимизация настроек PostgreSQL

Параметры конфигурации PostgreSQL могут значительно повлиять на производительность. Проверьте следующие параметры в файле postgresql.conf:

* shared_buffers: Память, выделенная для кэширования данных.<br>Обычно рекомендуется 25% от общей памяти системы.
* work_mem: <br>Память, выделенная для сортировки и операций с временными таблицами.
*maintenance_work_mem: <br>Память, выделенная для операций обслуживания,<br>таких как создание индексов.
* effective_cache_size: <br>Оценка размера кеша операционной системы.

1. Индексация таблиц
    <br>Убедитесь, что у вас есть подходящие индексы на таблицах
    <br>для ускорения операций вставки и выборки данных. Например:
```
-- sql

CREATE INDEX idx_data_timestamp ON data (timestamp);
CREATE INDEX idx_data_container_id ON data (container_id);
```
3. Пакетная вставка данных
    <br>Использование пакетной вставки данных вместо вставки по одной записи
    <br>может значительно улучшить производительность.
    <br>Вот пример пакетной вставки:
```
#python

def main():
    conn = get_db_connection()
    cur = conn.cursor()
    batch_size = 1000
    data_batch = []

    for i in range(10000):
        timestamp = datetime.utcnow()
        x = np.random.rand()
        y = np.random.rand()
        data_batch.append((timestamp, CONTAINER_ID, x, y, i))

        if len(data_batch) >= batch_size:
            try:
                cur.executemany(
                    "INSERT INTO data (timestamp, container_id, x, y, counter) VALUES (%s, %s, %s, %s, %s)",
                    data_batch
                )
                conn.commit()
                print(f"Inserted batch of {len(data_batch)} rows from container {CONTAINER_ID}")
                data_batch = []
            except Exception as e:
                print(f"Error inserting batch from container {CONTAINER_ID}: {e}")

    if data_batch:
        try:
            cur.executemany(
                "INSERT INTO data (timestamp, container_id, x, y, counter) VALUES (%s, %s, %s, %s, %s)",
                data_batch
            )
            conn.commit()
            print(f"Inserted final batch of {len(data_batch)} rows from container {CONTAINER_ID}")
        except Exception as e:
            print(f"Error inserting final batch from container {CONTAINER_ID}: {e}")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
```

4. Отключение авто-коммита
    <br>Коммиты требуют дополнительных ресурсов.
    <br>Отключение авто-коммита и выполнение его вручную после пакетной вставки
    <br>может улучшить производительность:
```
python

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, autocommit=False)
```

5. Аппаратные ресурсы
    <br>бедитесь, что ваш сервер имеет достаточно ресурсов
    <br>(ЦП, память, диск) для выполнения задач.

6. Логи и отладка
    <br>Логирование может замедлять работу приложения.
    <br>Убедитесь, что вы минимизируете логирование во время интенсивных операций вставки данных.
    <br>Например, вы можете уменьшить количество выводимых в лог сообщений или использовать асинхронное логирование.

7. Подведение итогов
    <br>Для оценки производительности выполните следующие шаги:
    * Проверьте настройки PostgreSQL.
    * Используйте индексы.
    * Перейдите на пакетную вставку данных.
    * Отключите авто-коммит и выполните его вручную.
    * Убедитесь в наличии достаточных аппаратных ресурсов.
    * Минимизируйте логирование.

### Эти шаги помогут вам понять,
<br>где могут быть узкие места
<br>и как можно улучшить производительность работы с PostgreSQL.