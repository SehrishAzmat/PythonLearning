# Thursday Deliverable — Expense Tracker Testing

## Overview

This deliverable focuses on testing the Expense Tracker project using **pytest**, Python's testing framework. The objective is to verify that the application's core functionality works correctly and that changes do not introduce unexpected bugs.

A total of **12 test functions** have been implemented in `test_expense.py` to validate the application's behavior.

## Project Structure

```text
expense_tracker/
├── main.py
├── tracker.py
├── storage.py
├── test_expense.py
└── README.md
```

*Note: The structure above is illustrative. Keep the filenames consistent with your actual project.*

## Concepts Practiced

- **pytest:** Running automated tests and checking application behavior.
- **Test functions:** Separating individual test cases to verify specific functionality.
- **Assertions:** Using `assert` to compare actual results with expected results.
- **Test isolation:** Testing functionality independently to make failures easier to identify.
- **Regression testing:** Re-running tests after code changes to ensure existing functionality still works.
- **Test-driven debugging:** Using test results to identify and investigate unexpected behavior.

## Test Coverage

The 12 test functions are designed to validate the Expense Tracker's behavior. The specific functionality covered depends on the test cases implemented in `test_expense.py`.

These tests help establish confidence in the application's correctness and make future refactoring safer.

## How to Run the Tests

### 1. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run this command from the directory containing your virtual environment.

### 2. Install pytest

If pytest is not already installed:

```bash
python -m pip install pytest
```

### 3. Run all tests

Navigate to the directory containing `test_expense.py` and run:

```bash
python -m pytest -v
```

The `-v` option displays the name and result of each test.

### 4. Run only the Expense Tracker tests

```bash
python -m pytest test_expense.py -v
```

## Understanding the Results

- **PASSED:** The test completed successfully.
- **FAILED:** The test ran but an assertion or another expected condition did not hold.
- **ERROR:** An unexpected error occurred while setting up or executing a test.

A successful run should show all 12 tests passing, assuming all test cases are correctly implemented and the application behaves as expected.

## Learning Outcomes

After completing this deliverable, I practiced:

1. Writing automated tests for Python application logic.
2. Using pytest to execute and inspect test results.
3. Verifying expected behavior with assertions.
4. Identifying failures through automated testing.
5. Understanding how testing improves maintainability and reduces regressions.

## Conclusion

This Thursday deliverable demonstrates the application of automated testing to the Expense Tracker project. Implementing 12 test functions provides a foundation for validating application behavior and developing more reliable, maintainable Python software.

**Deliverable:** `test_expense.py` containing 12 test functions.
