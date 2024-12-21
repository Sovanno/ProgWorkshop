# Параметризация тестов и составление наборов тестовых данных
## Выполнил Финк Э.В. группа ФИТ-222 <b>
в данной ветке представлено решение пятой лабораторной работы <b>

## Следует установить playwright, pytest и jsonschema
- pip3 install pytest-playwright
- pip3 install pytest
- pip3 install jsonschema

## Структура тестов
### Тесты поделены на две категории: Создание бронирования и Полученяи Токена
- ### Создание бронирования
- #### Проверяет создание бронирования с валидными и не валидными данными
- #### Обеспечитвает создание, удаление и обращение по ID
- ### Полкчение токена
- #### Проверяет верность сгенерированного токена
- #### Обеспечивает проверку на ошибки у не валидных данных

## Тестовые данные
### Валидное создание бронирования
```
valid_booking_data = [
    {
        "firstname": "Ялта",
        "lastname": "2007",
        "totalprice": 300000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-07"
        },
        "additionalneeds": "Breakfast"
    }
]
```

### Не валидное создание данных
```
invalid_booking_data = [
    {},
    {"firstname": None, "lastname": "БУБУБУ", "totalprice": 100, "depositpaid": True, ...},
    {"firstname": "Вито", "lastname": "Сколетте", "totalprice": None, "depositpaid": True, ...},
    ...
]
```

### Валидное получение токена
```
valid_token_data = [
    ("admin", "password123")
]
```

### Не валидное получение токена
```
invalid_token_data = [
    ("", "password123"),
    ("admin", ""),
    ("wrong_user", "wrong_pass"),
    (None, None),
    (1, 1),
    (True, False),
    ...
]
```

## Команда для запуска тестов
### pytest
