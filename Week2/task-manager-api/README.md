# Task Manager API

A learning project built during **Week 2** of the *4-Week Plan: Intern
to Professional Full Stack Python Developer*.

The goal of this README is to help me understand the backend codebase:
where things live, how a request moves through Django, what each
directory and file is responsible for, and how the project is growing
each day.

**Current database:** MySQL\
**Project location:** `PythonLearning/Week2/task-manager-api/`\
**Approach:** One project for the whole week. Each daily milestone
extends this codebase.

------------------------------------------------------------------------

## 1. How the Backend Fits Together

A backend receives a request, decides what code should handle it, may
read or change data in the database, and returns a response.

In this Django project, the flow is generally:

``` text
Client / Browser
      |
      | HTTP request
      v
config/urls.py
      |
      | routes request to the relevant app
      v
tasks/urls.py
      |
      v
tasks/views.py
      |
      | uses models / ORM when database data is needed
      v
tasks/models.py  <---->  MySQL database
      |
      v
HTTP response (HTML or JSON, depending on the view)
      |
      v
Client / Browser
```

Not every request follows every step. For example, a simple health-check
view may return a response without querying the database.

### What each part means

-   **URL configuration** decides which view handles a request.
-   **A view** contains the request-handling logic.
-   **A model** describes a type of data and its database relationships.
-   **The Django ORM** lets Python code query and update the database.
-   **MySQL** stores the persistent records.
-   **Templates**, if used, render HTML pages.
-   **Serializers**, when introduced with Django REST Framework, will
    validate and convert data for API requests and responses.
-   **Authentication and permissions** determine who is making a request
    and what that person is allowed to do.

------------------------------------------------------------------------

## 2. Project Directory Guide

The project is inside the existing `PythonLearning` Git repository. We
use the same `task-manager-api` directory throughout Week 2 instead of
creating a new project for each day.

``` text
PythonLearning/
├── Week1/
├── Week2/
│   └── task-manager-api/
│       ├── config/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   ├── asgi.py
│       │   └── wsgi.py
│       ├── tasks/
│       │   ├── migrations/
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── models.py
│       │   ├── tests.py
│       │   ├── urls.py
│       │   └── views.py
│       ├── manage.py
│       ├── requirements.txt
│       ├── studyguide.md
│       └── README.md
└── README.md
```

This is the main structure, not an exhaustive listing. Additional files
or directories may be added as the project grows.

### `config/` --- project-wide configuration

  -----------------------------------------------------------------------
  File                    Responsibility          When I might open it
  ----------------------- ----------------------- -----------------------
  `settings.py`           Installed apps,         When configuring MySQL,
                          middleware, database    adding Django REST
                          connection, templates,  Framework, or changing
                          and other project       project settings
                          settings                

  `urls.py`               Main URL routing;       When adding or tracing
                          connects top-level      a URL
                          paths to views or app   
                          URL configurations      

  `asgi.py`               ASGI application entry  When working with
                          point                   ASGI-compatible
                                                  deployment or
                                                  asynchronous serving

  `wsgi.py`               WSGI application entry  When working with a
                          point                   WSGI-compatible
                                                  deployment
  -----------------------------------------------------------------------

### `tasks/` --- application code

  -----------------------------------------------------------------------
  File or directory       Responsibility          When I might open it
  ----------------------- ----------------------- -----------------------
  `models.py`             Defines data models,    When changing projects,
                          fields, and             tasks, status choices,
                          relationships           or relationships

  `views.py`              Handles requests and    When changing what
                          returns responses       happens after a request
                                                  reaches the application

  `urls.py`               Maps app-specific URL   When adding or tracing
                          paths to views          task/project routes

  `admin.py`              Registers models and    When changing how
                          configures their Django models appear in
                          Admin presentation      `/admin/`

  `tests.py`              Automated tests for the When checking that
                          app                     behaviour continues to
                                                  work after changes

  `apps.py`               Application             When inspecting Django
                          configuration           app setup

  `migrations/`           Files that describe     When reviewing changes
                          database schema changes generated by
                                                  `makemigrations`
  -----------------------------------------------------------------------

As API work grows, additional files may be introduced---for example,
`serializers.py`, `permissions.py`, or other modules. Their
responsibilities will be documented here when they are added.

