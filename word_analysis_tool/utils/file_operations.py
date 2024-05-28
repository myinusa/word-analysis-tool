import csv
import logging
from typing import List


def read_file(file_path: str) -> str:
    """Reads the content of a text file and returns it as a string."""
    try:
        with open(file_path, "r") as file:
            logging.info(f"Reading file: {file_path}")
            return file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading file: {file_path}, Error: {e}")
        raise


def read_category_file(file_path: str, category_column_name: str) -> List[str]:
    """Reads the category values from a CSV file and returns them as a list."""
    try:
        categories = []
        with open(file_path, "r") as file:
            logging.info(f"Reading category file: {file_path}")
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                category = row.get(category_column_name)
                if category:
                    categories.append(category.lower())
        return categories
    except FileNotFoundError:
        logging.error(f"Category file not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading category file: {file_path}, Error: {e}")
        raise