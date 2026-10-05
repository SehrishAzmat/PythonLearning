"""
CORE PYTHON DEEP DIVE
=====================

Topics covered:

1. Python Data Structures

   * Lists
   * Tuples
   * Sets
   * Dictionaries
   * Nested data structures
   * List of dictionaries
   * Navigating nested structures
   * Common data structure methods

2. Comprehensions

   * List comprehensions
   * Filtering
   * Transformation
   * Dictionary comprehensions
   * Set comprehensions
   * Conditional comprehensions

3. Practice Problems

   * Nested list/dictionary navigation
   * Modifying nested structures
   * List comprehension problems
   * Dictionary comprehension problems

These concepts will later be used in the CLI Expense Tracker,
which will store expense records and eventually read/write JSON.
"""

# ============================================================

# 1. LISTS

# ============================================================

"""
A list is:

* Ordered
* Mutable
* Allows duplicates
* Accessed using indexes
  """

expenses = [100, 250, 75, 500]

# Accessing an item

print(expenses[0])       # 100

# Modifying an item

expenses[1] = 300

# Adding one item

expenses.append(200)

# Removing an item by value

expenses.remove(75)

# Accessing the last item

print(expenses[-1])

# ------------------------------------------------------------

# Important list methods

# ------------------------------------------------------------

numbers = [10, 20, 30]

# append() adds ONE object

numbers.append(40)

# extend() adds multiple elements

numbers.extend([50, 60])

# insert() adds at a specific index

numbers.insert(1, 15)

# remove() removes by value

numbers.remove(30)

# pop() removes and returns an item

removed = numbers.pop()

# clear() removes everything

# numbers.clear()

# index() finds the position of a value

position = numbers.index(20)

# count() counts occurrences

count = numbers.count(20)

# sort() sorts the list

numbers.sort()

# reverse() reverses the list

numbers.reverse()

# copy() creates a copy

numbers_copy = numbers.copy()

# ============================================================

# 2. APPEND VS EXTEND

# ============================================================

numbers = [10, 20, 30]

# append() adds the entire object as ONE element

numbers.append([40, 50])

print(numbers)

# [10, 20, 30, [40, 50]]

numbers = [10, 20, 30]

# extend() adds each element individually

numbers.extend([40, 50])

print(numbers)

# [10, 20, 30, 40, 50]

# ============================================================

# 3. TUPLES

# ============================================================

"""
A tuple is:

* Ordered
* Immutable
* Allows duplicates

Use a tuple when the collection should not be modified.
"""

coordinates = (10, 20)

print(coordinates[0])

# This would cause an error because tuples are immutable:

#

# coordinates[0] = 50

# Tuple unpacking

def get_user():
    return "Sehrish", 7

name, semester = get_user()

print(name)
print(semester)

# ============================================================

# 4. SETS

# ============================================================

"""
A set:

* Stores unique values
* Does not support normal positional indexing
* Automatically removes duplicates
  """

numbers = {1, 2, 3, 4}

numbers_with_duplicates = {1, 2, 2, 3, 3, 4}

print(numbers_with_duplicates)

# {1, 2, 3, 4}

# ------------------------------------------------------------

# Practical example: unique values

# ------------------------------------------------------------

emails = [
"[a@gmail.com](mailto:a@gmail.com)",
"[b@gmail.com](mailto:b@gmail.com)",
"[a@gmail.com](mailto:a@gmail.com)",
"[c@gmail.com](mailto:c@gmail.com)"
]

unique_emails = set(emails)

print(unique_emails)

# ------------------------------------------------------------

# Set operations

# ------------------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

# Union

print(a | b)

# {1, 2, 3, 4, 5}

# Intersection

print(a & b)

# {3}

# Difference

print(a - b)

# {1, 2}

# Symmetric difference

print(a ^ b)

# {1, 2, 4, 5}

# ============================================================

# 5. DICTIONARIES

# ============================================================

"""
A dictionary stores data as:

key -> value
"""

user = {
"name": "Sehrish",
"semester": 7,
"role": "developer"
}

# Access value

print(user["name"])

# Modify value

user["semester"] = 8

