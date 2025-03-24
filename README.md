# django-library-api

Library Management REST API.

## Project Setup

1. Clone the repo
2. Change working dir to project root:

```shell
cd library_api_project
```

3. Copy `library_api_project/.env.example` file and enter values into `library_api_project/.env` file:

- **PROJECT_SECRET_KEY** - project secret key

4. Run migrations

```shell
python manage.py migrate
```

5. Create superuser:

```shell
python manage.python creaetesuperuser
```

6. Run server:

```shell
python manage.py runserver
```