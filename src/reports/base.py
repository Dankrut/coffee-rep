from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseReport(ABC):
    """Базовый класс для всех отчетов."""
    
    @abstractmethod
    def calculate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Рассчитывает данные для отчета.
        
        Args:
            data: Список словарей с данными из CSV
            
        Returns:
            Список словарей с результатами отчета
        """
        pass
    
    @property
    @abstractmethod
    def headers(self) -> List[str]:
        """Заголовки для таблицы отчета."""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Название отчета."""
        pass