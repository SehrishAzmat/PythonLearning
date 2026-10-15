# Expense Tracker — Wednesday OOP Refactor

## Files
- `models.py`: `Expense` dataclass and readable string representation.
- `tracker.py`: `ExpenseTracker` class and expense operations.
- `storage.py`: JSON persistence.
- `main.py`: command-line menu.

## Run
```bash
python main.py
```

## Type-check
Install mypy if needed:
```bash
python -m pip install mypy
python -m mypy models.py tracker.py storage.py main.py
```
