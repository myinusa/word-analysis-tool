import csv
import logging
from typing import Dict, List


def add_category_column(
    word_count: Dict[str, int], categories: List[str] = None
) -> Dict[str, str]:
    """Adds a 'category' column to the word count dictionary based on the category list."""
    if categories is None:
        return {}
    word_category = {}
    for word in word_count.keys():
        word_category[word] = "yes" if word.lower() in categories else "no"
    return word_category


def write_to_csv(
    word_count: Dict[str, int], categories: List[str], output_file: str
) -> None:
    """Writes the word frequency dictionary to a CSV file, optionally with a 'category' column."""
    try:
        include_category = bool(categories)
        if include_category:
            word_category = add_category_column(word_count, categories)

        with open(output_file, "w", newline="") as csvfile:
            logging.info(f"Writing to CSV file: {output_file}")
            fieldnames = ["name", "count"]
            if include_category:
                fieldnames.append("category")
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            sorted_word_count = sorted(
                word_count.items(), key=lambda item: item[1], reverse=True
            )
            for word, count in sorted_word_count:
                row = {"name": word, "count": count}
                if include_category:
                    row["category"] = word_category.get(word, "no")
                writer.writerow(row)
    except Exception as e:
        logging.error(f"Error writing to CSV file : {output_file}, Error: {e}")
        raise