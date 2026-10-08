from expenses import add_expense, calculate_total, show_expenses
from storage import load_expenses, save_expenses


def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ")
            amount = float(input("Amount: "))
            description = input("Description: ")

            add_expense(expenses, category, amount, description)

            save_expenses(expenses)
            print("Expense added.")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total expenses: {total}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
