# Tuesday Study Guide — Django ORM, Models, Relationships, and Admin

**Project:** Task Manager API  
**Learning Plan:** 4-Week Plan — Intern to Professional Full Stack Python Developer  
**Week:** 2  
**Day:** Tuesday  
**Database:** MySQL  
**Status:** Completed — foundational ORM and model-management work

---

## 1. Learning Objectives

The objectives for Tuesday were to understand how Django connects Python models to database tables and how related records can be managed through the Django ORM.

By completing this milestone, I practised:

- Understanding Django models and the ORM.
- Defining database fields and model relationships.
- Understanding `ForeignKey` and `ManyToManyField`.
- Applying database migrations.
- Creating and managing database records through the Django shell.
- Registering models in Django Admin.
- Creating and managing users, groups, projects, and tasks.
- Exploring task and project editing, including status changes.
- Identifying authorization issues that need to be addressed in subsequent milestones.

## 2. Understanding the Django ORM

ORM stands for **Object-Relational Mapper**.

The Django ORM allows Python code to interact with a relational database without requiring manually written SQL for every operation.

For example, instead of writing an SQL query to retrieve tasks, Django allows us to use:

```python
Task.objects.all()
```

Django translates ORM operations into database queries.

### Important ORM operations

Retrieve all records:

```python
Task.objects.all()
```

Retrieve one record using its primary key:

```python
Task.objects.get(pk=1)
```

Filter records:

```python
Task.objects.filter(status="todo")
```

Create a record:

```python
Task.objects.create(
    title="Learn Django ORM",
    # Include any other required fields.
)
```

Update an existing record:

```python
task = Task.objects.get(pk=1)
task.status = "in_progress"
task.save()
```

Delete a record:

```python
task = Task.objects.get(pk=1)
task.delete()
```

**Note:** These examples demonstrate ORM concepts. The actual fields and required relationships depend on the current model definitions. Do not run a creation example without supplying all required fields.

## 3. Django Models

A model is a Python class that describes a type of data stored in the database.

For example, a task model may define fields such as:

- Title
- Description
- Status
- Assigned user
- Related project
- Creation timestamp
- Due date or other time-related fields

Django uses model definitions to determine the database structure.

A simplified example:

```python
from django.db import models


class Example(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

Here:

- `models.Model` makes the class a Django model.
- `CharField` stores short text.
- `max_length` defines the maximum permitted text length.
- `DateTimeField` stores date and time information.
- `auto_now_add=True` records the creation time automatically.

This is a simplified teaching example, not a replacement for the actual Task Manager models.

## 4. Project and Task Models

The Task Manager application uses two central concepts.

### Project

A project groups related tasks together.

Depending on the configured model fields, a project can contain information such as:

- Name
- Description
- Owner
- Members
- Creation timestamp

### Task

A task represents an individual unit of work.

Depending on the configured fields, a task can contain:

- Name or title
- Description
- Status
- Assigned user
- Related project
- Time-related information

These models work together to represent the structure of a project-management application.

## 5. Model Relationships

Relational databases connect records using relationships. Django provides fields that represent these relationships.

### 5.1 ForeignKey — Many-to-One

A `ForeignKey` connects a record to another record.

For example, many tasks can belong to one project.

Conceptually:

```text
Project
  |
  | 1
  |
  |------ Task A
  |------ Task B
  |------ Task C
```

Each task references its associated project.

A simplified example:

```python
project = models.ForeignKey(
    Project,
    on_delete=models.CASCADE,
    related_name="tasks",
)
```

Important parts:

- `Project` is the model being referenced.
- `on_delete=models.CASCADE` specifies that deleting a project through the database relationship can cascade to its related tasks.
- `related_name="tasks"` provides a convenient reverse relationship.

For example, when the relationship is configured with this `related_name`:

```python
project.tasks.all()
```

retrieves the tasks associated with that project.

**Important security consideration:** `on_delete=models.CASCADE` is a database/model behaviour, not an authorization rule. The application must separately control who is allowed to delete projects.

### 5.2 ManyToManyField — Many-to-Many

A many-to-many relationship allows multiple users to belong to multiple projects.

For example:

```text
User A -------- Project 1
   |                |
   |                |
Project 2 -------- User B
```

A simplified field might look like:

```python
members = models.ManyToManyField(
    User,
    related_name="projects",
)
```

Django normally creates an intermediary database table to store the relationships.

This table records which users are members of which projects.

A many-to-many relationship is different from project ownership. Membership alone should not automatically grant every user permission to edit or delete a project.

## 6. Database Migrations

A migration represents a change to the database schema based on Django's model definitions.

Two important commands are:

```powershell
python manage.py makemigrations
```

and:

```powershell
python manage.py migrate
```

### `makemigrations`

This generates migration files describing detected model changes.

### `migrate`

This applies unapplied migrations to the configured database.

For example, when a new model is introduced, Django can generate a migration to create its corresponding database table.

Useful inspection command:

```powershell
python manage.py showmigrations
```

This shows migration files and whether Django considers them applied.

**Important:** Migration files and the physical database tables are related but not identical. A migration records a schema change; applying it changes the database.

## 7. Working with the Django Shell

Django provides an interactive Python shell connected to the configured project environment.

Start it with:

```powershell
python manage.py shell
```

For example, to inspect the current user model:

```python
from django.contrib.auth import get_user_model

User = get_user_model()

User.objects.values("id", "username", "is_superuser")
```

This returns selected fields from the user records.

To inspect projects:

```python
from tasks.models import Project

Project.objects.all()
```

To inspect tasks:

```python
from tasks.models import Task

