"""
THURSDAY — ADVANCED PYTHON + PYTEST
Python Crash Course | Week 1

Topics covered:
1. Decorators
2. Generators
3. Context managers
4. Async/await basics
5. Intro to pytest and Expense Tracker testing

Run this file to see the short examples:
    python Thursday.py

Run the actual Expense Tracker tests from 02/Expense_tracker:
    python -m pytest -v

Keep those project tests in a separate file named test_expenses.py.
"""

import asyncio
from contextlib import contextmanager
from functools import wraps

# ============================================================
# 1. DECORATORS
# ============================================================
# A decorator receives a function and returns a replacement function.
# @simple_logger applies the decorator when add_numbers is defined.
# *args accepts positional arguments; **kwargs accepts keyword arguments.
# functools.wraps preserves the original function's metadata.


def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return wrapper


@simple_logger
def add_numbers(a: int, b: int) -> int:
    return a + b


def decorator_example() -> None:
    print(add_numbers(2, 3))  # Output: 5


# If wrapper calls func(...) but does not return its result, the decorated
# function returns None unless the wrapper returns something else.


# ============================================================
# 2. GENERATORS
# ============================================================
# yield produces values one at a time and pauses the function.
# return exits the function. Generators can avoid building another full list.


def large_expenses(expenses: list[dict]):
    """Yield expenses whose amount is greater than 1000."""
    for expense in expenses:
        if expense["amount"] > 1000:
            yield expense


def generator_example() -> None:
    expenses = [
        {"category": "Food", "amount": 500},
        {"category": "Rent", "amount": 1500},
        {"category": "Travel", "amount": 1200},
    ]

    for expense in large_expenses(expenses):
        print(expense)


# A generator is normally consumed as it is iterated. An exhausted generator
# does not automatically restart.


# ============================================================
# 3. CONTEXT MANAGERS
# ============================================================
# with manages setup and cleanup. For files, it closes the file when the
# block ends, including if an exception occurs inside the block.


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


@contextmanager
def managed_message(message: str):
    """Example context manager made with contextlib.contextmanager."""
    print(f"Entering: {message}")
    try:
        yield
    finally:
        print(f"Leaving: {message}")


def context_manager_example() -> None:
    with managed_message("example block"):
        print("Inside the block")


# The Expense Tracker's storage.py also uses `with` to safely open JSON files.


# ============================================================
# 4. ASYNC / AWAIT BASICS
# ============================================================
# async def defines a coroutine. await pauses the current coroutine until
# the awaited operation completes. asyncio.run() starts the async entry point.
# Async is useful for I/O-bound work; it does not automatically speed up
# CPU-heavy work.


async def fetch_expenses() -> list[str]:
    await asyncio.sleep(1)  # Simulates waiting for an I/O operation.
    return ["Food", "Transport", "Rent"]


async def async_example() -> None:
    expenses = await fetch_expenses()
    print(expenses)


def run_async_example() -> None:
    asyncio.run(async_example())


# asyncio.gather() can run multiple independent coroutines concurrently.
# Do not call asyncio.run() from inside an already-running event loop.


# ============================================================
# 5. PYTEST NOTES
# ============================================================
# Install pytest:
#     python -m pip install pytest
#
# Run tests from the project folder:
#     python -m pytest -v
#
# Pytest discovers test_*.py files and test_* functions by default.
# `assert` checks whether an expected condition is true.
# Arrange–Act–Assert:
#   Arrange: prepare objects and sample data.
#   Act: call the function or method.
#   Assert: check the result.
#
# Fixtures used in our Expense Tracker tests:
#   tmp_path       -> temporary directory for test files
#   monkeypatch    -> temporarily replaces storage.FILE_NAME
#   capsys         -> captures printed output
#   pytest.approx  -> compares floating-point values with tolerance
#   pytest.raises  -> checks that an expected exception is raised
#
# Our test_expenses.py covers adding expenses, totals, string formatting,
# printed output, JSON save/load, missing files, and invalid JSON structure.


def main() -> None:
    """Run each short lesson example once."""
    print("\n--- Decorators ---")
    decorator_example()

    print("\n--- Generators ---")
    generator_example()

    print("\n--- Context managers ---")
    context_manager_example()

    print("\n--- Async / await ---")
    run_async_example()

    print("\nLesson examples finished.")
    print("Run the tracker tests separately with: python -m pytest -v")


if __name__ == "__main__":
    main()