### Files at the project root

  -----------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- -----------------------------------
  `manage.py`                         Runs Django management commands
                                      such as `runserver`, `migrate`, and
                                      `test`

  `requirements.txt`                  Records Python package dependencies

  `studyguide.md`                     Detailed learning notes for a
                                      particular lesson or day

  `README.md`                         Project navigation guide, setup
                                      instructions, and the ongoing Week
                                      2 progress log

  `.gitignore`                        Specifies local or generated files
                                      Git should ignore
  -----------------------------------------------------------------------

The `.venv/` directory, credentials, secrets, and local-only database
files should not be committed accidentally.

------------------------------------------------------------------------

## 3. How to Navigate a Feature Through the Code

When I want to understand or change a feature, I should follow its path
through the backend rather than opening files randomly.

For example, to investigate a task-related URL:

1.  Open `config/urls.py` to see how top-level URLs are connected.
2.  Open `tasks/urls.py` to find the app route, if the route is defined
    there.
3.  Open `tasks/views.py` to inspect the function or class handling the
    request.
4.  If it reads or changes stored data, inspect the relevant model in
    `tasks/models.py`.
5.  Check `admin.py` if the behaviour concerns Django Admin.
6.  Check `tests.py` and run the relevant tests after changing the code.

The exact path depends on how the route is currently implemented. As the
project evolves, some responsibilities may move into additional modules.

### Common development commands

Run these from the `task-manager-api` directory with the project's
virtual environment activated.

``` powershell
# Check Django project configuration
python manage.py check

# See which migrations are applied
python manage.py showmigrations

# Generate migration files after changing models
python manage.py makemigrations

# Apply migrations to the configured database
python manage.py migrate

# Open the Django interactive shell
python manage.py shell

# Run tests for the tasks app
python manage.py test tasks

# Start the local development server
python manage.py runserver
```

Open the local server at `http://127.0.0.1:8000/` and Django Admin at
`http://127.0.0.1:8000/admin/`, when the corresponding routes are
configured.

Only create a superuser if an appropriate account does not already exist
in the database configured for this project.

------------------------------------------------------------------------

## 4. Database and Model Notes

The project uses Django models and the ORM with MySQL.

-   A **model** describes the fields and relationships for a type of
    record.
-   A **QuerySet** represents a database query that can retrieve or
    filter records.
-   A **ForeignKey** commonly represents many records related to one
    record---for example, tasks belonging to a project.
-   A **ManyToManyField** represents a relationship where multiple
    records can be connected on both sides---for example, project
    membership.
-   A **migration** records a database schema change and can apply that
    change to the configured database.

### Understanding table names

Django commonly derives table names from the app label and model name. A
`Task` model in the `tasks` app normally maps to `tasks_task`; a
`Project` model normally maps to `tasks_project`. A many-to-many
relationship may create a separate intermediary table.

The MySQL schema also shows tables named `tasks` and `projects`. Their
origin has not yet been confirmed. Before renaming or deleting any
table, inspect `tasks/models.py`, any model `Meta.db_table` settings,
the migration files, and the database configuration. Similar names alone
do not prove that tables are duplicates.

------------------------------------------------------------------------

## 5. Current Behaviour and Known Follow-ups

The following reflects what has been explored during the learning
sessions; run the project and tests to verify the current checkout.

-   The Django development server runs.
-   Django Admin is accessible.
-   Users, groups, projects, and tasks have been managed through the
    admin interface.
-   The current interface allows editing projects and tasks.
-   Task editing includes changing the status and other available
    fields.
-   MySQL is configured and migrations have been applied.

### Important issue: project permissions

Testing showed that a user could delete a project owned by the
superuser. This is an authorization flaw that still needs to be
addressed.

A working edit/delete interface does not by itself make an operation
secure. The server must verify who is making the request and whether
that user is allowed to perform the operation. Project creation must
also prevent users from assigning projects to arbitrary owners without
appropriate permission.

This will be a focus of the upcoming authentication and permissions
work.

### Other follow-up

The origins and use of similarly named MySQL tables still need to be
checked before any database cleanup.

------------------------------------------------------------------------

## 6. Week 2 Direction

