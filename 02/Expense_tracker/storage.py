import json
from pathlib import Path
from typing import Any

from models import Expense

FILE_NAME = Path("expenses.json")


def load_expenses() -> list[Expense]:
    """Load expenses from JSON, returning an empty list if no file exists."""
    try:
        with FILE_NAME.open("r", encoding="utf-8") as file:
            data: Any = json.load(file)
    except FileNotFoundError:
        return []

    if not isinstance(data, list):
        raise TypeError("Invalid expenses.json: expected a JSON list.")

    expenses: list[Expense] = []
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("Invalid expense record: expected a JSON object.")

        expenses.append(
            Expense(
                category=str(item["category"]),
                amount=float(item["amount"]),
                description=str(item["description"]),
            )
        )

    return expenses


def save_expenses(expenses: list[Expense]) -> None:
    """Save expense objects to JSON."""
    data = [
        {
            "category": expense.category,
            "amount": expense.amount,
            "description": expense.description,
        }
        for expense in expenses
    ]

    with FILE_NAME.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
