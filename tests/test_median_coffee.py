import pytest
from src.reports.median_coffee import MedianCoffeeReport


@pytest.fixture
def sample_data():
    """Фикстура с тестовыми данными."""
    return [
        {'student': 'Алексей Смирнов', 'coffee_spent': '450'},
        {'student': 'Алексей Смирнов', 'coffee_spent': '500'},
        {'student': 'Алексей Смирнов', 'coffee_spent': '550'},
        {'student': 'Дарья Петрова', 'coffee_spent': '200'},
        {'student': 'Дарья Петрова', 'coffee_spent': '250'},
        {'student': 'Дарья Петрова', 'coffee_spent': '300'},
        {'student': 'Иван Кузнецов', 'coffee_spent': '600'},
        {'student': 'Иван Кузнецов', 'coffee_spent': '650'},
        {'student': 'Иван Кузнецов', 'coffee_spent': '700'},
    ]


def test_median_coffee_report_calculation(sample_data):
    """Тест расчета медианных трат."""
    report = MedianCoffeeReport()
    result = report.calculate(sample_data)
    
    assert len(result) == 3
    
    # Проверяем порядок сортировки (по убыванию)
    assert result[0]['student'] == 'Иван Кузнецов'
    assert result[0]['median_coffee'] == 650.0
    
    assert result[1]['student'] == 'Алексей Смирнов'
    assert result[1]['median_coffee'] == 500.0
    
    assert result[2]['student'] == 'Дарья Петрова'
    assert result[2]['median_coffee'] == 250.0


def test_median_with_odd_number_of_values():
    """Тест медианы с нечетным количеством значений."""
    data = [
        {'student': 'Студент 1', 'coffee_spent': '100'},
        {'student': 'Студент 1', 'coffee_spent': '200'},
        {'student': 'Студент 1', 'coffee_spent': '300'},
    ]
    
    report = MedianCoffeeReport()
    result = report.calculate(data)
    
    assert len(result) == 1
    assert result[0]['median_coffee'] == 200.0


def test_median_with_even_number_of_values():
    """Тест медианы с четным количеством значений."""
    data = [
        {'student': 'Студент 1', 'coffee_spent': '100'},
        {'student': 'Студент 1', 'coffee_spent': '200'},
        {'student': 'Студент 1', 'coffee_spent': '300'},
        {'student': 'Студент 1', 'coffee_spent': '400'},
    ]
    
    report = MedianCoffeeReport()
    result = report.calculate(data)
    
    assert len(result) == 1
    assert result[0]['median_coffee'] == 250.0  # (200 + 300) / 2


def test_empty_data():
    """Тест с пустыми данными."""
    report = MedianCoffeeReport()
    result = report.calculate([])
    
    assert result == []


def test_invalid_coffee_value():
    """Тест обработки некорректных значений coffee_spent."""
    data = [
        {'student': 'Студент 1', 'coffee_spent': 'invalid'},
        {'student': 'Студент 1', 'coffee_spent': '200'},
    ]
    
    report = MedianCoffeeReport()
    result = report.calculate(data)
    
    # Должна быть только одна валидная запись
    assert len(result) == 1
    assert result[0]['median_coffee'] == 200.0


def test_properties():
    """Тест свойств отчета."""
    report = MedianCoffeeReport()
    
    assert report.name == "median-coffee"
    assert report.headers == ["Студент", "Медианные траты на кофе"]