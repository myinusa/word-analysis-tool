import logging
from word_analysis_tool.utils.file_operations import read_file, read_category_file
from word_analysis_tool.utils.text_operations import count_word_frequency
from word_analysis_tool.utils.csv_operations import write_to_csv
from word_analysis_tool.data.stop_words import stop_words
from word_analysis_tool.data.word_bank import word_bank
import argparse

# Constants
OUTPUT_FILE: str = "output.csv"

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Process playlist names and descriptions."
    )
    parser.add_argument(
        "--input_file",
        help="Path to the input text file containing playlist names and descriptions.",
    )
    parser.add_argument("--category_file", help="Path to the category CSV file.")
    parser.add_argument(
        "--category_column_name",
        help="Name of the column containing categories in the category CSV file.",
    )
    return parser.parse_args()


def main() -> None:
    """Main function to execute the script."""
    args = parse_arguments()
    input_file = args.input_file
    category_file = args.category_file
    category_column_name = args.category_column_name

    try:
        text = read_file(input_file)
        text = text.lower()
        word_count = count_word_frequency(text, stop_words, word_bank)
        logging.info(f"Total number of unique words and bigrams: {len(word_count)}")

        categories = []
        if category_file and category_column_name:
            try:
                categories = read_category_file(category_file, category_column_name)
            except FileNotFoundError:
                logging.warning(
                    f"Category file not found: {category_file}. Continuing without categories."
                )

        write_to_csv(word_count, categories, OUTPUT_FILE)
        logging.info("Script executed successfully.")
    except Exception as e:
        logging.critical(f"Script execution failed: {e}")


if __name__ == "__main__":
    main()