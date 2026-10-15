# Week 1 — Professional Python, Git and SQL

## Purpose

This README documents the first week of the **4-Week Plan: Intern to Professional Full Stack Python Developer**. Week 1 focuses on building professional Python habits, using Git/GitHub workflow, and learning relational database fundamentals.

The week's main outcome is a clean, typed, tested command-line Expense Tracker that reads and writes JSON, plus SQL practice and a review of the week's work.

## Week 1 at a glance

| Day | Learn | Build / deliverable |
|---|---|---|
| Monday | Development setup, virtual environments, `uv`/`pip`, VS Code, Git, branches, commits, pushes, pull requests, merge conflicts | Repository with README, `.gitignore`, pre-commit setup, and first PR merged |
| Tuesday | Core Python: data structures, comprehensions, functions, `*args`/`**kwargs`, exceptions, file I/O, modules and packages | CLI Expense Tracker that reads and writes JSON |
| Wednesday | OOP: classes, inheritance, dataclasses, dunder methods; type hints, `mypy`, PEP 8 | Refactor the tracker into classes with full type hints |
| Thursday | Advanced Python: decorators, generators, context managers, async/await basics; introduction to pytest | Write 10+ pytest tests for the tracker |
| Friday | SQL: tables, keys, joins, `GROUP BY`, indexes, normalization; PostgreSQL and `psql` | Design a four-table schema, write 15 SQL queries, and complete a Week 1 review |

## Monday — Development setup and Git workflow

### Topics
- Python environment setup and virtual environments
- Installing packages with `pip` or `uv`
- VS Code workflow
- Git clone, branches, commits, push, pull requests, and merge-conflict basics
- Repository hygiene: README, `.gitignore`, and pre-commit hooks

### Intended outcome
A reproducible repository with a clear README and `.gitignore`, a basic pre-commit setup, and the first change delivered through a pull request.

### Example commands
```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip
git status
git switch -c feature/expense-tracker
git add .
git commit -m "Set up Python project"
git push -u origin feature/expense-tracker
```

Commands should be adjusted to the repository's existing setup; do not recreate a virtual environment if the project already has a working one.

## Tuesday — Core Python and JSON file handling

### Topics
- Built-in data structures
- Comprehensions
- Functions and arguments, including `*args` and `**kwargs`
- Exception handling
- File I/O
- Modules and packages

### Expense Tracker
The initial tracker separates responsibilities into modules:
- `expenses.py`: add expenses, display expenses, calculate totals
- `storage.py`: load and save expense data as JSON
- `main.py`: command-line menu and user input
- `expenses.json`: persisted records

Each expense record uses the fields `category`, `amount`, and `description`.

### JSON concepts
- `json.load(file)` reads JSON from an open file and converts it into Python data.
- `json.dump(data, file, indent=4)` serializes Python data into JSON and writes it to an open file.
- `with open(...)` manages the file context and closes the file after the block finishes.
- `FileNotFoundError` can be handled to start with an empty list when the JSON file does not exist.

### Intended outcome
The command-line tracker can add expenses, display saved expenses, calculate the total, and persist data between runs.

## Wednesday — OOP and professional Python

### Topics
- Classes and objects
- Inheritance and composition
- Dataclasses
- Dunder methods
- Type hints
- `mypy`
- PEP 8

### Refactoring design
The tracker is organized into modules with separate responsibilities:

```text
expense_tracker/
├── main.py       # CLI and application flow
├── models.py     # Expense data model
├── tracker.py    # Expense management logic
├── storage.py    # JSON persistence
└── expenses.json # Saved expense records
```

### Key design decisions
- `Expense` is a data-oriented model represented by a `@dataclass`.
- `ExpenseTracker` manages a collection of `Expense` objects.
- Composition fits the relationship: an `ExpenseTracker` **has** expenses.
- Inheritance is appropriate when there is a genuine “is-a” relationship; it should not be added just to use inheritance.
- `__str__` can provide a readable string for an expense.
- `__len__` can make `len(tracker)` return the number of expenses.
- Type hints make expected parameters, attributes, and return values clearer.
- `mypy` checks type consistency statically; annotations alone generally do not enforce types at runtime.
- PEP 8 provides widely used conventions for readable, consistent Python code.

