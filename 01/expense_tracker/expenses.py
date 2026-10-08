def add_expense(expenses, category, amount, description):
    expense = {"category": category, "amount": amount, "description": description}

    expenses.append(expense)


def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(f"{expense['category']} - {expense['amount']} - {expense['description']}")


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)
