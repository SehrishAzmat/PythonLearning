from dataclasses import dataclass


@dataclass
class Expense:
    """Represent a single expense."""

    category: str
    amount: float
    description: str

    def __str__(self) -> str:
        """Return a human-readable summary of the expense."""
        return f"{self.category} - {self.amount:.2f} - {self.description}"
