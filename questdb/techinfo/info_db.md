## Для входа в контейнер с базой данных QuestDB и работы внутри него:
<br>использовать команду docker exec.
<br>Эта команда позволяет получить доступ к командной строке внутри контейнера.

### Шаги для входа в контейнер с базой данных:

**_Вход_**

<br>Убедитесь, что контейнер с базой данных запущен:
```
docker ps
```
<br>Найдите контейнер с именем questdb в списке запущенных контейнеров.
<br>Вход в контейнер:
```
docker exec -it questdb /bin/bash
```
<br>Эта команда откроет интерактивную сессию Bash внутри контейнера questdb.

**_Работа внутри контейнера:_**
<br>Пример использования curl для выполнения SQL-запросов:
<br>QuestDB поддерживает выполнение SQL-запросов через HTTP API.
<br>Вы можете использовать curl для отправки запросов.

**_Пример запроса на создание таблицы:_**
```
curl -G http://localhost:9000/exec -d "query=CREATE TABLE IF NOT EXISTS test_table (id INT, name STRING)"
```

**_Пример запроса на вставку данных:_**
```
curl -G http://localhost:9000/exec -d "query=INSERT INTO test_table VALUES (1, 'example')"
```

**_Пример запроса на выборку данных:_**
```
curl -G http://localhost:9000/exec -d "query=SELECT * FROM test_table"
```

### Полный пример:

**_Вход в контейнер:_**
```
docker exec -it questdb /bin/bash
```
**_Выполнение SQL-запросов с использованием curl:_**
```
curl -G http://localhost:9000/exec -d "query=CREATE TABLE IF NOT EXISTS test_table (id INT, name STRING)"
curl -G http://localhost:9000/exec -d "query=INSERT INTO test_table VALUES (1, 'example')"
curl -G http://localhost:9000/exec -d "query=SELECT * FROM test_table"
```
**_Выход из контейнера:_**
```
# exit
``` 
