from .median_coffee import MedianCoffeeReport

# Словарь доступных отчетов
REPORTS = {
    'median-coffee': MedianCoffeeReport,
}

__all__ = ['REPORTS', 'MedianCoffeeReport']