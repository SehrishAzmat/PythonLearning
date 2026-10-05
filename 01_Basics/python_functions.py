# ============================================================
# PYTHON FUNCTIONS — COMPLETE STUDY NOTES
# ============================================================

# Current Internship Plan:
# Core Python → Functions → *args/**kwargs → Exceptions → File I/O

# ============================================================
# 1. WHAT IS A FUNCTION?
# ============================================================

# A function is a reusable block of code designed to perform
# a specific task.

# Basic syntax:

def function_name():
    # code
    pass

# Defining a function does NOT execute it.
# The function runs only when it is called.

def greet():
    print("Hello Sehrish")

# Function call:
greet()

# ============================================================
# 2. PARAMETERS VS ARGUMENTS
# ============================================================

# Parameter:
# A variable written inside the function definition.

def greet_with_name(name):  # name = parameter
    print("Hello", name)

# Argument:
# The actual value passed when calling the function.

greet_with_name("Sehrish")  # "Sehrish" = argument

# Example:

def add(a, b):  # a and b are parameters
    return a + b


result = add(10, 20)  # 10 and 20 are arguments
print(result)

# ============================================================
# 3. RETURN VS PRINT
# ============================================================

# print() displays a value.
# return sends a value back to the caller.

def show_name():
    print("Sehrish")


def get_name():
    return "Sehrish"


show_name()
name = get_name()
print(name)

# A function without an explicit return returns None.

def greet_user(name):
    print("Hello", name)


result = greet_user("Sehrish")
print(result)

# Output:
# Hello Sehrish
# None

# ------------------------------------------------------------
# IMPORTANT:
# ------------------------------------------------------------

# print() → display something
# return → give something back to the caller
# return also immediately exits the function.

def check_age(age):
    if age >= 18:
        return "Adult"
    return "Minor"


print(check_age(21))

# ============================================================
# 4. USING RETURN FOR REUSABLE CALCULATIONS
# ============================================================

def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price


price = calculate_discount(1000, 20)
print(price)

# Why return is useful:
# The returned value can be:
# - stored
# - printed
# - used in another calculation
# - passed to another function

discounted_price = calculate_discount(1000, 20)
tax = discounted_price * 0.05
final_price = discounted_price + tax
print(final_price)

# ============================================================
# 5. POSITIONAL ARGUMENTS
# ============================================================

# Positional arguments are matched according to position.

def introduce(name, age):
    print(name)
    print(age)


introduce("Sehrish", 21)

# "Sehrish" → name
# 21        → age

# ============================================================
# 6. KEYWORD ARGUMENTS
# ============================================================

# Keyword arguments are matched using parameter names.

def introduce(name, age):
    print(name)
    print(age)


introduce(age=21, name="Sehrish")

# The order does not matter when using parameter names.

# ============================================================
# 7. DEFAULT PARAMETERS
# ============================================================

# A default parameter has a value that is used
# when the caller does not provide an argument.

def greet(name="User"):
    print("Hello", name)


greet("Sehrish")
greet()

# Output:
# Hello Sehrish
# Hello User

# ------------------------------------------------------------
# IMPORTANT RULE:
# A required parameter cannot come after a default parameter.
# ------------------------------------------------------------

# WRONG:
# def example(name="User", age):
#     pass

# CORRECT:

def example(age, name="User"):
    print(age, name)


# ============================================================
# 8. ARGUMENT ORDER RULES
# ============================================================

# Positional arguments must come before keyword arguments.

def student(name, age, city):
    print(name, age, city)


student("Sehrish", age=21, city="Lahore")

# This is invalid:
# student(name="Sehrish", 21, city="Lahore")

# ============================================================
# 9. *args
# ============================================================

# *args allows a function to receive an arbitrary number
# of positional arguments.

def show_numbers(*args):
    print(args)


show_numbers(10, 20, 30, 40)

# Output:
# (10, 20, 30, 40)

# IMPORTANT:
# *args is stored as a TUPLE.

# ============================================================
# 10. USING *args IN CALCULATIONS
# ============================================================

def calculate_total(*amounts):
    total = 0
    for amount in amounts:
        total += amount
    return total


result = calculate_total(500, 200, 300, 100)
print(result)

# 1100
# This is useful for an expense tracker because
# the number of expenses/amounts may vary.

# ============================================================
# 11. *args WITH NORMAL PARAMETERS
# ============================================================

def calculate(category, *amounts):
    total = sum(amounts)
    return category, total


result = calculate("Food", 500, 200, 300)
print(result)

# Output:
# ('Food', 1000)
# category → "Food"
# amounts → (500, 200, 300)

# ============================================================
# 12. **kwargs
# ============================================================

# **kwargs allows a function to receive an arbitrary number
# of keyword arguments.

def show_info(**kwargs):
    print(kwargs)


show_info(name="Sehrish", age=21)

# Output:
# {'name': 'Sehrish', 'age': 21}

# IMPORTANT:
# **kwargs is stored as a DICTIONARY.

# ============================================================
# 13. LOOPING THROUGH **kwargs
# ============================================================

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)


