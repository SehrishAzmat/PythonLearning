
-- Friday Deliverable 1: Database Schema
-- Database: MySQL 8.0+

CREATE DATABASE IF NOT EXISTS task_manager_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE task_manager_db;

-- Drop child tables before parent tables.
-- WARNING: Running this section again deletes existing table data.
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS users;

-- TABLE 1: USERS
CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- TABLE 2: PROJECTS
CREATE TABLE projects (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    owner_id INT UNSIGNED NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_projects_owner
        FOREIGN KEY (owner_id)
        REFERENCES users(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    INDEX idx_projects_owner_id (owner_id)
) ENGINE=InnoDB;

-- TABLE 3: TASKS
CREATE TABLE tasks (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    project_id INT UNSIGNED NOT NULL,
    assigned_to INT UNSIGNED NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    status ENUM('todo', 'in_progress', 'done')
        NOT NULL DEFAULT 'todo',
    priority ENUM('low', 'medium', 'high')
        NOT NULL DEFAULT 'medium',
    due_date DATE NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_tasks_project
        FOREIGN KEY (project_id)
        REFERENCES projects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_tasks_assignee
        FOREIGN KEY (assigned_to)
        REFERENCES users(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,

    INDEX idx_tasks_project_id (project_id),
    INDEX idx_tasks_assigned_to (assigned_to),
    INDEX idx_tasks_status (status),
    INDEX idx_tasks_due_date (due_date)
) ENGINE=InnoDB;

-- TABLE 4: COMMENTS
CREATE TABLE comments (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    task_id INT UNSIGNED NOT NULL,
    author_id INT UNSIGNED NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_comments_task
        FOREIGN KEY (task_id)
        REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_comments_author
        FOREIGN KEY (author_id)
        REFERENCES users(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    INDEX idx_comments_task_id (task_id),
    INDEX idx_comments_author_id (author_id)
) ENGINE=InnoDB;

-- SAMPLE DATA

INSERT INTO users (name, email) VALUES
('Ayesha Khan', 'ayesha@example.com'),
('Hamza Ali', 'hamza@example.com'),
('Sara Ahmed', 'sara@example.com');

INSERT INTO projects (name, description, owner_id) VALUES
('Expense Tracker', 'Track and review expenses.', 1),
('Task Manager', 'Manage projects and tasks.', 2);

INSERT INTO tasks
(project_id, assigned_to, title, description, status, priority, due_date)
VALUES
(1, 1, 'Design database schema',
 'Create four related tables.', 'done', 'high', '2026-10-12'),
(1, 2, 'Write SQL queries',
 'Practice joins and aggregation.', 'in_progress', 'high', '2026-10-18'),
(2, 2, 'Build task list',
 'Create the initial task list.', 'todo', 'medium', '2026-10-20'),
(2, 3, 'Review schema',
 'Check relationships and constraints.', 'todo', 'low', NULL);

INSERT INTO comments (task_id, author_id, body) VALUES
(1, 1, 'The first schema draft is ready.'),
(2, 2, 'I am practicing joins now.'),
(2, 3, 'Remember to test foreign keys.');

-- VERIFY TABLES
SHOW TABLES;

-- Inspect individual table structures if needed:
-- DESCRIBE users;
-- DESCRIBE projects;
-- DESCRIBE tasks;
-- DESCRIBE comments;
