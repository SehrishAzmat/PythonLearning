"""
Wednesday — Week 1: Professional Python
Topic: OOP refactoring, dataclasses, dunder methods, type hints, mypy, PEP 8.

This file is a learning/reference file for the Wednesday content. The practical
Expense Tracker implementation is split across models.py, tracker.py, storage.py,
and main.py in the project folder.
"""

from dataclasses import dataclass


# 1. Dataclasses
# A dataclass is useful when a class primarily stores structured data.
@dataclass
class Expense:
    """Represent one expense with explicitly typed fields."""

    category: str
    amount: float
    description: str

    # 2. Dunder method
    # __str__ defines the human-readable form used by print(expense) and str().
    def __str__(self) -> str:
        return f"{self.category} - {self.amount:.2f} - {self.description}"


# 3. Composition
# ExpenseTracker HAS a collection of Expense objects.
class ExpenseTracker:
    """Store and manage expenses."""

    def __init__(self) -> None:
        self.expenses: list[Expense] = []

    def add_expense(
        self,
        category: str,
        amount: float,
        description: str,
    ) -> None:
        """Create an Expense and add it to the collection."""
        expense = Expense(
            category=category,
            amount=amount,
            description=description,
        )
        self.expenses.append(expense)

    def show_expenses(self) -> None:
        """Display expenses, or explain that the tracker is empty."""
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(expense)

    def calculate_total(self) -> float:
        """Return the sum of all expense amounts."""
        return sum(expense.amount for expense in self.expenses)

    # __len__ allows len(tracker) to return the number of stored expenses.
    def __len__(self) -> int:
        return len(self.expenses)


def demonstrate_wednesday_topics() -> None:
    """Run a small demonstration of the concepts covered on Wednesday."""
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 500.0, "Lunch")
    tracker.add_expense("Transport", 200.0, "Bus")

    tracker.show_expenses()
    print(f"Total expenses: {tracker.calculate_total():.2f}")
    print(f"Number of expenses: {len(tracker)}")

    # Inheritance example (conceptual):
    # A RecurringExpense could inherit from Expense if it truly IS-A Expense.
    # We do not add this to the tracker without a real requirement.
    #
    # class RecurringExpense(Expense):
    #     pass
    #
    # Prefer composition for our actual relationship:
    # ExpenseTracker HAS Expense objects.


if __name__ == "__main__":
    demonstrate_wednesday_topics()
