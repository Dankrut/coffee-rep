import csv
from typing import List, Dict, Any


def read_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Читает данные из CSV файлов.
    
    Args:
        file_paths: Список путей к CSV файлам
        
    Returns:
        Список словарей с данными из всех файлов
        
    Raises:
        FileNotFoundError: Если один из файлов не найден
    """
    all_data = []
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames and 'student' in reader.fieldnames and 'coffee_spent' in reader.fieldnames:
                    for row in reader:
                        all_data.append(row)
                else:
                    raise ValueError(f"Файл {file_path} не содержит необходимых колонок")
        except FileNotFoundError:
            raise FileNotFoundError(file_path)
    
    return all_data