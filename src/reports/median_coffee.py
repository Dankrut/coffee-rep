from collections import defaultdict
from statistics import median
from typing import List, Dict, Any

from .base import BaseReport


class MedianCoffeeReport(BaseReport):
    """Отчет о медианных тратах на кофе по каждому студенту."""
    
    @property
    def name(self) -> str:
        return "median-coffee"
    
    @property
    def headers(self) -> List[str]:
        return ["Студент", "Медианные траты на кофе"]
    
    def calculate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Рассчитывает медианные траты на кофе для каждого студента.
        
        Args:
            data: Список словарей с данными из CSV
            
        Returns:
            Отсортированный по убыванию трат список студентов с медианами
        """
        # Группируем траты по студентам
        student_spent = defaultdict(list)
        
        for row in data:
            student = row['student']
            try:
                coffee_spent = float(row['coffee_spent'])
                student_spent[student].append(coffee_spent)
            except (ValueError, KeyError):
                continue
        
        # Рассчитываем медиану для каждого студента
        result = []
        for student, spent_list in student_spent.items():
            if spent_list:  # Проверяем, что есть данные
                median_spent = median(spent_list)
                result.append({
                    'student': student,
                    'median_coffee': median_spent
                })
        
        # Сортируем по убыванию трат
        result.sort(key=lambda x: x['median_coffee'], reverse=True)
        
        return result