show_info(name="Sehrish", age=21, city="Lahore")

# Output:
# name = Sehrish
# age = 21
# city = Lahore

# ============================================================
# 14. **kwargs FOR EXPENSE DETAILS
# ============================================================

def add_expense(**expense):
    return expense


result = add_expense(category="Food", amount=500, description="Lunch")
print(result)

# Output:
# {
# 'category': 'Food',
# 'amount': 500,
# 'description': 'Lunch'
# }

# This is useful when an expense can have different
# named details.

# ============================================================
# 15. COMBINING NORMAL PARAMETERS + *args + **kwargs
# ============================================================

# General order:
# normal parameters
# *args
# **kwargs

def create_expense(category, amount, *tags, **details):
    return {
        "category": category,
        "amount": amount,
        "tags": tags,
        "details": details,
    }


expense = create_expense(
    "Food",
    500,
    "lunch",
    "office",
    description="Burger",
    payment_method="Cash",
)

print(expense)

# Result:
# {
# "category": "Food",
# "amount": 500,
# "tags": ("lunch", "office"),
# "details": {
# "description": "Burger",
# "payment_method": "Cash"
# }
# }

# Breakdown:
# category → "Food"
# amount   → 500
# *tags    → ("lunch", "office")
# **details → {"description": "Burger", "payment_method": "Cash"}

# ============================================================
# 16. * PACKING VS * UNPACKING
# ============================================================

# In a function definition, *args PACKS values into a tuple.

def numbers(*args):
    print(args)


numbers(1, 2, 3)

# At a function call, * can UNPACK an iterable.

def add_values(a, b, c):
    return a + b + c


values = [10, 20, 30]
result = add_values(*values)
print(result)

# 60

# ============================================================
# 17. ** UNPACKING
# ============================================================

def introduce(name, age):
    print(name, age)


person = {"name": "Sehrish", "age": 21}
introduce(**person)

# Dictionary keys must match the parameter names.

# ============================================================
# 18. VARIABLE SCOPE
# ============================================================

# Scope determines where a variable can be accessed.

# LOCAL SCOPE
# A variable created inside a function is local to that function.

def example():
    x = 10
    print(x)


example()

# x cannot normally be accessed outside the function.

# ============================================================
# 19. GLOBAL SCOPE
# ============================================================

x = 100


def show():
    print(x)


show()

# A function can READ a global variable.
# But assigning to a variable inside a function creates
# a local variable unless global is explicitly used.

x = 10


def change():
    x = 20
    print(x)


change()
print(x)

# Output:
# 20
# 10

# Recommended approach:
# Prefer passing values into functions and returning values
# instead of modifying global variables.

# ============================================================
# 20. LEGB RULE
# ============================================================

# Python searches for variables using:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in

# Search order:
# Local → Enclosing → Global → Built-in

# ============================================================
# 21. NESTED FUNCTIONS
# ============================================================

# A function can be defined inside another function.

def outer():
    def inner():
        print("Inside inner")

    inner()


outer()

# inner() exists inside outer()'s scope.

# ============================================================
# 22. CLOSURES
# ============================================================

# A closure happens when an inner function remembers
# variables from its enclosing function even after the
# outer function has finished executing.

def outer(message):
    def inner():
        print(message)

    return inner


greet = outer("Hello Sehrish")
greet()

# Output:
# Hello Sehrish
# inner() remembers the value of message.

# ============================================================
# 23. CLOSURE PRACTICAL EXAMPLE
# ============================================================

def multiplier(n):
    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)
triple = multiplier(3)
print(double(10))
print(triple(10))

# Output:
# 20
# 30
# double remembers n = 2
# triple remembers n = 3

# ============================================================
# 24. FUNCTIONS ARE OBJECTS
# ============================================================

# Functions are objects in Python.
# This means they can be:
# - assigned to variables
# - stored in lists
# - passed to other functions
# - returned from functions

def greet():
    print("Hello")


say_hello = greet
say_hello()

# greet and say_hello refer to the same function.

# IMPORTANT:
# greet → function object
# greet() → execute the function

# ============================================================
# 25. STORING FUNCTIONS IN A LIST
# ============================================================

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = [add, multiply]
print(operations[0](2, 3))
print(operations[1](2, 3))

# Output:
# 5
# 6

# ============================================================
# 26. HIGHER-ORDER FUNCTIONS
# ============================================================

# A higher-order function is a function that:
# 1. accepts another function as an argument
# OR
# 2. returns another function

def apply(operation, value):
    return operation(value)


def double_value(x):
    return x * 2


result = apply(double_value, 10)
print(result)

# Output:
# 20
# double_value is passed as a function object.
# apply() calls it using operation(value).

# ============================================================
# 27. FUNCTION RETURNING ANOTHER FUNCTION
# ============================================================

def multiplier(n):
    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)
print(double(10))

# multiplier() returns the multiply() function.

# ============================================================
# 28. LAMBDA FUNCTIONS
# ============================================================

# A lambda is a small anonymous function.
square = lambda x: x * x
print(square(5))

# Equivalent normal function:

def square_function(x):
    return x * x


