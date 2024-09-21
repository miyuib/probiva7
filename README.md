

### Манул на русском

---

## probiva7

`probiva7` — это библиотека Python для работы с файлами CSV, которая позволяет получать данные из локальных CSV-файлов или с Google Диска. Библиотека поддерживает гибкую настройку и форматирование результатов.

### Установка

Для установки библиотеки выполните следующую команду:

```bash
pip install probiva7
```

### Использование

#### 1. Работа с Google Диском (режим `Origin`)

Библиотека автоматически загружает файл `EYEOFGOD.csv` с Google Диска и использует его в режиме `Origin`.

```python
from probiva7 import Probiva7

probiva = Probiva7()
probiva.set_csv_origin()

result = probiva.get_result(id="ID: {id}", phone="Телефон: {phone}")
print(result)
```

#### 2. Работа с локальной базой данных (режим `Local`)

Вы можете работать с любым локальным CSV-файлом, указав путь к нему и схему (названия столбцов).

```python
from probiva7 import Probiva7

schema = ["id", "number", "Adresse"]

probiva = Probiva7()
probiva.set_csv_local("/path/to/local/csv", schema)

result = probiva.get_result(id="ID: {id}", number="Номер: {number}", Adresse="Адрес: {Adresse}")
print(result)
```

### Методы

- `set_csv_origin()` — Устанавливает режим работы с Google Диском.
- `set_csv_local(directory, schema)` — Устанавливает режим работы с локальным CSV-файлом.
- `set_directory(directory)` — Устанавливает директорию для локального CSV-файла.
- `get_result(**kwargs)` — Возвращает отформатированные результаты на основе переданных ключей и схемы.

### Зависимости

- `gdown` — Для загрузки файлов с Google Диска.

---

### Manual in English

---

## probiva7

`probiva7` is a Python library for working with CSV files, allowing you to fetch data from either local CSV files or Google Drive. The library supports flexible configuration and result formatting.

### Installation

To install the library, run the following command:

```bash
pip install probiva7
```

### Usage

#### 1. Working with Google Drive (Mode `Origin`)

The library automatically downloads the `EYEOFGOD.csv` file from Google Drive and uses it in the `Origin` mode.

```python
from probiva7 import Probiva7

probiva = Probiva7()
probiva.set_csv_origin()

result = probiva.get_result(id="ID: {id}", phone="Phone: {phone}")
print(result)
```

#### 2. Working with Local Database (Mode `Local`)

You can work with any local CSV file by specifying its path and schema (column names).

```python
from probiva7 import Probiva7

schema = ["id", "number", "Adresse"]

probiva = Probiva7()
probiva.set_csv_local("/path/to/local/csv", schema)

result = probiva.get_result(id="ID: {id}", number="Number: {number}", Adresse="Address: {Adresse}")
print(result)
```

### Methods

- `set_csv_origin()` — Sets the mode to work with Google Drive.
- `set_csv_local(directory, schema)` — Sets the mode to work with a local CSV file.
- `set_directory(directory)` — Sets the directory for the local CSV file.
- `get_result(**kwargs)` — Returns formatted results based on the provided keys and schema.

### Dependencies

- `gdown` — For downloading files from Google Drive.

---

Этот мануал объясняет основные возможности библиотеки и как её использовать. 
