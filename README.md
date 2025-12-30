This repository contains practice code from the book [Django for APIs](https://learndjango.com/courses/django-for-apis/), 5th edition.

[![](https://github.com/asarkar/django-for-apis/workflows/CI/badge.svg)](https://github.com/asarkar/django-for-apis/actions)

## Table of Contents

1. Initial Set up
2. Web APIs
3. [Library Website](ch03/)
4. [Library API](ch04/)
5. [Todo API](ch05/)
6. Todo Vue Frontend
7. [Blog API](ch07/)
8. [Permissions](ch08/)
9. [User Authentication](ch09/)
10. [Viewsets and Routers](ch10/)
11. [Schemas and Documentation](ch11/)

## API Endpoints

### Library API

| Method | Endpoint  | Description    |
|--------|-----------|----------------|
| GET    | `/`       | List all books |

### TODO API

| Method | Endpoint  | Description     |
|--------|-----------|-----------------|
| GET    | `/`       | List all TODOs  |
| GET    | `/{id}/`  | Retrieve a TODO |

### Blog Endpoints

| Method | Endpoint                            | Description            |
|--------|-------------------------------------|------------------------|
| GET    | `/`                                 | List all posts         |
| GET    | `/{id}/`                            | Retrieve a post        |
| GET    | `/users/`                           | List all users         |
| GET    | `/users/{id}/`                      | Retrieve a user        |
| POST   | `/rest-auth/registration`           | Register a new user    |
| POST   | `/rest-auth/login`                  | Log in a user          |
| GET    | `/rest-auth/logout`                 | Log out a user         |
| POST   | `/rest-auth/password/reset`         | Request password reset |
| POST   | `/rest-auth/password/reset/confirm` | Confirm password reset |

## Development

### Setup

```bash
# Install dependencies
uv sync

# Activate virtual environment (optional, uv run handles this)
source .venv/bin/activate
```

### Running a Chapter

```bash
# Run migrations
uv run --directory <chapter> manage.py migrate

# Start development server
uv run --directory <chapter> manage.py runserver
```

Example:
```bash
uv run --directory ch03 manage.py migrate
uv run --directory ch03 manage.py runserver
```

### Running Tests

```bash
# Run tests for a specific chapter
uv run --directory <chapter> manage.py test

# Or use the CI script
./.github/run.sh <chapter>
```

Example:
```bash
uv run --directory ch03 manage.py test
./.github/run.sh ch03
```
