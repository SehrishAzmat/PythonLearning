from models import Expense


class ExpenseTracker:
    """Manage a collection of expenses."""

    def __init__(self) -> None:
        self.expenses: list[Expense] = []

    def add_expense(
        self,
        category: str,
        amount: float,
        description: str,
    ) -> None:
        """Add an expense to the tracker."""
        expense = Expense(
            category=category,
            amount=amount,
            description=description,
        )
        self.expenses.append(expense)

    def show_expenses(self) -> None:
        """Print all expenses, or a message if none exist."""
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(expense)

    def calculate_total(self) -> float:
        """Return the sum of all expense amounts."""
        return sum(expense.amount for expense in self.expenses)

    def __len__(self) -> int:
        """Return the number of expenses."""
        return len(self.expenses)