# Add new key/value

user["city"] = "Lahore"

print(user)

# ============================================================

# 6. WHY DICTIONARIES ARE USEFUL

# ============================================================

"""
Compare these two representations.
"""

# Less descriptive

expense_as_list = ["Food", 500, "2026-10-05"]

# More descriptive

expense_as_dict = {
"category": "Food",
"amount": 500,
"date": "2026-10-05"
}

"""
With the list, we have to remember:

index 0 -> category
index 1 -> amount
index 2 -> date

With the dictionary:

"category" -> category
"amount"   -> amount
"date"     -> date
"""

# ============================================================

# 7. NESTED DATA STRUCTURES

# ============================================================

"""
A very common real-world structure is:

list
-> dictionary
-> list

For example:
"""

expenses = [
{
"id": 1,
"title": "Lunch",
"category": "Food",
"amount": 500
},
{
"id": 2,
"title": "Uber",
"category": "Transport",
"amount": 350
}
]

"""
Mental model:

expenses
|
+-- expense 1 -> dictionary
|
+-- expense 2 -> dictionary

This is a LIST OF DICTIONARIES.
"""

# ============================================================

# 8. NESTED DATA STRUCTURE PRACTICE

# ============================================================

students = [
{
"name": "Ali",
"age": 21,
"skills": ["Python", "SQL"]
},
{
"name": "Sara",
"age": 22,
"skills": ["JavaScript", "React"]
},
{
"name": "Ahmed",
"age": 20,
"skills": ["Python", "Django"]
}
]

# ------------------------------------------------------------

# Q1

# Get Sara's name

# ------------------------------------------------------------

answer_q1 = students[1]["name"]

print(answer_q1)

# Ali? No -> Sara

# ------------------------------------------------------------

# Q2

# Get Django

# ------------------------------------------------------------

answer_q2 = students[2]["skills"][1]

print(answer_q2)

# Django

# ------------------------------------------------------------

# Q3

# Get Sara's age

# ------------------------------------------------------------

answer_q3 = students[1]["age"]

print(answer_q3)

# 22

# ------------------------------------------------------------

# Q4

# What is the type of students?

# ------------------------------------------------------------

print(type(students))

# list

# More precisely:

# list of dictionaries

# ------------------------------------------------------------

# Q5

# What is the type of students[0]?

# ------------------------------------------------------------

print(type(students[0]))

# dict

# ------------------------------------------------------------

# Q6

# What is the type of students[0]["skills"]?

# ------------------------------------------------------------

print(type(students[0]["skills"]))

# list

# ------------------------------------------------------------

# Q7

# Add "Git" to Ahmed's skills

# ------------------------------------------------------------

students[2]["skills"].append("Git")

print(students[2]["skills"])

# ["Python", "Django", "Git"]

# ============================================================

# 9. UNDERSTANDING THE NAVIGATION PATH

# ============================================================

"""
When working with nested structures, follow the path
one step at a time.

students[2]["skills"][1]

means:

students
|
+-- [2]
|
+-- Ahmed's dictionary
|
+-- ["skills"]
|
+-- skills list
|
+-- [1]
|
+-- "Django"
"""

print(students[2])
print(students[2]["skills"])
print(students[2]["skills"][1])

# ============================================================

# 10. NESTED DICTIONARY + LIST PRACTICE

# ============================================================

company = {
"name": "TechCorp",
"employees": [
{
"name": "Ali",
"role": "Developer",
"languages": ["Python", "SQL"]
},
{
"name": "Sara",
"role": "Designer",
"languages": ["Figma", "HTML"]
}
]
}

# Q1

print(company["name"])

# TechCorp

# Q2

print(company["employees"][0]["name"])

# Ali

# Q3

print(company["employees"][1]["role"])

# Designer

# Q4

print(company["employees"][0]["languages"][1])

# SQL

# Q5

# Add JavaScript to Sara's languages

company["employees"][1]["languages"].append("JavaScript")

print(company["employees"][1]["languages"])

# ["Figma", "HTML", "JavaScript"]

# ============================================================

# 11. IDENTIFYING TYPES WHILE NAVIGATING

