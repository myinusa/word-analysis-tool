# Word Analysis Tool

## Description

The Word Analysis Tool is a Python-based application designed to perform detailed analysis of text files. It provides functionalities such as word frequency analysis, stop word filtering, and exporting results to various formats. This tool is ideal for linguists, data analysts, and anyone interested in text analysis or natural language processing.

## Steps

- `curl -sSL <https://install.python-poetry.org> | python3 -`
- `poetry install`
- `poetry build`
- `poetry shell`
- `python3 -m word_analysis_tool` or `poetry run word-analysis --input_file example.txt`

## File Structure

```text
word-analysis-tool/
│
├── word-analysis-tool/  # Main package directory
│   ├── __init__.py    # Initializes Python package
│   ├── main.py        # Main script
│   ├── utils/         # Subpackage for utilities
│   │   ├── __init__.py
│   │   ├── file_operations.py
│   │   ├── text_operations.py
│   │   ├── csv_operations.py
│   │
│   ├── data/          # Subpackage for data
│   │   ├── __init__.py
│   │   ├── stop_words.py
│   │   ├── word_bank.py
│
├── logs/              # Directory for log files
│   ├── app.log
│
├── setup.py           # Setup script for the package
├── README.md  
```
