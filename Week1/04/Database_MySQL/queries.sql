
-- Friday Deliverable 2: SQL Queries
-- MySQL 8.0+
USE task_manager_db;

-- 1. SELECT: Display all users.
SELECT * FROM users;

-- 2. WHERE + ORDER BY: Show high-priority tasks.
SELECT id, title, status, priority, due_date
FROM tasks
WHERE priority = 'high'
ORDER BY due_date;

-- 3. INSERT: Add a new user.
-- Change the email if you run this more than once.
INSERT INTO users (name, email)
VALUES ('Noor Fatima', 'noor@example.com');

-- 4. UPDATE: Change a task's status.
UPDATE tasks
SET status = 'done'
WHERE id = 3;

-- 5. DELETE: Delete a comment.
-- Uncomment only when you want to delete the sample comment.
-- DELETE FROM comments WHERE id = 3;

-- 6. INNER JOIN: Show tasks with their project names.
SELECT
    t.id,
    t.title,
    p.name AS project_name
FROM tasks AS t
INNER JOIN projects AS p
    ON t.project_id = p.id;

-- 7. INNER JOIN: Show tasks with their assigned users.
SELECT
    t.title,
    u.name AS assigned_user,
    t.status
FROM tasks AS t
INNER JOIN users AS u
    ON t.assigned_to = u.id;

-- 8. LEFT JOIN: Show all users, including users without tasks.
SELECT
    u.name,
    t.title AS task_title
FROM users AS u
LEFT JOIN tasks AS t
    ON t.assigned_to = u.id
ORDER BY u.name;

-- 9. Multiple JOINs: Show comments, task titles, and authors.
SELECT
    c.id,
    t.title AS task_title,
    u.name AS comment_author,
    c.body
FROM comments AS c
INNER JOIN tasks AS t
    ON c.task_id = t.id
INNER JOIN users AS u
    ON c.author_id = u.id;

-- 10. GROUP BY: Count tasks by status.
SELECT
    status,
    COUNT(*) AS total_tasks
FROM tasks
GROUP BY status;

-- 11. GROUP BY + HAVING: Projects containing more than one task.
SELECT
    p.name AS project_name,
    COUNT(t.id) AS total_tasks
FROM projects AS p
LEFT JOIN tasks AS t
    ON p.id = t.project_id
GROUP BY p.id, p.name
HAVING COUNT(t.id) > 1;

-- 12. Aggregate functions: Overall task statistics.
SELECT
    COUNT(*) AS total_tasks,
    SUM(status = 'done') AS completed_tasks,
    AVG(status = 'done') * 100 AS completion_percentage
FROM tasks;

-- 13. Subquery: Find tasks in the Expense Tracker project.
SELECT title, status
FROM tasks
WHERE project_id = (
    SELECT id
    FROM projects
    WHERE name = 'Expense Tracker'
);

-- 14. Subquery: Find users assigned to at least one task.
SELECT id, name, email
FROM users
WHERE id IN (
    SELECT assigned_to
    FROM tasks
    WHERE assigned_to IS NOT NULL
);

-- 15. Date filtering: Find tasks due in the next 14 days.
SELECT title, due_date
FROM tasks
WHERE due_date BETWEEN CURRENT_DATE
                    AND DATE_ADD(CURRENT_DATE, INTERVAL 14 DAY)
ORDER BY due_date;

-- 16. CASE: Convert task statuses into readable labels.
SELECT
    title,
    CASE status
        WHEN 'todo' THEN 'Not started'
        WHEN 'in_progress' THEN 'In progress'
        WHEN 'done' THEN 'Completed'
    END AS status_label
FROM tasks;

-- 17. COUNT + GROUP BY: Count tasks assigned to each user.
SELECT
    u.name,
    COUNT(t.id) AS assigned_tasks
FROM users AS u
LEFT JOIN tasks AS t
    ON u.id = t.assigned_to
GROUP BY u.id, u.name
ORDER BY assigned_tasks DESC;

-- 18. Index inspection: View indexes on the tasks table.
SHOW INDEX FROM tasks;

-- 19. EXPLAIN: Inspect how MySQL plans a status-filter query.
EXPLAIN
SELECT id, title
FROM tasks
WHERE status = 'todo';

-- 20. Transaction: Insert a task and commit the change.
START TRANSACTION;

INSERT INTO tasks
    (project_id, assigned_to, title, status, priority)
VALUES
    (1, 1, 'Transaction practice task', 'todo', 'low');

COMMIT;

-- EXTRA PRACTICE: Roll back a comment insertion.
-- Run this complete block together.
START TRANSACTION;

INSERT INTO comments (task_id, author_id, body)
VALUES (1, 1, 'This comment will be rolled back.');

ROLLBACK;
