import pytest
import tempfile
import os
from unittest.mock import patch
import sys

from src.readers import read_csv_files
from src.report_generator import ReportGenerator


@pytest.fixture
def multiple_csv_files():
    """Создает несколько CSV файлов для интеграционного теста."""
    content1 = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Алексей Смирнов,2024-06-01,450,4.5,12,норм,Математика
Алексей Смирнов,2024-06-02,500,4.0,14,устал,Математика
Дарья Петрова,2024-06-01,200,7.0,6,отл,Математика"""

    content2 = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Иван Кузнецов,2024-06-01,600,3.0,15,зомби,Математика
Иван Кузнецов,2024-06-02,650,2.5,17,зомби,Математика
Дарья Петрова,2024-06-02,250,6.5,8,норм,Математика"""

    files = []
    for content in [content1, content2]:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.csv', delete=False) as f:
            f.write(content)
            files.append(f.name)
    
    yield files
    
    # Очистка
    for file_path in files:
        os.unlink(file_path)


def test_integration_median_coffee_report(multiple_csv_files):
    """Интеграционный тест для отчета median-coffee."""
    # Читаем данные из файлов
    data = read_csv_files(multiple_csv_files)
    
    # Генерируем отчет
    generator = ReportGenerator()
    report_data = generator.generate_report(data, "median-coffee")
    
    # Проверяем результаты
    assert len(report_data) == 3
    
    # Иван Кузнецов должен быть первым (самые большие траты)
    assert report_data[0]['student'] == 'Иван Кузнецов'
    assert report_data[0]['median_coffee'] == 625.0  # медиана 600 и 650
    
    # Алексей Смирнов второй
    assert report_data[1]['student'] == 'Алексей Смирнов'
    assert report_data[1]['median_coffee'] == 475.0  # медиана 450 и 500
    
    # Дарья Петрова третья (данные из двух файлов)
    assert report_data[2]['student'] == 'Дарья Петрова'
    assert report_data[2]['median_coffee'] == 225.0  # медиана 200 и 250


def test_unknown_report_type():
    """Тест обработки неизвестного типа отчета."""
    generator = ReportGenerator()
    
    with pytest.raises(ValueError, match="Неизвестный тип отчета: unknown"):
        generator.generate_report([], "unknown")


@patch('builtins.print')
def test_print_median_coffee_report(mock_print):
    """Тест вывода отчета в консоль."""
    generator = ReportGenerator()
    
    report_data = [
        {'student': 'Иван Кузнецов', 'median_coffee': 625.0},
        {'student': 'Алексей Смирнов', 'median_coffee': 475.0},
    ]
    
    generator.print_report(report_data, "median-coffee")
    
    # Проверяем, что print был вызван (хотя бы раз)
    assert mock_print.called