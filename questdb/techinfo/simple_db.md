## Как запустить контейнер с бд questdb и подключиться к ней

**_Создать из готового образа контейнер и подключиться к нему_**
```
docker run -d --name test_questdb -p 8813:8812 -p 9001:9000 questdb/questdb
docker exec -it test_questdb /bin/bash
```

Попадаем в контейнер и запускаем консоль

**_Можно зайти из браузера по хост-порту ZB:(9001)_**
```
localhost:9001
```

И там есть графическая консоль для запросов

**_Можно зайти из терминала хоста, указав порт ZB:(8813)_**
* В терминале хоста даем команду создания таблицы
```
curl -G --data-urlencode "query=CREATE TABLE proba (id INT, tstamp TIMESTAMP, creater VARCHAR, x DOUBLE, y DOUBLE) timestamp(tstamp)" http://localhost:9001/exec
```

* В терминале хоста даем команды заполнения таблицы
```
curl -G --data-urlencode "query=INSERT INTO proba VALUES (1, '2023-08-01T00:14:50.000000Z', 'owner', 125.0, 412.0)" http://localhost:9001/exec

curl -G --data-urlencode "query=INSERT INTO proba VALUES (2, '2023-08-01T00:14:50.000000Z', 'owner', 15.0, 42.0)" http://localhost:9001/exec
```

* В терминале хоста даем команды запроса
```
curl -G --data-urlencode "query=SELECT * FROM proba" http://localhost:9001/exec
```
Вывод не очень красивый


* Лучше использовать питоновский клиент
```
import requests
import json

# URL и запрос
url = 'http://localhost:9001/exec'
query = 'SELECT * FROM proba'
params = {
    'query': query,
    'format': 'json',  # Используем формат JSON для получения данных
    'header': 'false'
}

# Выполнение запроса
response = requests.get(url, params=params)
data = response.json()

# Разбор данных
columns = [col['name'] for col in data['columns']]
rows = data['dataset']

# Функция для красивого отображения данных
def print_table(headers, rows):
    # Определение ширины столбцов
    column_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]
    column_widths = [max(len(header), width) for header, width in zip(headers, column_widths)]

    # Печать заголовка
    header_row = ' | '.join(header.ljust(width) for header, width in zip(headers, column_widths))
    print(header_row)
    print('-' * len(header_row))

    # Печать данных
    for row in rows:
        print(' | '.join(str(item).ljust(width) for item, width in zip(row, column_widths)))

# Вывод таблицы
print_table(columns, rows)
```




