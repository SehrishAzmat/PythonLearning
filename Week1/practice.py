expenses = [
    {"category": "Food", "amount": 1250, "description": "Lunch at cafe"},
    {"category": "Transport", "amount": 275, "description": "Bus fare"},
    {"category": "Entertainment", "amount": 1500, "description": "Movie ticket"},
]


def total_spent(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
        return total


total_spent(expenses)
