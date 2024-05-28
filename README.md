# Word Analysis Tool

## Description

The Word Analysis Tool is a Python-based application designed to perform detailed analysis of text files. It provides functionalities such as word frequency analysis, stop word filtering, and exporting results to various formats. This tool is ideal for linguists, data analysts, and anyone interested in text analysis or natural language processing.

## Steps

1. **Install Poetry**:
   Poetry is a tool for dependency management and packaging in Python. To install Poetry, run the following command in your terminal:

    ```shell
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    This command downloads and executes the Poetry installation script.

2. **Install Dependencies**:

    Once Poetry is installed, you can install all the dependencies required for this project by navigating to the project's root directory and running:

    ```shell
    poetry install
    ```

    This command reads the `pyproject.toml` file and installs all the necessary packages.

3. **Build the Project**:

    To build the project, use:

    ```shell
    poetry build
    ```

    This command packages the project into distributable formats like wheel and source distributions.

4. **Activate Virtual Environment**:

    To activate the Poetry-managed virtual environment, run:

    ```shell
    poetry shell
    ```

5. **Run the Application**:

    You can run the application using one of the following commands:

    - Directly with Python:

      ```shell
      python3 -m word_analysis_tool
      ```

    - Using Poetry:

      ```shell
      poetry run word-analysis --input_file example.txt
      ```

    Replace `example.txt` with the path to your input text file. This command analyzes the specified file and outputs the results.

## Roadmap

- [ ] Add support for other file formats
- [ ] Add support for other output formats
- [ ] Record installation

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
