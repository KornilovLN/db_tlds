import requests
import json

# URL и запрос
url = 'http://localhost:9000/exec'
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

