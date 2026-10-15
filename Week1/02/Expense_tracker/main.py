from storage import load_expenses, save_expenses
from tracker import ExpenseTracker


def main() -> None:
    tracker = ExpenseTracker()
    tracker.expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            category = input("Category: ").strip()

            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            description = input("Description: ").strip()

            tracker.add_expense(category, amount, description)
            save_expenses(tracker.expenses)
            print("Expense added.")

        elif choice == "2":
            tracker.show_expenses()

        elif choice == "3":
            print(f"Total expenses: {tracker.calculate_total():.2f}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
