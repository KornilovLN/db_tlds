### Создание таблицы в базе данных
**_Запустите контейнер PostgreSQL и создайте таблицу для хранения данных:_**
```
CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    container_id INT NOT NULL,
    x FLOAT8 NOT NULL,
    y FLOAT8 NOT NULL,
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
    container_id INT NOT NULL,
    x FLOAT8 NOT NULL,
    y FLOAT8 NOT NULL,
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