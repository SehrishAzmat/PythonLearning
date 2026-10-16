# Week 2 — Monday Study Guide
## HTTP, REST API Design, and Django Foundations

**Program:** 4-Week Plan — Intern to Professional Full Stack Python Developer

**Project:** `PythonLearning/Week2/task-manager-api`

**Deliverable:** A Django project with a `tasks` app, working starter endpoints, automated tests, and project documentation.

---

## 1. Learning Objectives

By completing this session, I should be able to:

- Explain how HTTP communication works between a client and server.
- Understand HTTP methods, status codes, headers, and response bodies.
- Describe REST API conventions and resource-based URLs.
- Differentiate a Django project from a Django app.
- Explain the purpose of the `config/` and `tasks/` directories.
- Understand Django URL routing and function-based views.
- Run and test a Django development server.
- Understand Django's built-in administration and authentication features.
- Interpret Django server logs.
- Apply basic Git and GitHub practices to the project.

## 2. Understanding HTTP

HTTP stands for Hypertext Transfer Protocol. It defines how clients and servers communicate over a network.

A client can be a browser, mobile application, or frontend application. A server receives the request, processes it, and returns a response.

In this project, Django acts as the backend server.

### 2.1 The HTTP Request-Response Cycle

When I open:

`http://127.0.0.1:8000/api/tasks/`

the following process occurs:

1. The browser sends an HTTP request.
2. Django receives the request.
3. Django checks its URL configuration.
4. The matching view function executes.
5. The view prepares the response.
6. Django sends the HTTP response to the browser.
7. The browser displays the returned data.

The process can be represented as:

```text
Client / Browser
       |
       | HTTP Request
       v
Django URL Configuration
       |
       v
Application View
       |
       v
HTTP Response
       |
       v
Client / Browser
```

### 2.2 HTTP Request Components

An HTTP request can contain the following parts:

| Component | Purpose |
|---|---|
| Method | Specifies the requested operation |
| URL/path | Identifies the requested resource |
| Headers | Provide metadata about the request |
| Body | Contains optional data sent to the server |

Example:

```http
GET /api/tasks/ HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json
```

Here:

- `GET` is the HTTP method.
- `/api/tasks/` is the requested path.
- `HTTP/1.1` is the protocol version.
- `Host` identifies the server.
- `Accept` indicates that the client can accept JSON.

### 2.3 Common HTTP Methods

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve data | Get all tasks |
| POST | Submit data, commonly to create a resource | Create a task |
| PUT | Replace an existing resource | Replace task details |
| PATCH | Partially update a resource | Change a task's status |
| DELETE | Delete a resource | Delete a task |

Example API operations:

```http
GET /api/tasks/
POST /api/tasks/
GET /api/tasks/1/
PATCH /api/tasks/1/
DELETE /api/tasks/1/
```

These are conventional examples of the API we will build. The current Monday project does not yet implement all these operations.

## 3. Understanding HTTP Status Codes

A status code communicates the outcome of an HTTP request.

### 3.1 Important Status Codes

| Status | Name | Meaning |
|---|---|---|
| 200 | OK | Request succeeded |
| 201 | Created | A resource was successfully created |
| 204 | No Content | Request succeeded without a response body |
| 301 | Moved Permanently | Resource is redirected to another URL |
| 400 | Bad Request | Request contains invalid data |
| 401 | Unauthorized | Valid authentication is missing or unavailable |
| 403 | Forbidden | Access is denied |
| 404 | Not Found | Requested route or resource does not exist |
| 405 | Method Not Allowed | HTTP method is not supported by the endpoint |
| 500 | Internal Server Error | Unexpected server-side error occurred |

A `401` response generally concerns authentication, while `403` concerns permission to perform an operation. Exact behavior depends on the API's authentication scheme.

### 3.2 Status Codes in My Project

My development server produced these responses:

```text
"GET /health/ HTTP/1.1" 200 58
"GET /favicon.ico HTTP/1.1" 404 2730
"GET /api/tasks HTTP/1.1" 301 0
"GET /api/tasks/ HTTP/1.1" 200 137
```

#### Health endpoint: 200

```text
"GET /health/ HTTP/1.1" 200 58
```

The health-check endpoint successfully returned a response. The response body was 58 bytes.

#### Favicon request: 404

```text
"GET /favicon.ico HTTP/1.1" 404 2730
```

Browsers commonly request a favicon, the small icon shown in a browser tab.

I have not configured a favicon at that path, so Django returned a 404 response. This does not indicate that the health endpoint is broken.

#### Task URL without a trailing slash: 301

```text
"GET /api/tasks HTTP/1.1" 301 0
```

