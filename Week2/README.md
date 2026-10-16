# Task Manager API

A Django backend project developed as part of the **4-Week Plan: Intern to Professional Full Stack Python Developer**.

**Current milestone:** Week 2 — Monday: HTTP, REST API Design, and Django Foundations.

## 1. Project Overview

The Task Manager API is the starting point for a backend application that will eventually support users, projects, and tasks.

The Monday milestone establishes the Django project structure, URL routing, JSON responses, initial endpoints, automated tests, and development workflow.

### Current Features

- Django project setup and configuration.
- A dedicated `tasks` application.
- Health-check endpoint.
- Task-list endpoint returning sample JSON data.
- URL routing between the project and application.
- Django's built-in administration interface.
- Initial database migrations.
- Automated tests for the endpoints.
- Project documentation and dependency management.

**Current limitation:** The task-list endpoint returns hard-coded sample data. Database-backed task management, CRUD operations, authentication, permissions, and PostgreSQL integration are planned for subsequent milestones.

## 2. Technology Stack

- **Language:** Python
- **Framework:** Django 5.2
- **Initial database:** SQLite
- **API response format:** JSON
- **Testing:** Django TestCase and test client
- **Version control:** Git and GitHub
- **Development environment:** Python virtual environment

## 3. Project Structure

```text
PythonLearning/
├── Week1/
├── Week2/
│   └── task-manager-api/
│       ├── config/
│       │   ├── __init__.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       ├── tasks/
│       │   ├── migrations/
│       │   ├── __init__.py
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── models.py
│       │   ├── tests.py
│       │   ├── urls.py
│       │   └── views.py
│       ├── .venv/
│       ├── .gitignore
│       ├── db.sqlite3
│       ├── manage.py
│       ├── requirements.txt
│       ├── README.md
└── README.md
```

The `.venv/` directory and `db.sqlite3` are local development files. They should be excluded from Git when appropriate.

The project lives inside the existing `PythonLearning` repository. A separate nested Git repository is not required.

## 4. File Responsibilities

| File or directory | Purpose |
|---|---|
| `config/settings.py` | Project settings, installed apps, middleware, and database configuration |
| `config/urls.py` | Main URL routing configuration |
| `config/asgi.py` | ASGI application entry point |
| `config/wsgi.py` | WSGI application entry point |
| `tasks/views.py` | Request handlers and JSON responses |
| `tasks/urls.py` | Routes for task-related endpoints |
| `tasks/models.py` | Database model definitions |
| `tasks/tests.py` | Automated endpoint tests |
| `tasks/admin.py` | Registration of application models in Django admin |
| `tasks/apps.py` | Application configuration |
| `tasks/migrations/` | Database schema migration files |
| `manage.py` | Command-line interface for Django management commands |
| `requirements.txt` | Python dependencies |

## 5. Prerequisites

Install the following before running the project:

- Python 3.12 or later.
- Git.
- Visual Studio Code or another code editor.
- Windows Command Prompt or PowerShell.

## 6. Local Setup

Run the commands from the `task-manager-api` directory.

### Step 1: Navigate to the project

```bat
cd C:\Users\SehrishAzmat\Downloads\PythonProjects\PythonLearning\Week2\task-manager-api
```

### Step 2: Activate the virtual environment

For Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

If the virtual environment does not exist yet, create it first:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

The terminal should display `(.venv)` before the current directory.

### Step 3: Install dependencies

If `requirements.txt` already exists:

```bat
python -m pip install -r requirements.txt
```

Otherwise, install Django and generate the file:

```bat
python -m pip install "Django>=5.2,<6.0"
python -m pip freeze > requirements.txt
```

### Step 4: Check the project

```bat
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

### Step 5: Apply database migrations

```bat
python manage.py migrate
```

This applies the migration files for Django's installed applications and prepares the database tables they require.

### Step 6: Run automated tests

```bat
python manage.py test tasks
```

The five Monday tests should pass.

### Step 7: Start the development server

```bat
python manage.py runserver
```

The local development server will normally be available at:

`http://127.0.0.1:8000/`

Press `CTRL+C` in the terminal to stop the server.

## 7. API Endpoints

