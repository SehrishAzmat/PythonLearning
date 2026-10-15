
# Friday SQL Deliverables — MySQL

## Overview

This folder contains the Friday SQL practice work for Week 1 of the Python learning plan. The database is implemented using MySQL 8.0+.

## Files

- `schema.sql` — creates the database, four tables, relationships, constraints, indexes, and sample data.
- `queries.sql` — contains 20 SQL practice queries.
- `friday_sql_fundamentals.py` — study notes for the SQL concepts covered on Friday.

## Database Design

The database is named `task_manager_db`.

### Tables

**1. users**

Stores user information:
- `id`: Primary key
- `name`: User's name
- `email`: Unique email address
- `created_at`: Account creation timestamp

**2. projects**

Stores project information:
- `id`: Primary key
- `name`: Project name
- `description`: Project details
- `owner_id`: Foreign key referencing `users.id`
- `created_at`: Creation timestamp

**3. tasks**

Stores tasks belonging to projects:
- `id`: Primary key
- `project_id`: Foreign key referencing `projects.id`
- `assigned_to`: Optional foreign key referencing `users.id`
- `title`: Task title
- `description`: Task details
- `status`: `todo`, `in_progress`, or `done`
- `priority`: `low`, `medium`, or `high`
- `due_date`: Optional deadline
- `created_at`: Creation timestamp

**4. comments**

Stores comments written on tasks:
- `id`: Primary key
- `task_id`: Foreign key referencing `tasks.id`
- `author_id`: Foreign key referencing `users.id`
- `body`: Comment content
- `created_at`: Creation timestamp

## Relationships

- One user can own multiple projects.
- One project can contain multiple tasks.
- One user can be assigned multiple tasks.
- A task can have no assigned user or one assigned user.
- One task can have multiple comments.
- One user can write multiple comments.

## SQL Concepts Practiced

The `queries.sql` file demonstrates:

1. `SELECT`, `WHERE`, and `ORDER BY`
2. `INSERT`, `UPDATE`, and `DELETE`
3. `INNER JOIN` and `LEFT JOIN`
4. Joining multiple tables
5. Aggregate functions: `COUNT`, `SUM`, and `AVG`
6. `GROUP BY` and `HAVING`
7. Subqueries
8. Date filtering with `DATE_ADD`
9. Conditional output with `CASE`
10. Primary keys and foreign keys
11. Index inspection with `SHOW INDEX`
12. Query-plan inspection with `EXPLAIN`
13. Transactions using `START TRANSACTION`, `COMMIT`, and `ROLLBACK`

## How to Run

### MySQL Workbench

1. Connect to your local MySQL server.
2. Open `schema.sql`.
3. Execute the script and verify the four tables.
4. Open `queries.sql`.
5. Execute the statements individually and inspect their results.

### MySQL command line

Run these commands from the folder containing the SQL files:

```bash
mysql -u root -p < schema.sql
mysql -u root -p task_manager_db < queries.sql
```

Replace `root` if your MySQL username is different.

## Design Notes

- Primary keys uniquely identify rows.
- Foreign keys maintain valid relationships between tables.
- `NOT NULL` ensures required values are provided.
- `UNIQUE` prevents duplicate email addresses.
- Indexes can help MySQL locate rows or perform joins more efficiently, but they also require storage and can slow down writes.
- Separating users, projects, tasks, and comments reduces unnecessary duplication and supports normalized relational design.

## Important Notes

- `schema.sql` drops and recreates its four tables. Running it again removes existing data in those tables.
- The sample data is for learning and testing only.
- Some queries change data. Review `INSERT`, `UPDATE`, and `DELETE` statements before running them.
- The transaction examples should be executed as complete blocks.

## Friday Completion Checklist

- [ ] Create and run the four-table schema.
- [ ] Verify the primary and foreign keys.
- [ ] Run and understand at least 15 SQL queries.
- [ ] Explain the difference between `WHERE` and `HAVING`.
- [ ] Explain `INNER JOIN` versus `LEFT JOIN`.
- [ ] Explain why normalization and indexes matter.
- [ ] Complete the Week 1 review.
- [ ] Complete a timed 60-minute Python + SQL coding task.
- [ ] Review the Expense Tracker code and tests.
- [ ] Commit and push the Friday folder to GitHub.

## Git Commands

From the root of your repository:

```bash
git add Friday/
git commit -m "Add Friday MySQL deliverables"
git push
```
