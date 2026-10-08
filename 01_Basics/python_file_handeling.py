"""
File Handling in Python
-----------------------

Topics covered:
- open()
- File modes: r, w, a, x
- Reading files
- Writing files
- Appending to files
- with open()
- JSON file handling
- json.dump()
- json.load()
- json.dumps()
- json.loads()
- Exception handling with files
- Expense Tracker persistence
"""

import json

# ============================================================
# 1. BASIC FILE READING
# ============================================================


def read_file(filename):
    """Read and return the complete contents of a text file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


# ============================================================
# 2. BASIC FILE WRITING
# ============================================================


def write_file(filename, content):
    """Write content to a file.

    'w' mode overwrites existing content.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


# ============================================================
# 3. APPENDING TO A FILE
# ============================================================


def append_to_file(filename, content):
    """Append content to the end of an existing file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)


# ============================================================
# 4. READING LINES
# ============================================================


def read_lines(filename):
    """Read a file and return its lines as a list."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


# ============================================================
# 5. JSON - PYTHON OBJECT TO JSON FILE
# ============================================================


def save_json(filename, data):
    """Save a Python object to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# ============================================================
# 6. JSON FILE TO PYTHON OBJECT
# ============================================================


def load_json(filename):
    """Load JSON data from a file and return the Python object."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# ============================================================
# 7. JSON STRING CONVERSION
# ============================================================


def python_to_json_string(data):
    """Convert a Python object into a JSON string."""
    return json.dumps(data)


def json_string_to_python(data):
    """Convert a JSON string into a Python object."""
    return json.loads(data)


# ============================================================
# 8. EXPENSE TRACKER - LOAD EXPENSES
# ============================================================


def load_expenses():
    """Load expenses from expenses.json.

    Returns an empty list if:
    - The file does not exist.
    - The JSON file contains invalid JSON.
    """
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# ============================================================
# 9. EXPENSE TRACKER - SAVE EXPENSES
# ============================================================


def save_expenses(expenses):
    """Save the expenses list to expenses.json."""
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# ============================================================
# 10. EXPENSE TRACKER EXAMPLE
# ============================================================


def expense_tracker_example():
    """Demonstrate loading, modifying, and saving expenses."""

    expenses = load_expenses()

    new_expense = {"category": "Food", "amount": 500, "description": "Lunch"}

    expenses.append(new_expense)

    save_expenses(expenses)

    print("Current expenses:")
    print(expenses)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    expense_tracker_example()