# ============================================================

"""
Question:

company["employees"]
company["employees"][0]
company["employees"][0]["languages"]

Answers:

1. list
2. dict
3. list
   """

print(type(company["employees"]))                    # list
print(type(company["employees"][0]))                # dict
print(type(company["employees"][0]["languages"]))   # list

# ============================================================

# 12. LIST COMPREHENSIONS

# ============================================================

"""
Normal loop:

numbers = [1, 2, 3, 4, 5]

result = []

for i in numbers:
result.append(i * 2)

List comprehension:

result = [i * 2 for i in numbers]
"""

numbers = [1, 2, 3, 4, 5]

result = [i * 2 for i in numbers]

print(result)

# [2, 4, 6, 8, 10]

# General pattern:

# [expression for item in iterable]

# ============================================================

# 13. NORMAL LOOP VS LIST COMPREHENSION

# ============================================================

numbers = [1, 2, 3, 4, 5]

# Normal loop

result = []

for i in numbers:
    result.append(i * 2)

print(result)

# List comprehension

result = [i * 2 for i in numbers]

print(result)

# Both produce:

# [2, 4, 6, 8, 10]

# ============================================================

# 14. FILTERING WITH LIST COMPREHENSIONS

# ============================================================

"""
Problem:

numbers = [1, 2, 3, 4, 5, 6]

Create:

[2, 4, 6]
"""

numbers = [1, 2, 3, 4, 5, 6]

# Normal loop

result = []

for i in numbers:
    if i % 2 == 0:
        result.append(i)

print(result)

# [2, 4, 6]

# List comprehension

result = [i for i in numbers if i % 2 == 0]

print(result)

# [2, 4, 6]

# General pattern:

# [expression for item in iterable if condition]

# ============================================================

# 15. TRANSFORMATION VS FILTERING

# ============================================================

"""
TRANSFORMATION

[i * 2 for i in numbers]

Every item is transformed.

1 -> 2
2 -> 4
3 -> 6
"""

numbers = [1, 2, 3]

result = [i * 2 for i in numbers]

print(result)

# [2, 4, 6]

"""
FILTERING

[i for i in numbers if i % 2 == 0]

Items are selected based on a condition.
"""

numbers = [1, 2, 3, 4]

result = [i for i in numbers if i % 2 == 0]

print(result)

# [2, 4]

# ============================================================

# 16. LIST COMPREHENSION WITH DICTIONARIES

# ============================================================

expenses = [
{"category": "Food", "amount": 500},
{"category": "Transport", "amount": 300},
{"category": "Food", "amount": 700},
{"category": "Shopping", "amount": 1000}
]

# Problem:

# Get the amounts of Food expenses.

food_amounts = [
expense["amount"]
for expense in expenses
if expense["category"] == "Food"
]

print(food_amounts)

# [500, 700]

# Important:

#

# expense["amount"]

# |

# +-- WHAT goes into the new list

#

# for expense in expenses

# |

# +-- WHERE the items come from

#

# if expense["category"] == "Food"

# |

# +-- WHICH items should be selected

# ============================================================

# 17. LIST COMPREHENSION — CATEGORY BY AMOUNT

# ============================================================

"""
Problem:

Give me the category of every expense
whose amount is greater than 400.
"""

result = [
expense["category"]
for expense in expenses
if expense["amount"] > 400
]

print(result)

# ["Food", "Food", "Shopping"]

# ============================================================

# 18. TRANSFORMATION + FILTERING

# ============================================================

"""
Problem:

Double the amount of every Food expense.

Expected:

[1000, 1400]
"""

result = [
expense["amount"] * 2
for expense in expenses
if expense["category"] == "Food"
]

print(result)

# [1000, 1400]

# ============================================================

# 19. DICTIONARY COMPREHENSIONS

# ============================================================

"""
Dictionary comprehension syntax:

{key: value for item in iterable}
"""

numbers = [1, 2, 3, 4]

squares = {
x: x * x
for x in numbers
}

print(squares)

# {

# 1: 1,

# 2: 4,

# 3: 9,

# 4: 16

# }