The request omitted the final slash.

Django's usual `APPEND_SLASH` configuration can redirect a slashless URL to a matching URL that ends with a slash.

#### Task URL with a trailing slash: 200

```text
"GET /api/tasks/ HTTP/1.1" 200 137
```

The browser requested the correct route and received the JSON response.

For this project, I should use `/api/tasks/`.

### 3.3 What Do the Numbers at the End Mean?

Consider:

```text
"GET /api/tasks/ HTTP/1.1" 200 137
```

- `GET`: HTTP method.
- `/api/tasks/`: requested path.
- `HTTP/1.1`: protocol version.
- `200`: response status code.
- `137`: response body size in bytes.

The last number is not the number of tasks and is not the response time. It is the size of the response body reported by the development server.

Similarly, `58` is the body size for the health response, and `2730` is the body size for the 404 response.

The development server also displays a warning that it is not suitable for production. This is normal because `runserver` is intended for local development.

## 4. Understanding JSON

JSON stands for JavaScript Object Notation. It is a text format used to exchange structured data between applications.

Example:

```json
{
  "id": 1,
  "title": "Complete Django setup",
  "completed": false
}
```

This object contains three properties:

- `id`: identifies the task.
- `title`: stores the task title.
- `completed`: indicates whether the task is complete.

JSON supports strings, numbers, booleans, arrays, objects, and `null`.

Python uses `True`, `False`, and `None`; JSON uses `true`, `false`, and `null`.

Django's `JsonResponse` converts a Python dictionary into a JSON response.

## 5. Understanding REST API Design

REST stands for Representational State Transfer. It is an architectural style used to design networked applications.

REST-style APIs commonly organize URLs around resources and use HTTP methods to describe operations.

### 5.1 Resource-Based URLs

Examples of resources in a task-management application include:

- Users
- Projects
- Tasks

A conventional resource-based API might use:

| Resource | URL | Purpose |
|---|---|---|
| Task collection | `/api/tasks/` | List or create tasks |
| Individual task | `/api/tasks/1/` | Access task 1 |
| Project collection | `/api/projects/` | List or create projects |
| Individual project | `/api/projects/1/` | Access project 1 |

Prefer:

```http
GET /api/tasks/
```

over:

```http
GET /api/get-all-tasks/
```

The HTTP method already communicates that the request is retrieving data.

### 5.2 CRUD Operations

CRUD stands for Create, Read, Update, and Delete.

| Operation | Typical HTTP method |
|---|---|
| Create | POST |
| Read | GET |
| Update | PUT or PATCH |
| Delete | DELETE |

The Monday deliverable introduces the foundation for these operations. Full database-backed CRUD will be developed later.

## 6. Django Project vs Django App

A Django **project** contains the configuration for the overall website or backend system.

A Django **app** contains a particular area of functionality.

One project can contain multiple apps. For example, a larger task-management project might contain:

```text
config/
users/
projects/
tasks/
notifications/
```

In my current project:

- `config/` manages project-wide settings and routing.
- `tasks/` contains task-related functionality.
- `manage.py` provides command-line management commands.

## 7. Understanding the `config/` Directory

The `config/` directory was generated by Django when the project was created.

### 7.1 `config/settings.py`

This file contains the main project settings.

It controls:

- Installed applications.
- Middleware.
- Database configuration.
- Templates.
- Time zone and language.
- Static files.
- Security-related settings.

For example, the `tasks` application must be registered in `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tasks",
]
```

The exact configuration should retain the other settings generated by Django.

### 7.2 `config/urls.py`

This file contains the main URL configuration.

It can route requests directly or include the URL configuration of another app.

Example:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]
```

This means:

- `/admin/` is handled by Django admin.
- Other matching paths are delegated to `tasks.urls`.

### 7.3 `config/asgi.py`

ASGI stands for Asynchronous Server Gateway Interface.

This file exposes the Django application for ASGI-compatible servers.

### 7.4 `config/wsgi.py`

WSGI stands for Web Server Gateway Interface.

This file exposes the Django application for WSGI-compatible servers.

I generally do not need to edit either file during the initial exercises.

### 7.5 `config/__init__.py`

This file marks `config` as a Python package. It is normally empty in a newly generated Django project.

## 8. Understanding the `tasks/` Directory

The `tasks/` directory is the application responsible for task-related behavior.

### 8.1 `tasks/views.py`

Views receive HTTP requests and return HTTP responses.

Example:

```python
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "message": "Task Manager API is running",
        }
    )


@require_GET
def task_list(request):
    tasks = [
        {
            "id": 1,
            "title": "Complete Django setup",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Learn HTTP methods",
            "completed": True,
        },
    ]

    return JsonResponse({"tasks": tasks})