Task.objects.all()
```

To leave the shell:

```python
exit()
```

### Common mistake: `NameError`

If code uses:

```python
owner=user
```

Python expects a variable named `user` to have been defined first.

A variable can be assigned by retrieving a user record:

```python
user = User.objects.get(username="your_username")
```

Replace `"your_username"` with an actual username in the current database.

This is different from writing a person's full name directly as Python code. Text values must be represented as strings, and model relationships generally require the related model instance or an appropriate identifier.

## 8. Django Admin

Django Admin provides an interface for managing database records.

The admin site can be accessed locally at:

```text
http://127.0.0.1:8000/admin/
```

A superuser account can be created using:

```powershell
python manage.py createsuperuser
```

An existing superuser does not need to be recreated if it already exists in the same database.

### Registering models

Application models must be registered with Django Admin if they are to appear there through the usual model-registration mechanism.

For example:

```python
from django.contrib import admin
from .models import Project, Task

admin.site.register(Project)
admin.site.register(Task)
```

This is a basic registration example. If the current `admin.py` already has customized `ModelAdmin` classes or registrations, preserve the existing implementation instead of duplicating it.

### Work completed

During Tuesday's practical work, I:

- Configured the project to work with MySQL.
- Resolved the missing MySQL database-driver issue.
- Applied database migrations.
- Registered and accessed project-related models through Django Admin.
- Created and managed users, groups, projects, and tasks.
- Ran the development server.
- Accessed the admin interface and explored the application-facing interface.
- Tested task and project editing, including changing task status.

## 9. Understanding Database Table Names

Django normally generates table names from the application label and model name.

For example:

```text
tasks.Task     -> tasks_task
tasks.Project  -> tasks_project
```

A many-to-many relationship may generate an intermediary table such as:

```text
tasks_project_members
```

The exact names depend on the model definitions, application labels, and any custom `db_table` configuration.

Tables such as `tasks`, `projects`, or `users` may have originated from earlier application work or from explicitly configured table names. A screenshot alone is not enough to establish their origin.

### How to investigate

Inspect:

- The model definitions.
- Each model's `Meta` class, especially `db_table`.
- The installed applications in `settings.py`.
- Migration files.
- The actual table structures in MySQL.

Do not delete or merge tables merely because their names appear similar. Confirm which application uses them and whether they contain required data first.

## 10. Important Security Findings

The project now supports editing tasks and projects through the interface, but working CRUD functionality does not automatically mean the application is secure.

One issue observed during testing is that a user could delete a project owned by the superuser.

This demonstrates the difference between authentication and authorization.

### Authentication

Determines which user is making a request.

### Authorization

Determines which actions that user is allowed to perform.

The application should eventually enforce rules such as:

- Users cannot assign projects to arbitrary owners through untrusted client input.
- Only authorized users can edit or delete projects.
- Task updates are restricted according to ownership, membership, or assigned permissions.
- The server validates permissions independently of what the interface displays.
- Administrative privileges are handled separately from ordinary user permissions.

These rules should be implemented and tested in the appropriate views, API endpoints, and permission classes.

**This security work remains a follow-up item; the presence of an owner field is not itself an authorization mechanism.**

## 11. Troubleshooting Notes

### Error: `No module named 'MySQLdb'`

Cause: The MySQL database driver required by Django was not available in the active environment.

Resolution: Install the appropriate `mysqlclient` package in the project's active virtual environment.

### Error: `Table 'task_manager_db.auth_user' doesn't exist`

Cause: Django attempted to query the user table before the required migrations had been applied to the configured database.

Resolution:

```powershell
python manage.py migrate
```

### Error: `NameError: name 'user' is not defined`

Cause: Code referenced a variable that had not been assigned.

Resolution: Retrieve the intended user record and assign it to a variable before using it.

### Unapplied migrations

Check migration status:

```powershell
python manage.py showmigrations
```

Apply migrations:

```powershell
python manage.py migrate
```

## 12. Useful Commands Reference

| Command | Purpose |
|---|---|
| `python manage.py check` | Check project configuration for common issues |
| `python manage.py makemigrations` | Generate migration files for model changes |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py showmigrations` | Inspect migration status |
| `python manage.py shell` | Open the Django interactive shell |
| `python manage.py createsuperuser` | Create an administrative account when needed |
| `python manage.py runserver` | Start the development server |
| `python manage.py test tasks` | Run tests in the tasks application |

Run commands from the project directory with the intended virtual environment activated.

## 13. Tuesday Completion Checklist

- [x] Django ORM concepts explored.
- [x] Project and task models used.
- [x] Database relationships explored.
- [x] MySQL configured and connected.
- [x] Required migrations applied.
- [x] Users, groups, projects, and tasks managed through Django Admin.
- [x] Development server started successfully.
- [x] Project and task editing explored.
- [x] Task status changes tested.
- [x] Database table naming confusion identified for further inspection.
- [ ] Project ownership and deletion permissions secured.
- [ ] Automated tests added for the relevant model and permission behaviours.
- [ ] Changes committed and pushed to the existing PythonLearning repository.

## 14. Key Takeaways

1. Django models define how application data is represented.
2. The ORM allows Python code to query and modify relational data.
3. `ForeignKey` represents a many-to-one relationship.
4. `ManyToManyField` represents a many-to-many relationship.
5. Migrations describe and apply database schema changes.
6. Django Admin provides a convenient interface for managing registered models.
7. A working interface does not automatically provide secure authorization.
8. Database tables should be investigated before renaming or deleting them.
9. The same Task Manager API project will be extended throughout Week 2 rather than recreated each day.

---

**Next milestone:** Continue with Django REST Framework, API serializers, authentication, and permissions, with particular attention to preventing unauthorized project and task operations.
