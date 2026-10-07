# ============================================================

# PYTHON EXCEPTIONS

# ============================================================

# Exception:

# An exception is a runtime error/event that interrupts the

# normal flow of a program.

#

# Common examples:

# ValueError          -> correct type, invalid value

# TypeError           -> wrong/incompatible type

# ZeroDivisionError  -> division by zero

# KeyError            -> missing dictionary key

# IndexError          -> invalid list index

# FileNotFoundError   -> file does not exist

# JSONDecodeError     -> invalid JSON

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

# If an exception occurs, else does not run.

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

# Example where both else and finally are used:

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

# 5. raise

# ============================================================

# raise is used when we deliberately want to create an exception.

def add_expense(amount):

```
if amount < 0:
    raise ValueError("Expense amount cannot be negative.")

return amount
```

# Example:

try:
amount = add_expense(-500)
print(amount)

except ValueError as error:
print(error)

# Output:

# Expense amount cannot be negative.

# ============================================================

# 6. Catching the Exception Object

# ============================================================

# "as error" stores the exception object in a variable.

try:
number = int("hello")

except ValueError as error:
print(error)

# The output is the exception's message:

# invalid literal for int() with base 10: 'hello'

# ============================================================

# 7. Common Exception Types

# ============================================================

# ValueError

# Correct data type but invalid value.

try:
number = int("hello")

except ValueError:
print("Invalid number.")

# TypeError

# Incompatible data types.

try:
result = "500" + 100

except TypeError:
print("Cannot combine these data types.")

# ZeroDivisionError

# Attempting to divide by zero.

try:
result = 10 / 0

except ZeroDivisionError:
print("Cannot divide by zero.")

# KeyError

# Trying to access a dictionary key that doesn't exist.

expense = {
"category": "Food",
"amount": 500
}

try:
print(expense["description"])

except KeyError:
print("Description key does not exist.")

# IndexError

# Trying to access an invalid list index.

numbers = [10, 20, 30]

try:
print(numbers[5])

except IndexError:
print("Invalid list index.")

# FileNotFoundError

# Trying to open a file that doesn't exist.

try:
file = open("expenses.json", "r")

except FileNotFoundError:
print("File does not exist.")

# JSONDecodeError

# Occurs when JSON data is invalid.

#

# This becomes especially important when we start

# reading expense data from JSON files.

# ============================================================

# 8. Function + Exception Handling

# ============================================================

def get_amount():

```
try:
    return float(input("Enter amount: "))

except ValueError:
    print("Invalid amount.")
    return None
```

amount = get_amount()

if amount is not None:
print("Amount:", amount)

# ============================================================

# 9. Validation Using raise

# ============================================================

def validate_amount(amount):

```
if amount < 0:
    raise ValueError("Amount cannot be negative.")

return amount
```

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

# 10. Expense Tracker Example

# ============================================================

def add_expense(expenses, category, amount):

```
if amount < 0:
    raise ValueError("Amount cannot be negative")

expense = {
    "category": category,
    "amount": amount
}

expenses.append(expense)

return expenses
```

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

# 11. Why Doesn't the Expense Get Added?

# ============================================================

# When -500 is passed:

# amount < 0

# |

# v

# True

# |

# v

# raise ValueError(...)

# |

# v

# function stops immediately

# |

# X

# expense dictionary is NOT created

# |

# X

# expenses.append(expense) is NOT executed

# The exception moves to the except block:

try:
add_expense(expenses, "Food", -500)

except ValueError as error:
print(error)

# error contains the ValueError object.

# print(error) prints its message.

# ============================================================

# 12. Handling vs Raising Exceptions

# ============================================================

# RAISING:

#

# We use raise when our program detects an invalid condition

# and wants to signal that something went wrong.

def validate_expense(amount):

```
if amount < 0:
    raise ValueError("Amount cannot be negative.")
```

# HANDLING:

#

# We use try/except to handle an exception raised by code.

try:
validate_expense(-100)

except ValueError as error:
print(error)

# Simple distinction:

#

# raise    -> creates/raises the exception

# except   -> catches/handles the exception

# ============================================================

# 13. Avoid Bare except

# ============================================================

# Avoid:

try:
amount = int(input("Amount: "))

except:
print("Something went wrong.")

# Better:

try:
amount = int(input("Amount: "))

except ValueError:
print("Please enter a valid number.")

# Why?

#

# A bare except can hide unexpected programming errors.

# Catch the specific exceptions you expect.

# ============================================================

# 14. Complete Expense Validation Example

# ============================================================

def create_expense(category, amount):

```
if not category:
    raise ValueError("Category cannot be empty.")

if amount < 0:
    raise ValueError("Amount cannot be negative.")

return {
    "category": category,
    "amount": amount
}
```

try:

```
expense = create_expense("Food", -500)
print(expense)
```

except ValueError as error:
print("Error:", error)

# Output:

# Error: Amount cannot be negative.

# ============================================================

# 15. Combining User Input + Validation

# ============================================================

try:

```
category = input("Enter category: ")
amount = float(input("Enter amount: "))

if amount < 0:
    raise ValueError("Amount cannot be negative.")

expense = {
    "category": category,
    "amount": amount
}

print("Expense:", expense)
```

except ValueError as error:
print("Error:", error)

# ============================================================

# 16. Exception Flow

# ============================================================

# General flow:

#

# try

# |

# |-- no exception --> else

# |                      |

# |                      v

# |                   finally

# |

# |-- exception ------> except

# |

# v

# finally

#

#

# finally runs in both cases.

# ============================================================

# 17. Quick Reference

# ============================================================

# try

# -> code that may fail

#

# except

# -> handles an exception

#

# else

# -> runs when try succeeds

#

# finally

# -> always runs

#

# raise

# -> deliberately raises an exception

#

# as error

# -> stores the exception object

# ============================================================

# 18. Exception Checklist

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

# [x] Difference between raising and handling

# [x] Why bare except should be avoided

# ============================================================

# NEXT TOPIC

# ============================================================

# File I/O

#

# We will learn:

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

# - Handling FileNotFoundError

# - Handling JSONDecodeError

# - Building the expense tracker's JSON storage

# ============================================================