```

Important concepts:

- `JsonResponse` returns JSON.
- `@require_GET` restricts a view to GET requests.
- `request` represents the incoming HTTP request.
- The `return` statement sends a response back to Django.
- The sample list is currently hard-coded rather than loaded from a database.

### 8.2 `tasks/urls.py`

This file defines the routes for the tasks app.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health_check, name="health-check"),
    path("api/tasks/", views.task_list, name="task-list"),
]
```

The route names `health-check` and `task-list` let other parts of the application refer to these routes by name.

### 8.3 `tasks/models.py`

This file defines database models.

A model describes the fields and behavior of a type of data stored in the database.

For example, a future `Task` model may contain:

- Title.
- Description.
- Completion status.
- Creation timestamp.
- Assigned user.
- Associated project.

We will implement the actual models during Tuesday's session.

### 8.4 `tasks/tests.py`

This file contains automated tests for the application.

Tests can check whether:

- An endpoint returns the expected status.
- The response contains the correct JSON fields.
- A GET-only endpoint rejects POST requests.
- Future CRUD operations behave correctly.

### 8.5 `tasks/admin.py`

This file registers application models with Django's admin site.

For example, after creating a `Task` model, we could register it using:

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

This would allow authorized administrators to manage tasks through the admin interface.

Do not add this registration until the model exists.

### 8.6 `tasks/apps.py`

This file contains the Django app configuration class.

Django uses it to identify and configure the application.

### 8.7 `tasks/migrations/`

This directory stores migration files that describe database schema changes.

When a model is added or modified, Django can generate a migration describing the change.

### 8.8 `tasks/__init__.py`

This file marks the directory as a Python package. It is normally empty in a new application.

## 9. Understanding `manage.py`

`manage.py` is the command-line entry point for Django management tasks.

Common commands include:

```bat
python manage.py check
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py test tasks
python manage.py createsuperuser
```

Their purposes are:

| Command | Purpose |
|---|---|
| `check` | Checks the project for common configuration problems |
| `runserver` | Starts the local development server |
| `migrate` | Applies database migrations |
| `makemigrations` | Creates migration files from model changes |
| `test tasks` | Runs tests for the tasks app |
| `createsuperuser` | Creates an administrator account |

## 10. Understanding Django Admin

Django provides a built-in admin interface that can manage registered database models.

The standard Django project setup enables the admin app and exposes its route.

### 10.1 Why Users and Groups Appear

Django includes built-in authentication functionality.

Its standard installed applications include:

- `django.contrib.admin`
- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`

Running `python manage.py migrate` applies migrations for the installed apps and prepares their required database tables.

Migrations do not independently create the admin website. The admin application provides the interface, URL configuration exposes it, and database migrations prepare the data structures it needs.

### 10.2 Users

Django's built-in user model supports accounts and authentication.

Depending on the user model and configuration, its fields include a username, email address, password hash, active status, staff status, and superuser status.

Django does not store a user's raw password as plain text. Its password-handling system stores a password hash.

### 10.3 Groups

Groups collect permissions.

For example, an application might define a group for project managers and assign it permissions to manage particular models.

Users can then receive permissions through their group membership rather than having every permission assigned individually.

### 10.4 Important User Settings

| Setting | Meaning |
|---|---|
| Active | Whether the account is enabled |
| Staff status | Whether the user may access Django admin, subject to other checks |
| Superuser status | Grants all permissions |
| Groups | Permissions inherited through group membership |
| User permissions | Permissions assigned directly to the user |

Staff status alone does not grant every permission. Superusers have broader privileges.

Admin access is also different from access to a future frontend. The backend must enforce its own authentication and authorization rules for API requests.

### 10.5 What We Will Study Later

- Tuesday: models, migrations, and registering application models in admin.
- Wednesday: authentication, tokens, and API permissions.
- Thursday: validation and error handling.
- Friday: tests and review.

## 11. Database Migrations

Django models describe the structure of application data. Migrations translate model changes into database schema operations.

Two important commands are:

```bat
python manage.py makemigrations
python manage.py migrate
```

`makemigrations` creates migration files from detected model changes.

`migrate` applies pending migrations to the configured database.

These commands are related but not interchangeable.

The initial Django project typically uses SQLite. PostgreSQL will be introduced as part of the internship's database milestone.

## 12. Automated Tests

The Monday deliverable contains five tests for the health-check and task-list endpoints.

Example test structure:

```python
from django.test import TestCase
from django.urls import reverse