### Type-checking command
Run this from the folder that contains all four Python modules:

```bash
python -m mypy models.py tracker.py storage.py main.py
```

### Path handling note
Use a path anchored to the storage module so the data file does not depend on the terminal's current working directory:

```python
from pathlib import Path

FILE_NAME = Path(__file__).parent / "expenses.json"
```

Make sure `Path` is imported from `pathlib`, not `zipfile`.

### Intended outcome
The existing tracker is refactored into classes, retains its JSON persistence and CLI behavior, and uses type hints throughout.

## Thursday — Advanced Python and testing

### Topics
- Decorators
- Generators
- Context managers
- Async/await fundamentals
- Introductory pytest

### Intended deliverable
Write **10 or more pytest tests** for the tracker.

Useful test areas include:
- Adding an expense
- Showing an empty tracker
- Calculating totals
- Multiple expenses
- Saving and loading JSON
- Loading when the file does not exist
- Invalid input or invalid persisted data where applicable

Tests should verify observable behavior rather than only implementation details. Keep tests repeatable and avoid relying on a developer's personal data file.

### Typical test command
```bash
python -m pytest
```

## Friday — SQL and relational database fundamentals

### Topics
- Tables, rows, columns, and relational modeling
- Primary keys and foreign keys
- `SELECT`, `INSERT`, `UPDATE`, and `DELETE`
- `JOIN`
- Aggregation with `GROUP BY` and `HAVING`
- Indexing basics
- Normalization
- PostgreSQL and `psql`

### Intended deliverable
- Design a four-table schema
- Write at least 15 SQL queries
- Review the week's Python and SQL work

### Suggested query coverage
Ensure the query set includes:
1. Basic `SELECT` with `WHERE`
2. `INSERT`
3. `UPDATE`
4. `DELETE`
5. `INNER JOIN`
6. `LEFT JOIN`
7. Aggregation with `COUNT`
8. Aggregation with `SUM`
9. `GROUP BY`
10. `HAVING`
11. Sorting with `ORDER BY`
12. Filtering with `LIMIT`
13. A subquery
14. A query using multiple related tables
15. An index example and an explanation of when it may help

These are suggested coverage areas to organize practice; they are not a substitute for recording the actual queries completed.

## Week 1 completion checklist

### Environment and collaboration
- [ ] Python environment and dependencies work
- [ ] Repository includes a README and `.gitignore`
- [ ] Git branch, commit, push, and pull-request workflow practiced
- [ ] Pre-commit setup reviewed or configured

### Python and Expense Tracker
- [ ] CLI accepts and adds expenses
- [ ] Expenses can be displayed
- [ ] Total calculation works
- [ ] JSON data persists between runs
- [ ] Modules have clear responsibilities
- [ ] Refactored code uses classes and a dataclass where appropriate
- [ ] Type hints cover functions, methods, and important attributes
- [ ] `mypy` has been run and any reported issues reviewed
- [ ] Code style follows PEP 8 conventions
- [ ] At least 10 pytest tests written and run

### SQL
- [ ] Four-table schema designed
- [ ] Primary and foreign keys identified
- [ ] At least 15 SQL queries written
- [ ] Joins and aggregation practiced
- [ ] Indexing and normalization basics reviewed

### End-of-week review
The plan calls for a timed 60-minute coding task involving Python and SQL, plus a review of the Expense Tracker pull request against the rubric.

- [ ] Timed Python + SQL task completed
- [ ] Tracker pull request reviewed
- [ ] Three-line daily log / weekly notes updated
- [ ] Remaining blockers documented

## Git workflow reminder

Use the repository's agreed branch and pull-request workflow. A typical sequence is:

```bash
git status
git switch -c feature/week-1-expense-tracker
git add .
git commit -m "Refactor expense tracker and add tests"
git push -u origin feature/week-1-expense-tracker
```

Open a pull request on GitHub after pushing. Check the branch name and repository status before committing; do not blindly stage unrelated files.

## Notes

This document summarizes the Week 1 schedule and deliverables in the **4-Week Plan: Intern to Professional Full Stack Python Developer**. The exact work completed should be marked in the checklist only after it has been verified in the repository.
