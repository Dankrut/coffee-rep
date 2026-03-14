#!/usr/bin/env python3
"""
Скрипт для обработки CSV файлов с данными о подготовке студентов к экзаменам.
Формирует отчеты на основе переданных параметров.
"""

import argparse
import sys
from typing import List

from src.readers import read_csv_files
from src.report_generator import ReportGenerator


def parse_arguments():
    """Парсинг аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description="Генерация отчетов по данным о подготовке студентов"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Список CSV файлов для обработки"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=["median-coffee"],
        help="Тип отчета для генерации"
    )
    return parser.parse_args()


def main():
    """Основная функция скрипта."""
    args = parse_arguments()
    
    try:
        # Чтение данных из файлов
        data = read_csv_files(args.files)
        
        if not data:
            print("Нет данных для обработки", file=sys.stderr)
            sys.exit(1)
        
        # Генерация отчета
        generator = ReportGenerator()
        report_data = generator.generate_report(data, args.report)
        
        # Вывод отчета
        generator.print_report(report_data, args.report)
        
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка в данных: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()