# ============================================================

# 20. DICTIONARY COMPREHENSION WITH EXPENSES

# ============================================================

expenses = [
{"category": "Food", "amount": 500},
{"category": "Transport", "amount": 300},
{"category": "Shopping", "amount": 1000}
]

result = {
expense["category"]: expense["amount"]
for expense in expenses
}

print(result)

# {

# "Food": 500,

# "Transport": 300,

# "Shopping": 1000

# }

# ============================================================

# 21. SET COMPREHENSION

# ============================================================

"""
Set comprehension:

{expression for item in iterable}

Example:
"""

amounts = {
expense["amount"]
for expense in expenses
}

print(amounts)

# {500, 300, 1000}

"""
Important distinction:

List comprehension:
[expression for item in iterable]

Set comprehension:
{expression for item in iterable}

Dictionary comprehension:
{key: value for item in iterable}
"""

# ============================================================

# 22. DICTIONARY COMPREHENSION WITH STUDENTS

# ============================================================

students = [
{"name": "Ali", "marks": 85},
{"name": "Sara", "marks": 92},
{"name": "Ahmed", "marks": 76}
]

students_dict = {
student["name"]: student["marks"]
for student in students
}

print(students_dict)

# {

# "Ali": 85,

# "Sara": 92,

# "Ahmed": 76

# }

# ============================================================

# 23. CONDITIONAL DICTIONARY COMPREHENSION

# ============================================================

students = [
{"name": "Ali", "marks": 85},
{"name": "Sara", "marks": 92},
{"name": "Ahmed", "marks": 76},
{"name": "Zain", "marks": 95}
]

"""
Problem:

Give me name -> marks only for students
whose marks are greater than 90.

Expected:

{
"Sara": 92,
"Zain": 95
}
"""

top_students = {
student["name"]: student["marks"]
for student in students
if student["marks"] > 90
}

print(top_students)

# {

# "Sara": 92,

# "Zain": 95

# }

# ============================================================

# 24. COMPREHENSION CHEAT SHEET

# ============================================================

"""
LIST

[expression for item in iterable]

LIST + FILTER

[expression for item in iterable if condition]

SET

{expression for item in iterable}

DICTIONARY

{key: value for item in iterable}

DICTIONARY + FILTER

{
key: value
for item in iterable
if condition
}
"""

# ============================================================

# 25. PROBLEM-SOLVING MENTAL MODEL

# ============================================================

"""
Whenever a nested structure confuses you:

DO NOT try to understand the whole expression at once.

Break it into steps.

Example:

students[2]["skills"][1]

Step 1:
students[2]

-> Ahmed's dictionary

Step 2:
students[2]["skills"]

-> Ahmed's skills list

Step 3:
students[2]["skills"][1]

-> second skill -> Django

For:

students[2]["skills"].append("Git")

Step 1:
students[2]

-> Ahmed's dictionary

Step 2:
students[2]["skills"]

-> Ahmed's skills list

Step 3:
.append("Git")

-> call append() on that list
"""

# ============================================================

# 26. DATA STRUCTURE SELECTION — QUICK GUIDE

# ============================================================

"""
LIST
Use when:

* order matters
* you need duplicates
* you need indexing
* you need a mutable collection

Example:
expenses = [expense1, expense2, expense3]

TUPLE
Use when:

* order matters
* data should not be modified

Example:
coordinates = (10, 20)

SET
Use when:

* uniqueness matters
* you need set operations

Example:
unique_emails = set(emails)

DICTIONARY
Use when:

* data has named fields
* you need key -> value relationships

Example:
expense = {
"category": "Food",
"amount": 500
}

LIST OF DICTIONARIES
Use when:

* you have multiple records
* each record has named fields

Example:
expenses = [
{"category": "Food", "amount": 500},
{"category": "Transport", "amount": 300}
]
"""

# ============================================================

# 27. PRACTICE PROBLEMS — RECAP

# ============================================================

