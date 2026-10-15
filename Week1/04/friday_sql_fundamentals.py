"""
Friday — SQL & Database Fundamentals
PythonLearning / Friday / friday_sql_fundamentals.py

Study notes for the Friday learning session in the four-week internship plan.

Note:
SQL examples in this file are strings for learning/reference. They are not executed
by Python. Run the SQL statements in PostgreSQL using psql or pgAdmin.
"""


def show_relational_database_basics() -> None:
    """Explain tables, rows, columns, and relational database terminology."""
    print("\n1. RELATIONAL DATABASE BASICS")
    print("-" * 32)
    print("A relational database stores structured data in related tables.")
    print("A table contains rows (records) and columns (fields).")
    print("SQL is the language used to define, retrieve, and modify relational data.")
    print("PostgreSQL is a relational database management system.")
    print("psql is PostgreSQL's interactive command-line client.")


def show_keys_and_constraints() -> None:
    """Show an example table definition with keys and constraints."""
    print("\n2. KEYS AND CONSTRAINTS")
    print("-" * 26)

    sql = """
CREATE TABLE users (
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE projects (
    project_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    name VARCHAR(150) NOT NULL
);
"""
    print(sql.strip())
    print("PRIMARY KEY: uniquely identifies a row.")
    print("FOREIGN KEY: links a row to a valid record in another table.")
    print("NOT NULL: requires a value.")
    print("UNIQUE: prevents duplicate values in the constrained column.")
    print("CHECK: enforces a condition on inserted or updated values.")


def show_crud_queries() -> None:
    """Demonstrate SQL Create, Read, Update, and Delete operations."""
    print("\n3. SQL CRUD")
    print("-" * 12)

    examples = {
        "CREATE (INSERT)": """
INSERT INTO expenses (category, amount)
VALUES ('Food', 500.00);
""",
        "READ (SELECT)": """
SELECT category, amount
FROM expenses
WHERE amount > 300
ORDER BY amount DESC;
""",
        "UPDATE": """
UPDATE expenses
SET amount = 550.00
WHERE expense_id = 1;
""",
        "DELETE": """
DELETE FROM expenses
WHERE expense_id = 1;
""",
    }

    for operation, sql in examples.items():
        print(f"\n{operation}:")
        print(sql.strip())

    print("\nCaution: UPDATE or DELETE without a suitable WHERE clause can affect")
    print("every row in the table.")


def show_joins() -> None:
    """Demonstrate INNER JOIN and LEFT JOIN."""
    print("\n4. SQL JOINS")
    print("-" * 13)

    inner_join = """
SELECT p.name AS project_name, u.name AS owner_name
FROM projects AS p
INNER JOIN users AS u
    ON p.user_id = u.user_id;
"""
    left_join = """
SELECT u.name AS user_name, p.name AS project_name
FROM users AS u
LEFT JOIN projects AS p
    ON u.user_id = p.user_id;
"""

    print("INNER JOIN — returns rows with matching records on both sides:")
    print(inner_join.strip())
    print("\nLEFT JOIN — preserves all left-side rows, using NULL for missing matches:")
    print(left_join.strip())


def show_aggregation() -> None:
    """Demonstrate aggregate functions, GROUP BY, and HAVING."""
    print("\n5. AGGREGATION")
    print("-" * 15)

    sql = """
SELECT category, SUM(amount) AS total_spent
FROM expenses
GROUP BY category
HAVING SUM(amount) > 500;
"""
    print(sql.strip())
    print("\nCOUNT() counts rows or non-NULL values.")
    print("SUM() adds numeric values; AVG() calculates an average.")
    print("MIN() and MAX() return minimum and maximum values.")
    print("WHERE filters rows before grouping; HAVING filters groups after grouping.")


def show_normalization() -> None:
    """Summarize the first three normal forms."""
    print("\n6. NORMALIZATION")
    print("-" * 17)
    print("1NF: keep each field atomic; avoid lists of repeated values in a cell.")
    print("2NF: satisfy 1NF and remove partial dependencies on part of a composite key.")
    print("3NF: satisfy 2NF and remove transitive dependencies of non-key attributes.")
    print("Normalization helps reduce redundant data and update, insertion, and deletion anomalies.")


def show_indexes() -> None:
    """Explain indexes and demonstrate creating one."""
    print("\n7. INDEXES")
    print("-" * 11)

    sql = """
CREATE INDEX idx_tasks_status
ON tasks(status);

EXPLAIN
SELECT *
FROM tasks
WHERE status = 'pending';
"""
    print(sql.strip())
    print("\nIndexes can speed up suitable searches, joins, or sorts.")
    print("They require storage and can add overhead to INSERT, UPDATE, and DELETE.")
    print("PostgreSQL chooses whether an index is useful for a particular query.")


def show_postgresql_commands() -> None:
    """List useful psql meta-commands and SQL examples."""
    print("\n8. POSTGRESQL AND PSQL")
    print("-" * 23)

    commands = [
        r"\l                 -- list databases",
        r"\c database_name   -- connect to a database",
        r"\dt                -- list tables",
        r"\d table_name      -- describe a table",
        r"\q                 -- exit psql",
    ]
    for command in commands:
        print(command)

    print("\nSQL examples:")
    print("SELECT current_database();")
    print("SELECT version();")
    print("psql meta-commands are not SQL statements.")


def show_transactions() -> None:
    """Demonstrate a basic SQL transaction."""
    print("\n9. TRANSACTIONS")
    print("-" * 16)

    sql = """
BEGIN;

UPDATE expenses
SET amount = 550.00
WHERE expense_id = 1;

COMMIT;
"""
    print(sql.strip())
    print("COMMIT makes the transaction's changes permanent.")
    print("ROLLBACK can undo uncommitted changes.")


def show_four_table_schema() -> None:
    """Print the four-table task-management schema used in Friday's lesson."""
    print("\n10. FOUR-TABLE SCHEMA")
    print("-" * 23)

    schema = """
CREATE TABLE users (
    user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE projects (
    project_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    name VARCHAR(150) NOT NULL
);

CREATE TABLE tasks (
    task_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id INTEGER NOT NULL REFERENCES projects(project_id),
    title VARCHAR(200) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    hours INTEGER NOT NULL DEFAULT 0 CHECK (hours >= 0)
);

CREATE TABLE comments (
    comment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    task_id INTEGER NOT NULL REFERENCES tasks(task_id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    content TEXT NOT NULL
);
"""
    print(schema.strip())


def main() -> None:
    """Print the Friday SQL study notes."""
    show_relational_database_basics()
    show_keys_and_constraints()
    show_crud_queries()
    show_joins()
    show_aggregation()
    show_normalization()
    show_indexes()
    show_postgresql_commands()
    show_transactions()
    show_four_table_schema()


if __name__ == "__main__":
    main()
