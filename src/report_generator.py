from typing import List, Dict, Any

from tabulate import tabulate

from src.reports import REPORTS


class ReportGenerator:
    """Генератор отчетов."""
    
    def __init__(self):
        self._reports = {}
        # Регистрируем все доступные отчеты
        for report_name, report_class in REPORTS.items():
            self.register_report(report_class())
    
    def register_report(self, report):
        """Регистрирует новый тип отчета."""
        self._reports[report.name] = report
    
    def generate_report(self, data: List[Dict[str, Any]], report_name: str) -> List[Dict[str, Any]]:
        """
        Генерирует отчет указанного типа.
        
        Args:
            data: Сырые данные из CSV
            report_name: Название отчета
            
        Returns:
            Данные для отчета
            
        Raises:
            ValueError: Если указан неизвестный тип отчета
        """
        if report_name not in self._reports:
            raise ValueError(f"Неизвестный тип отчета: {report_name}")
        
        report = self._reports[report_name]
        return report.calculate(data)
    
    def print_report(self, report_data: List[Dict[str, Any]], report_name: str):
        """
        Выводит отчет в консоль в виде таблицы.
        
        Args:
            report_data: Данные отчета
            report_name: Название отчета
        """
        if report_name not in self._reports:
            raise ValueError(f"Неизвестный тип отчета: {report_name}")
        
        report = self._reports[report_name]
        
        # Преобразуем данные для tabulate
        table_data = []
        for item in report_data:
            if report_name == "median-coffee":
                table_data.append([
                    item['student'],
                    f"{item['median_coffee']:.2f}"
                ])
        
        print(f"\nОтчет: {report_name}")
        print(tabulate(
            table_data,
            headers=report.headers,
            tablefmt="grid",
            numalign="right"
        ))
    def test_print_report_with_invalid_data():
        """Тест вывода отчета с некорректными данными."""
        generator = ReportGenerator()
        report_data = [{'student': 'Тест', 'median_coffee': 100}]
        generator.print_report(report_data, "median-coffee") 