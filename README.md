# Python Algorithms & Data Structures

## Running Tests with Pytest

### 1. Install pytest
Ensure `pytest` is installed in your Python environment:
```bash
pip install pytest
```

### 2. Run all tests in the project
To discover and run all tests across all your `utests/` directories, run this command from the root of your workspace:
```bash
python -m pytest
```
*(Note: Using `python -m pytest` automatically adds your current directory to the Python path, allowing your tests to import your local modules without `ModuleNotFoundError` issues).*

### 3. Run tests in a specific directory
If you only want to run the tests for a specific topic, pass the directory path:
```bash
python -m pytest problems/utests/
```

### 4. Run a specific test file
To run just one file, pass the exact file path:
```bash
python -m pytest two_pointers/basics/utests/test_longest_sub_string.py
```

### 5. Run a specific test function
If you want to run a single test function inside a file, use the `::` syntax followed by the test function name:
```bash
python -m pytest problems/utests/test_tree_sum.py::test_my_specific_case
```

### 6. Useful Pytest Flags
* **`-v` (Verbose):** Shows the name of every individual test being run and its status (PASSED/FAILED).
  ```bash
  python -m pytest -v
  ```
* **`-s` (Show Output):** Prints any `print()` statements in your code to the console.
  ```bash
  python -m pytest -s
  ```
* **`-k` (Keyword Match):** Runs tests that match a specific substring in their name.
  ```bash
  python -m pytest -k "longest"
  ```
* **`--lf` (Last Failed):** Only runs the tests that failed during the last run.
  ```bash
  python -m pytest --lf
  ```