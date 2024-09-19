# Проект bank_widget

## Описание:

Проект bank - это приложение, которое показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:VeNDeTeT/Homework.git
```
## Конфигурация
1. Установите библиотеки Flake8, black, isort, mypy в группу lint.:
```
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```
## Использование:

1. Используйте код из модуля masks для получения масок номера счета и номера банковской карты по отдельности.
2. Используйте код из модуля widget для получения масок номера счета и номера банковской карты вместе и даты операции.
3. Используйте код из модуля processing для получения информации по операциям.
4. Используйте код из модуля generators для фильтрации информации по операциям.
5. Используйте код из модуля decorators для создания декоратора, который проводит логирование вызовов функции. Логирует вызов функции и её результат в файл или консоль.
6. Используйте код из модуля external_api для импорта курса валют через API
7. Используйте код из модуля utils для импорта из файла JSON информации по ранзакциям.


## Модуль masks.py:

Пример работы функции, возвращающей маску карты 7000792289606361 # входной аргумент 7000 79** **** 6361 # выход функции.

Пример работы функции, возвращающей маску счета 73654108430135874305 # входной аргумент **4305 # выход функции.

В модуль добавлен логгер, который записывает логи в файл.

# Модуль widget.py:

Пример для карты Visa Platinum 7000 7922 8960 6361 # входной аргумент Visa Platinum 7000 79** **** 6361 # выход функции.

Пример для счета Счет 73654108430135874305 # входной аргумент Счет **4305 # выход функции.

Пример для даты 2018-07-11T02:26:18.671407 # входной аргумент 11.07.2018 # выход функции.

## Модуль processing.py: 
1. Функция, которая принимает на вход список словарей и значение для ключа state (опциональный параметр со значением по умолчанию EXECUTED ) и возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
2. Функция, которая принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы по убыванию даты (ключ date ). Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).

## Модуль generators.py:
1. Функция, которая принимает список словарей с банковскими операциями (или объект-генератор, который выдает по одной банковской операции) и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
2. Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
3. Генератор номеров банковских карт, который должен генерировать номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например от 0000 0000 0000 0001 до 9999 9999 9999 9999 (диапазоны передаются как параметры генератора).

## Модуль utils:

Функция get_mask_card_number принимает на вход путь до JSON-файла с информацией о проводимых транзакциях. И возвращает список словарей.

В модуль добавлен логгер, который записывает логи в файл.

## Модуль decorators
Содержит декоратор для логирования вызовов функции сложения числе - function Логирует вызов функции и её результат в файл или консоль. Принимает необязательный аргумент filename для указания файла логирования.

## Модуль transactions_csv_and_xlsx
Модуль transactions_csv_and_xlsx содержит функции, с помощью которых осуществляется считывание данных из файлов CSV и XLSX.


## Библиотека CSV and pandas
1.Установите библиотеку

```
poetry add pandas
```

2. Для корректной работы с Excel-файлами в pandas необходимо дополнительно установить библиотеку openpyxl

```
poetry add openpyxl
```

## Тестирование:
# Для тестирования кода установите Pytest:

```
poetry add --group dev pytest
```

# Установите Code coverage для расчета процента протестированного кода:
```
poetry add --group dev pytest-cov
```

## Запуск Code coverage:
```
pytest --cov
```
# Чтобы сгенерировать отчет о покрытии в HTML-формате, используйте следующую команду:
```
pytest --cov=src --cov-report=html
```

# Для тестирования вывода в консоль используйте специальную фикстуру:
```
capsys
```
# Модуль main
Модуль main содержит функцию main, которая отвечает за основную логику проекта и связывает функциональности между собой. В модуле реализован пользовательский интерфейс по получению транзакций, а также их фильтрации.
## Пример использования
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Введите номер пункта: 1
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:
EXECUTED
Отсортировать операции по дате?  Да/Нет
да
Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
да
Выводить только рублевые тразакции? Да/Нет
да
Отфильтровать список транзакций по определенному слову в описании? Да/Нет:
да
Видите слово для поиска: открытие