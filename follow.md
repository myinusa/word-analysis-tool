After building your Python package using the pyproject.toml configuration, you can install and execute it in several ways. Here’s how you can do it:

1. Installing the Package Locally
After building the package with python -m build, you will have wheel and source distribution files in the dist/ directory. You can install the package locally using pip. Navigate to the directory containing the dist folder and run:

pip install dist/word_analysis_tool-0.1.0-py3-none-any.whl
Replace word_analysis_tool-0.1.0-py3-none-any.whl with the actual name of the wheel file generated in your dist directory.

2. Running the Installed Package
Once the package is installed, you can run it using the entry point you defined in your pyproject.toml. According to the example provided, the entry point for the console script is named word-analysis. You can execute your package directly from the command line:

word-analysis --input_file=path/to/your/input.txt --category_file=path/to/your/categories.csv --category_column_name=yourColumnName
Replace the paths and yourColumnName with the actual values relevant to your use case.

3. Running Without Installing
If you prefer to run the package without installing it, you can use python -m followed by the package name, assuming your package structure and __main__.py are set up correctly to handle this. For example:

python -m word_analysis_tool.main --input_file=path/to/your/input.txt --category_file=path/to/your/categories.csv --category_column_name=yourColumnName
This method requires that your Python paths and package imports are correctly set up to recognize word_analysis_tool.main as a valid module path.

4. Using a Virtual Environment
It's a good practice to use a virtual environment to avoid conflicts with other packages and to keep your system clean. Here’s how you can set up a virtual environment and install your package within it:

# Create a virtual environment

python -m venv venv

# Activate the virtual environment

# On Windows

venv\Scripts\activate

# On Unix or MacOS

source venv/bin/activate

# Install your package

pip install dist/word_analysis_tool-0.1.0-py3-none-any.whl

# Run your package

word-analysis --input_file=path/to/your/input.txt --category_file=path/to/your/categories.csv --category_column_name=yourColumnName
5. Updating the Package
If you make changes to your package and rebuild it, you can upgrade the installed package using:

pip install --upgrade dist/word_analysis_tool-0.1.0-py3-none-any.whl
This setup ensures that you can develop, test, and use your Python package efficiently, leveraging modern packaging practices with Python's built-in tools.
