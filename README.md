# Coffee Report Generator

Скрипт для обработки CSV файлов с данными о подготовке студентов к экзаменам и генерации отчетов.

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/Dankrut/coffee-report.git
cd coffee-report
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Создание тестовых данных
```bash
python setup_test_data.py
```

## 📊 Использование

```bash
# Запуск с одним файлом
python main.py --files data/sample_data.csv --report median-coffee

# Запуск с несколькими файлами
python main.py --files data/sample_data.csv data/session2.csv --report median-coffee
```

## Примеры работы

### Запуск тестов
images/тесты.png

### Покрытие кода
images/покрытие.png

### Работа с одним файлом
images/один-файл.png

### Работа с несколькими файлами
images/несколько-файлов.png

### Обработка ошибок
images/обработка-ошибок.png

## Тестирование

```bash
pytest tests/ -v
pytest tests/ --cov=src --cov-report=term-missing
```

## Структура проекта

```
coffee-report/
├── src/           # Исходный код
├── tests/         # Тесты
├── data/          # Тестовые данные
├── images/        # Скриншоты
└── main.py        # Точка входа
```