class HealthCheckTests(TestCase):
    def test_health_check_returns_success(self):
        response = self.client.get(reverse("health-check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")


class TaskListTests(TestCase):
    def test_task_list_returns_success(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, 200)

    def test_task_list_returns_two_tasks(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(len(response.json()["tasks"]), 2)

    def test_task_list_returns_expected_fields(self):
        response = self.client.get(reverse("task-list"))
        first_task = response.json()["tasks"][0]

        self.assertEqual(
            set(first_task.keys()),
            {"id", "title", "completed"},
        )

    def test_task_list_rejects_post(self):
        response = self.client.post(
            reverse("task-list"),
            data={"title": "New task"},
        )

        self.assertEqual(response.status_code, 405)
```

Run the tests with:

```bat
python manage.py test tasks
```

Expected result: five passing tests.

Django's test client simulates HTTP requests, so the development server does not need to be running during the test command.

## 13. Environment Setup

### Windows Command Prompt

Navigate to the project directory and activate the virtual environment:

```bat
cd C:\Users\SehrishAzmat\Downloads\PythonProjects\PythonLearning\Week2\task-manager-api
.venv\Scripts\activate.bat
```

Verify Python:

```bat
where python
python --version
python -m pip --version
```

The first `where python` result should point to the project's `.venv\Scripts\python.exe`.

Install dependencies if necessary:

```bat
python -m pip install "Django>=5.2,<6.0"
python -m pip freeze > requirements.txt
```

Run checks and tests:

```bat
python manage.py check
python manage.py migrate
python manage.py test tasks
```

Start the server:

```bat
python manage.py runserver
```

## 14. Git and GitHub

The project is inside the existing `PythonLearning` repository.

Check the repository root:

```bat
git rev-parse --show-toplevel
```

The output should point to the `PythonLearning` directory, not a nested repository inside `task-manager-api`.

Check pending changes:

```bat
git status
```

Review `.gitignore` to ensure that the virtual environment, local database, and secret files are not committed.

Commit only the intended changes and push them to the existing repository. If following a feature-branch workflow, create a branch and open a pull request.

## 15. Common Problems and Solutions

| Problem | What to check |
|---|---|
| Django is not recognized | Activate `.venv` and check the installation |
| `No module named django` | Check `where python` and install dependencies in the active environment |
| Endpoint returns 404 | Check URL patterns and trailing slashes |
| Endpoint returns 405 | Check whether the HTTP method is supported |
| Database table is missing | Run `python manage.py migrate` |
| Port 8000 is occupied | Run `python manage.py runserver 8001` |
| Favicon returns 404 | Usually harmless without a configured favicon |
| Git push fails | Check remote configuration, branch, authentication, and repository status |

When debugging, read the traceback carefully and locate the file and line where the error occurs before changing code.

## 16. Monday Completion Checklist

- [ ] Project and app directories exist.
- [ ] Virtual environment is active.
- [ ] Django is installed.
- [ ] `tasks` is registered in `INSTALLED_APPS`.
- [ ] Health endpoint returns HTTP 200.
- [ ] Task-list endpoint returns HTTP 200 and JSON.
- [ ] Initial database migrations are applied.
- [ ] All five automated tests pass.
- [ ] `README.md` is complete.
- [ ] `studyguide.md` is saved.
- [ ] `.gitignore` excludes local environment files.
- [ ] Changes are committed and pushed to the existing repository.
- [ ] Required pull request and daily log are complete.

## 17. Tuesday Preview — Django ORM and Models

Tuesday moves from sample data to real database-backed data.

Planned topics:

1. Django models and fields.
2. User, project, and task relationships.
3. `ForeignKey` and `ManyToManyField`.
4. Migrations and QuerySets.
5. `select_related()` and `prefetch_related()`.
6. Django admin for application models.
7. PostgreSQL configuration and integration.

The Tuesday deliverable is to create the users, projects, and tasks models in PostgreSQL and make them manageable through Django admin.

The Monday task-list endpoint currently returns hard-coded data. Replacing that sample data with database-backed operations is part of the upcoming work.

---

## Key Takeaways

1. HTTP defines how clients and servers communicate.
2. Status codes communicate the outcome of a request.
3. The final number in the Django request log represents the response-body size in bytes.
4. REST-style APIs organize endpoints around resources and use HTTP methods to express operations.
5. `config/` contains project-wide configuration; `tasks/` contains task-related application code.
6. URL patterns connect requests to views, and views return responses.
7. Django's built-in admin and authentication framework provide Users, Groups, and permission management.
8. Migrations prepare and update database structures.
9. Automated tests help verify that endpoints behave as expected.
10. Monday establishes the foundation; Tuesday introduces models, relationships, and PostgreSQL.

**End of Week 2 Monday Study Guide.**