The week builds on one codebase, with each day adding another layer of
backend understanding and implementation.

  --------------------------------------------------------------------------------
  Day               Focus                     How it builds on   Status
                                              the project        
  ----------------- ------------------------- ------------------ -----------------
  Monday            HTTP, REST concepts,      Established the    Completed
                    Django project/app        Django project and 
                    structure, URLs, views,   request/response   
                    JSON responses, initial   foundations        
                    tests                                        

  Tuesday           Django ORM, models,       Added and explored Completed
                    relationships,            database-backed    
                    migrations, MySQL, and    project/task       
                    Django Admin              management         

  Wednesday         Django REST Framework,    Develop API        Next
                    serializers,              operations and     
                    authentication, and       address            
                    permissions               authorization      

  Thursday          Validation, filtering,    Make API behaviour Planned
                    pagination,               more reliable and  
                    configuration, and API    easier to use      
                    documentation                                

  Friday            Testing, coverage, code   Verify the week's  Planned
                    review, and introductory  work and improve   
                    caching/background-task   maintainability    
                    concepts                                     
  --------------------------------------------------------------------------------

The status should be updated only after each milestone's work has been
implemented and checked.

------------------------------------------------------------------------

## 7. Week 2 Daily Progress Log

This section records **what changed, what was learned, what remains, and
what comes next**. Keep previous entries and append or update the next
day's section as the same project develops.

### Monday --- Django Foundations

**Status:** Completed

**Focus:** HTTP and REST foundations, Django project and app structure,
URL routing, views, JSON responses, initial endpoint tests, and
development workflow.

**Progress recorded:** - Created and configured the Django project and
`tasks` application. - Added initial health-check and task-list
endpoints. - Explored URL routing and request/response behaviour. -
Added initial automated endpoint tests. - Set up project documentation
and dependencies.

**What this established:** The basic structure of a Django backend and
the path from a URL to a view and its response.

**Next:** Add database-backed models and learn how Django represents
relationships between records.

### Tuesday --- Django ORM and Models

**Status:** Completed

**Focus:** ORM, models, relationships, migrations, MySQL, and Django
Admin.

**Progress recorded:** - Connected Django to MySQL and resolved the
missing MySQL driver. - Applied the required database migrations. -
Worked with the `Project` and `Task` models and their configured
relationships. - Registered and managed models through Django Admin. -
Created and managed users, groups, projects, and tasks. - Tested project
and task editing, including task status changes. - Identified table
names in MySQL that need further investigation.

**What this established:** How Django models map to database tables, how
related records are represented, and how stored records can be managed
through Django.

**Outstanding:** - Enforce project ownership and prevent unauthorized
project deletion. - Confirm the origin of similarly named MySQL tables
before changing them. - Add or review automated tests for model
behaviour and permissions.

**Study notes:** See `studyguide.md`.

**Next:** Introduce Django REST Framework and build API operations with
authentication and server-side permissions.

### Wednesday --- Django REST Framework

**Status:** Planned --- update after completing the work.

**Record during the day:** - What concepts were studied: - What files or
features changed: - Commands and tests run: - What was verified: -
Issues still open: - Commit or GitHub update:

### Thursday --- Validation and API Quality

**Status:** Planned --- update after completing the work.

**Record during the day:** - What concepts were studied: - What files or
features changed: - Commands and tests run: - What was verified: -
Issues still open: - Commit or GitHub update:

### Friday --- Testing and Weekly Review

**Status:** Planned --- update after completing the work.

**Record during the day:** - What concepts were studied: - What files or
features changed: - Commands and tests run: - What was verified: -
Issues still open: - Commit or GitHub update:

------------------------------------------------------------------------

## 8. Current Project Snapshot

**Completed:** Monday's Django foundations and Tuesday's ORM, models,
relationships, migrations, MySQL, and admin work.

**Current priorities:** 1. Add server-side authorization for project and
task operations. 2. Investigate the origin of similarly named MySQL
tables without deleting data prematurely. 3. Build on the existing
project with Django REST Framework. 4. Add and run automated tests as
new behaviour is introduced.

**Next step:** Wednesday --- serializers, API endpoints, authentication,
and permissions.

Update this snapshot as the week progresses.

------------------------------------------------------------------------

## Author

Sehrish

## License

This is an internship learning project. Add a license if the project
will be distributed as open-source software.