print(square_function(5))

# Lambda is useful when a small function is needed temporarily.

# ============================================================
# 29. LAMBDA WITH SORTED()
# ============================================================

expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Transport", "amount": 200},
    {"category": "Shopping", "amount": 1000},
]

sorted_expenses = sorted(expenses, key=lambda expense: expense["amount"])
print(sorted_expenses)

# The lambda tells sorted() which value to use as the key.

# ============================================================
# 30. LAMBDA WITH FILTER()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Output:
# [2, 4, 6]

# ============================================================
# 31. LAMBDA WITH MAP()
# ============================================================

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)

# Output:
# [1, 4, 9, 16]

# ============================================================
# 32. FUNCTIONS + EXPENSE TRACKER
# ============================================================

# Functions allow us to divide an expense tracker
# into reusable responsibilities.

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Transport", "amount": 200},
    {"category": "Shopping", "amount": 1000},
]

total = calculate_total(expenses)
print(total)

# ============================================================
# 33. FILTER EXPENSES USING A FUNCTION
# ============================================================

def expensive_expenses(expenses, minimum_amount):
    result = []
    for expense in expenses:
        if expense["amount"] >= minimum_amount:
            result.append(expense)
    return result


result = expensive_expenses(expenses, 500)
print(result)

# ============================================================
# 34. SORT EXPENSES USING A LAMBDA
# ============================================================

sorted_expenses = sorted(
    expenses,
    key=lambda expense: expense["amount"],
    reverse=True,
)
print(sorted_expenses)

# ============================================================
# 35. FUNCTION DESIGN PRINCIPLES
# ============================================================

# Good functions should generally:
# 1. Have one clear responsibility.
# 2. Use meaningful names.
# 3. Accept required data through parameters.
# 4. Return useful results.
# 5. Avoid unnecessary global state.
# 6. Be reusable.
# 7. Be easy to test.

# Example:

def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


# This function:
# - receives data
# - processes data
# - returns a result
# - does not depend on global variables

# ============================================================
# 36. IMPORTANT FUNCTION RULES — QUICK REFERENCE
# ============================================================

# def → defines a function
# () → calls a function when placed after its name
# parameter → variable in function definition
# argument → actual value passed to function
# return → sends value back and exits function
# print → displays a value
# *args → arbitrary positional arguments, stored as tuple
# **kwargs → arbitrary keyword arguments, stored as dictionary
# * at function call → unpacks iterable
# ** at function call → unpacks dictionary
# local scope → variable inside function
# global scope → variable outside functions
# LEGB → Local → Enclosing → Global → Built-in
# nested function → function inside another function
# closure → inner function remembers enclosing variables
# higher-order function → accepts/returns another function
# lambda → small anonymous function

# ============================================================
# 37. FINAL FUNCTION EXAMPLE — COMBINING CONCEPTS
# ============================================================

def create_expense(category, amount, *tags, **details):
    return {
        "category": category,
        "amount": amount,
        "tags": tags,
        "details": details,
    }


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def filter_by_category(expenses, category):
    return [expense for expense in expenses if expense["category"] == category]


def sort_by_amount(expenses):
    return sorted(expenses, key=lambda expense: expense["amount"])


expenses = [
    create_expense(
        "Food",
        500,
        "lunch",
        description="Burger",
        payment_method="Cash",
    ),
    create_expense(
        "Transport",
        200,
        "office",
        description="Rickshaw",
        payment_method="Cash",
    ),
    create_expense(
        "Food",
        800,
        "dinner",
        description="Pizza",
        payment_method="Card",
    ),
]

print("Total:", calculate_total(expenses))
print("Food:", filter_by_category(expenses, "Food"))
print("Sorted:", sort_by_amount(expenses))

# ============================================================
# FUNCTIONS — TOPIC CHECKLIST
# ============================================================

# [x] Function definition
# [x] Function calling
# [x] Parameters
# [x] Arguments
# [x] return
# [x] print vs return
# [x] Positional arguments
# [x] Keyword arguments
# [x] Default parameters
# [x] Parameter ordering rules
# [x] *args
# [x] **kwargs
# [x] * unpacking
# [x] ** unpacking
# [x] Combining normal parameters + *args + **kwargs
# [x] Local scope
# [x] Global scope
# [x] LEGB
# [x] Nested functions
# [x] Closures
# [x] Functions as objects
# [x] Higher-order functions
# [x] Lambda functions
# [x] map()
# [x] filter()
# [x] sorted() with key
# [x] Function design principles
# [x] Expense-tracker function patterns

# ============================================================
# NEXT IN CURRENT INTERNSHIP PLAN
# ============================================================

# After Functions:
# 1. Exceptions
# 2. File I/O
# 3. Modules & Packages
# 4. Build CLI Expense Tracker reading/writing JSON
#
# Then:
# 5. OOP + dataclasses
# 6. Dunder methods
# 7. Type hints + mypy
# 8. Advanced Python
# - decorators
# - generators
# - context managers
# - async/await basics
# 9. pytest
#
# This follows the current 4-week internship plan.

# ============================================================