| HTTP method | Endpoint | Purpose | Expected status |
|---|---|---|---|
| GET | `/health/` | Check application health | 200 OK |
| GET | `/api/tasks/` | Return the sample task list | 200 OK |
| GET | `/admin/` | Open Django administration | Login required |

### Health Check

**URL:** `http://127.0.0.1:8000/health/`

Example response:

```json
{
  "status": "ok",
  "message": "Task Manager API is running"
}
```

The health-check endpoint confirms that the application can receive a request and return a response.

### Task List

**URL:** `http://127.0.0.1:8000/api/tasks/`

Example response:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete Django setup",
      "completed": false
    },
    {
      "id": 2,
      "title": "Learn HTTP methods",
      "completed": true
    }
  ]
}
```

These are sample tasks defined in the view. They are not currently saved in the database.

**Note:** Use the trailing slash in `/api/tasks/`. Django's usual `APPEND_SLASH` configuration can redirect `/api/tasks` to `/api/tasks/` when a matching route exists.

## 8. Automated Testing

Run:

```bat
python manage.py test tasks
```

The five tests cover:

1. The health endpoint returns HTTP 200 and the expected status.
2. The task-list endpoint returns HTTP 200.
3. The task-list endpoint returns two sample tasks.
4. The task objects contain the expected fields.
5. The GET-only task-list endpoint rejects POST requests with HTTP 405.

The tests use Django's test client, so a separate development server does not need to be running.

## 9. Django Administration

Django provides a built-in admin interface and authentication framework.

To create an administrator account, if one does not already exist:

```bat
python manage.py createsuperuser
```

Then open:

`http://127.0.0.1:8000/admin/`

Django's built-in authentication models provide Users and Groups. Users represent accounts; groups collect permissions that can be assigned to multiple users.

The admin interface is available because the Django admin application is enabled and its URL is configured in `config/urls.py`. Migrations prepare the required database tables.

Our own task and project models will be introduced and registered in later milestones.

**Security:** Do not share administrator credentials or expose the development server publicly.

## 10. Git and GitHub Workflow

The project belongs to the existing `PythonLearning` repository.

From the `task-manager-api` directory, verify the repository root:

```bat
git rev-parse --show-toplevel
git status
```

The repository root should be the `PythonLearning` directory.

Do not initialize another Git repository inside `task-manager-api`.

After reviewing the changed files, commit the intended work. For example, from the repository root:

```bat
git add Week2/task-manager-api
git commit -m "docs: complete Week 2 Monday Django foundations"
git push
```

Use a feature branch and open a pull request if that is the workflow being followed for the internship. If the remote branch has not been configured, check `git remote -v` and the current branch before pushing.

Keep `.venv/`, local database files, and secrets out of Git. Check `.gitignore` and `git status` before committing.

## 11. Week 2 Roadmap

| Day | Planned focus | Main outcome |
|---|---|---|
| Monday | HTTP, REST, Django fundamentals, routes, views, and tests | Working starter project and endpoints |
| Tuesday | Django ORM, models, relationships, migrations, admin, and PostgreSQL | Users, projects, and tasks models |
| Wednesday | Django REST Framework, serializers, authentication, and permissions | Secured API operations |
| Thursday | Validation, filtering, pagination, configuration, and API documentation | More complete and maintainable API |
| Friday | Testing, coverage, code review, and introductory caching/background-task concepts | Tested and documented weekly deliverable |

These are planned learning milestones; features listed for later days are not necessarily implemented yet.

## 12. Monday Completion Checklist

- [ ] Django project and `tasks` app exist.
- [ ] Virtual environment is working.
- [ ] Django dependencies are recorded in `requirements.txt`.
- [ ] `tasks` is registered in `INSTALLED_APPS`.
- [ ] Health endpoint returns HTTP 200.
- [ ] Task-list endpoint returns the expected JSON.
- [ ] Initial database migrations have been applied.
- [ ] Five automated tests pass.
- [ ] `README.md` and `studyguide.md` are saved.
- [ ] `.gitignore` excludes local environment files.
- [ ] Changes are committed and pushed to the existing repository.
- [ ] The required pull request and daily log are complete.

## Author

Sehrish

## License

This is an internship learning project. Add a license if the project will be distributed as open-source software.
