# Python Learning

A personal Python learning and practice repository containing programming concepts, exercises, examples, and small projects developed while learning Python.

## 📁 Project Structure

```text
PythonLearning/
│
├── 01_Basics/
├── 02_Conditions/
├── 03_Loops/
├── 04_Functions/
├── 05_OOP/
├── 06_File_Handling/
│
├── .gitignore
└── README.md
```

## 🐍 Python Environment

* Python: 3.14.7
* Package Manager: pip
* IDE: Visual Studio Code
* Virtual Environment: `.venv`

The project uses a Python virtual environment to keep project dependencies isolated from the global Python installation.

The `.venv` directory is intentionally excluded from Git.

## 🚀 Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd PythonLearning
```

### 2. Create a virtual environment

Windows:

```cmd
python -m venv .venv
```

### 3. Activate the virtual environment

For Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

For PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Verify Python

```cmd
python --version
```

### 5. Open the project in VS Code

```cmd
code .
```

Select the project's `.venv` interpreter through:

```text
Ctrl + Shift + P
→ Python: Select Interpreter
→ PythonLearning\.venv\Scripts\python.exe
```

## 📚 Learning Topics

### 01 — Basics

Basic Python syntax and fundamental programming concepts.

Topics include:

* Python syntax
* Variables
* Data types
* Input and output
* Operators
* Type conversion
* Strings

### 02 — Conditions

Decision-making in Python.

Topics include:

* `if`
* `elif`
* `else`
* Comparison operators
* Logical operators
* Nested conditions

### 03 — Loops

Repetition and iteration.

Topics include:

* `for` loops
* `while` loops
* `range()`
* Nested loops
* `break`
* `continue`
* `pass`

### 04 — Functions

Reusable blocks of Python code.

Topics include:

* Defining functions
* Parameters
* Arguments
* Return values
* Default arguments
* Keyword arguments
* Scope
* Lambda functions

### 05 — Object-Oriented Programming

Object-oriented programming concepts in Python.

Topics include:

* Classes
* Objects
* Constructors
* Attributes
* Methods
* Encapsulation
* Inheritance
* Polymorphism

### 06 — File Handling

Working with files and stored data.

Topics include:

* Opening files
* Reading files
* Writing files
* Appending data
* File modes
* `with` statement
* Working with paths

## 🛠️ Development

All Python code is developed and tested locally using Visual Studio Code and the project's virtual environment.

Packages should be installed inside the active virtual environment using:

```cmd
python -m pip install <package-name>
```

The virtual environment itself should not be committed to Git.

## 🎯 Purpose

This repository is primarily used for:

* Learning Python
* Practicing programming concepts
* Maintaining coding exercises
* Experimenting with Python features
* Building small practice projects
* Tracking learning progress through Git

## 📌 Notes

This repository is a learning project and will evolve as new Python concepts and projects are added.