"""
PROBLEM 1
Given:

students = [
{
"name": "Ali",
"age": 21,
"skills": ["Python", "SQL"]
},
{
"name": "Sara",
"age": 22,
"skills": ["JavaScript", "React"]
},
{
"name": "Ahmed",
"age": 20,
"skills": ["Python", "Django"]
}
]

Find:

1. Sara's name
2. Django
3. Sara's age
4. Type of students
5. Type of students[0]
6. Type of students[0]["skills"]
7. Add Git to Ahmed's skills
   """

"""
PROBLEM 2
Given:

company = {
"name": "TechCorp",
"employees": [
{
"name": "Ali",
"role": "Developer",
"languages": ["Python", "SQL"]
},
{
"name": "Sara",
"role": "Designer",
"languages": ["Figma", "HTML"]
}
]
}

Find:

1. company["name"]
2. company["employees"][0]["name"]
3. company["employees"][1]["role"]
4. company["employees"][0]["languages"][1]
5. Add JavaScript to Sara's languages
   """

"""
PROBLEM 3
Given:

numbers = [1, 2, 3, 4, 5]

Create:

[2, 4, 6, 8, 10]

First solve using a normal loop.
Then solve using a list comprehension.
"""

"""
PROBLEM 4
Given:

numbers = [1, 2, 3, 4, 5, 6]

Create:

[2, 4, 6]

Use a list comprehension.
"""

"""
PROBLEM 5
Given:

expenses = [
{"category": "Food", "amount": 500},
{"category": "Transport", "amount": 300},
{"category": "Food", "amount": 700},
{"category": "Shopping", "amount": 1000}
]

Create:

[500, 700]

Use a list comprehension.
"""

"""
PROBLEM 6

Using the same expenses list:

Give me the category of every expense
whose amount is greater than 400.

Correct result:

["Food", "Food", "Shopping"]
"""

"""
PROBLEM 7

Using the same expenses list:

Double the amount of every Food expense.

Correct result:

[1000, 1400]
"""

"""
PROBLEM 8

Using:

expenses = [
{"category": "Food", "amount": 500},
{"category": "Transport", "amount": 300},
{"category": "Shopping", "amount": 1000}
]

Create:

{
"Food": 500,
"Transport": 300,
"Shopping": 1000
}

Use a dictionary comprehension.
"""

"""
PROBLEM 9

Using:

students = [
{"name": "Ali", "marks": 85},
{"name": "Sara", "marks": 92},
{"name": "Ahmed", "marks": 76}
]

Create:

{
"Ali": 85,
"Sara": 92,
"Ahmed": 76
}

Use a dictionary comprehension.
"""

"""
PROBLEM 10

Using:

students = [
{"name": "Ali", "marks": 85},
{"name": "Sara", "marks": 92},
{"name": "Ahmed", "marks": 76},
{"name": "Zain", "marks": 95}
]

Create:

{
"Sara": 92,
"Zain": 95
}

Use a conditional dictionary comprehension.
"""

# ============================================================

# KEY TAKEAWAYS

# ============================================================

"""

1. LIST
   Ordered + mutable + duplicates allowed.

2. TUPLE
   Ordered + immutable.

3. SET
   Unique values + set operations.

4. DICTIONARY
   key -> value.

5. NESTED STRUCTURES
   A list can contain dictionaries.
   A dictionary can contain lists.
   Structures can be nested multiple levels deep.

6. NAVIGATION
   list -> [index]
   dictionary -> ["key"]

   Example:
   students[2]["skills"][1]

7. LIST COMPREHENSION

   [expression for item in iterable]

8. FILTERED LIST COMPREHENSION

   [expression for item in iterable if condition]

9. SET COMPREHENSION

   {expression for item in iterable}

10. DICTIONARY COMPREHENSION

    {key: value for item in iterable}

11. CONDITIONAL DICTIONARY COMPREHENSION

    {
    key: value
    for item in iterable
    if condition
    }

12. When debugging nested structures:
    Break the expression into smaller steps.

13. A very important real-world structure:

    expenses = [
    {
    "category": "Food",
    "amount": 500
    },
    {
    "category": "Transport",
    "amount": 300
    }
    ]

    This list-of-dictionaries structure will be used
    in the CLI Expense Tracker and eventually stored
    as JSON.
    """
