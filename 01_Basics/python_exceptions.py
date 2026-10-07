# ============================================================
# PYTHON EXCEPTIONS
# ============================================================

# An exception is a runtime error/event that interrupts the
# normal flow of a program.


# ============================================================
# 1. try / except
# ============================================================

# Code that may cause an exception goes inside try.
# except handles the exception.

try:
    amount = int(input("Enter amount: "))
    print(amount)
except ValueError:
    print("Please enter a valid number.")


# ============================================================
# 2. Multiple Exceptions
# ============================================================

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# 3. else
# ============================================================

# else runs ONLY when the try block succeeds.

try:
    amount = int(input("Enter amount: "))
except ValueError:
    print("Invalid amount.")
else:
    print("Amount entered successfully:", amount)


# ============================================================
# 4. finally
# ============================================================

# finally runs whether an exception occurs or not.

try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number.")
finally:
    print("Done")


# ============================================================
# 5. else + finally
# ============================================================

try:
    number = int(input("Enter number: "))
    result = 100 / number
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Operation finished.")


# ============================================================
# 6. raise
# ============================================================

# raise is used when we deliberately want to create an exception.


def add_expense(amount):
    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")
    return amount


try:
    amount = add_expense(-500)
    print(amount)
except ValueError as error:
    print(error)


# ============================================================
# 7. Catching the Exception Object
# ============================================================

# "as error" stores the exception object in a variable.

try:
    number = int("hello")
except ValueError as error:
    print(error)


# ============================================================
# 8. Common Exception Types
# ============================================================

# ValueError:
# Correct data type but invalid value.

try:
    number = int("hello")
except ValueError:
    print("Invalid number.")


# TypeError:
# Incompatible data types.

try:
    result = "500" + 100
except TypeError:
    print("Cannot combine these data types.")


# ZeroDivisionError:
# Attempting to divide by zero.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# KeyError:
# Trying to access a dictionary key that does not exist.

expense = {"category": "Food", "amount": 500}

try:
    print(expense["description"])
except KeyError:
    print("Description key does not exist.")


# IndexError:
# Trying to access an invalid list index.

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Invalid list index.")


# FileNotFoundError:
# Trying to open a file that does not exist.

try:
    with open("expenses.json", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File does not exist.")

# JSONDecodeError:
# Occurs when JSON data is invalid.
# We will use this when working with JSON files.


# ============================================================
# 9. Function + Exception Handling
# ============================================================


def get_amount():
    try:
        return float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return None


amount = get_amount()

if amount is not None:
    print("Amount:", amount)


# ============================================================
# 10. Validation Using raise
# ============================================================


def validate_amount(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    return amount


# Valid value:

try:
    amount = validate_amount(500)
    print(amount)
except ValueError as error:
    print(error)


# Invalid value:

try:
    amount = validate_amount(-500)
    print(amount)
except ValueError as error:
    print(error)


# ============================================================
# 11. Expense Tracker Example
# ============================================================


def add_expense(expenses, category, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    expense = {"category": category, "amount": amount}

    expenses.append(expense)
    return expenses


expenses = []

try:
    add_expense(expenses, "Food", -500)
except ValueError as error:
    print(error)

print(expenses)


# Output:
# Amount cannot be negative
# []


# ============================================================
# 12. Why Does the Expense NOT Get Added?
# ============================================================

# When -500 is passed:
#
# amount < 0
#     |
#     v
#   True
#     |
#     v
# raise ValueError(...)
#     |
#     v
# function stops immediately
#
# Therefore these lines are never reached:
#
# expense = {
#     "category": category,
#     "amount": amount
# }
#
# expenses.append(expense)


# ============================================================
# 13. Raising vs Handling Exceptions
# ============================================================

# RAISING:
# raise creates/signals an exception.


def validate_expense(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")


# HANDLING:
# try/except catches and handles an exception.

try:
    validate_expense(-100)
except ValueError as error:
    print(error)


# Simple distinction:
#
# raise  -> raises the exception
# except -> catches/handles the exception


# ============================================================
# 14. Avoid Bare except
# ============================================================

# Avoid:
#
# try:
#     amount = int(input("Amount: "))
# except:
#     print("Something went wrong.")
#
# Better:

try:
    amount = int(input("Amount: "))
except ValueError:
    print("Please enter a valid number.")


# Catch the specific exception you expect.


# ============================================================
# 15. Complete Expense Validation
# ============================================================


def create_expense(category, amount):
    if not category:
        raise ValueError("Category cannot be empty.")

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    return {"category": category, "amount": amount}


try:
    expense = create_expense("Food", -500)
    print(expense)
except ValueError as error:
    print("Error:", error)


# ============================================================
# 16. User Input + Validation
# ============================================================

try:
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    expense = {"category": category, "amount": amount}

    print("Expense:", expense)

except ValueError as error:
    print("Error:", error)


# ============================================================
# 17. Exception Flow
# ============================================================

# Normal flow:
#
# try
#   |
#   +-- no exception --> else
#   |                      |
#   |                      v
#   |                   finally
#   |
#   +-- exception ------> except
#                          |
#                          v
#                       finally
#
# finally runs in both cases.


# ============================================================
# 18. Quick Reference
# ============================================================

# try:
#     Code that may fail
#
# except:
#     Handle an exception
#
# else:
#     Runs when try succeeds
#
# finally:
#     Always runs
#
# raise:
#     Deliberately raises an exception
#
# as error:
#     Stores the exception object


# ============================================================
# 19. Exception Checklist
# ============================================================

# [x] What is an exception?
# [x] try
# [x] except
# [x] Multiple except blocks
# [x] else
# [x] finally
# [x] raise
# [x] Exception object using "as"
# [x] Common exception types
# [x] Function exception handling
# [x] Validation with raise
# [x] Expense tracker validation
# [x] Raising vs handling
# [x] Avoiding bare except


# ============================================================
# NEXT TOPIC: FILE I/O
# ============================================================

# We will cover:
#
# - Opening files
# - Reading files
# - Writing files
# - Appending files
# - with open(...)
# - File modes
# - JSON files
# - json.load()
# - json.dump()
# - FileNotFoundError
# - JSONDecodeError
# - Expense tracker JSON storage
