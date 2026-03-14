import pytest
import csv
import tempfile
import os

from src.readers import read_csv_files


@pytest.fixture
def sample_csv_content():
    """Фикстура с примером CSV данных."""
    return """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
Алексей Смирнов,2024-06-02,500,4.0,14,устал,Математика
Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика"""


@pytest.fixture
def temp_csv_file(sample_csv_content):
    """Создает временный CSV файл с тестовыми данными."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.csv', delete=False) as f:
        f.write(sample_csv_content)
        temp_path = f.name
    
    yield temp_path
    
    # Очистка после теста
    os.unlink(temp_path)


def test_read_single_csv_file(temp_csv_file):
    """Тест чтения одного CSV файла."""
    data = read_csv_files([temp_csv_file])
    
    assert len(data) == 3
    assert data[0]['student'] == 'Алексей Смирнов'
    assert data[0]['coffee_spent'] == '450'
    assert data[1]['student'] == 'Алексей Смирнов'
    assert data[1]['coffee_spent'] == '500'
    assert data[2]['student'] == 'Дарья Петрова'
    assert data[2]['coffee_spent'] == '200'


def test_read_multiple_csv_files(temp_csv_file, sample_csv_content):
    """Тест чтения нескольких CSV файлов."""
    # Создаем второй файл
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.csv', delete=False) as f:
        f.write(sample_csv_content)
        second_file = f.name
    
    try:
        data = read_csv_files([temp_csv_file, second_file])
        assert len(data) == 6  # 3 + 3 записи
    finally:
        os.unlink(second_file)


def test_file_not_found():
    """Тест обработки несуществующего файла."""
    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent_file.csv"])


def test_empty_file():
    """Тест чтения пустого файла."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.csv', delete=False) as f:
        f.write("student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n")
        temp_path = f.name
    
    try:
        data = read_csv_files([temp_path])
        assert len(data) == 0
    finally:
        os.unlink(temp_path)

def test_missing_required_columns():
    """Тест обработки файла без необходимых колонок."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.csv', delete=False) as f:
        f.write("wrong_column1,wrong_column2\nvalue1,value2")
        temp_path = f.name
    
    try:
        with pytest.raises(ValueError, match="не содержит необходимых колонок"):
            read_csv_files([temp_path])
    finally:
        os.unlink(temp_path)