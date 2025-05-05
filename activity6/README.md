# TaskFlow API Documentation

TaskFlow is a simple task management platform that provides API endpoints for managing projects and tasks.

## Authentication

All endpoints require authentication. The API supports both token-based and session-based authentication.

To obtain an authentication token:

```
POST /api-token-auth/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

Use the token in subsequent requests:

```
Authorization: Token your_token_here
```

## API Endpoints

### Projects

#### List Projects

- **Method:** GET
- **URL:** `/api/projects/`
- **Headers:** Authorization required
- **Response:** List of projects accessible to the authenticated user

```json
[
  {
    "id": 1,
    "title": "Project Title",
    "description": "Project Description",
    "owner": {
      "id": 1,
      "username": "owner_username",
      "email": "owner@example.com"
    },
    "created_at": "2025-05-05T10:00:00Z",
    "updated_at": "2025-05-05T10:00:00Z"
  }
]
```

#### Create Project

- **Method:** POST
- **URL:** `/api/projects/`
- **Headers:**
  - Authorization required
  - Content-Type: application/json
- **Request Body:**

```json
{
  "title": "New Project",
  "description": "Project Description"
}
```

- **Response:** Created project object

#### Get Project Details

- **Method:** GET
- **URL:** `/api/projects/{id}/`
- **Headers:** Authorization required
- **Response:** Project details object

#### Update Project

- **Method:** PUT
- **URL:** `/api/projects/{id}/`
- **Headers:**
  - Authorization required
  - Content-Type: application/json
- **Request Body:**

```json
{
  "title": "Updated Title",
  "description": "Updated Description"
}
```

- **Response:** Updated project object

#### Delete Project

- **Method:** DELETE
- **URL:** `/api/projects/{id}/`
- **Headers:** Authorization required
- **Response:** 204 No Content

### Tasks

#### List Tasks

- **Method:** GET
- **URL:** `/api/tasks/`
- **Headers:** Authorization required
- **Response:** List of tasks accessible to the authenticated user

```json
[
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "project": {
      "id": 1,
      "title": "Project Title"
    },
    "assigned_to": {
      "id": 1,
      "username": "assigned_user",
      "email": "user@example.com"
    },
    "status": "TODO",
    "due_date": "2025-05-10T00:00:00Z",
    "created_at": "2025-05-05T10:00:00Z",
    "updated_at": "2025-05-05T10:00:00Z"
  }
]
```

#### Create Task

- **Method:** POST
- **URL:** `/api/tasks/`
- **Headers:**
  - Authorization required
  - Content-Type: application/json
- **Request Body:**

```json
{
  "title": "New Task",
  "description": "Task Description",
  "project": 1,
  "assigned_to": 1,
  "status": "TODO",
  "due_date": "2025-05-10T00:00:00Z"
}
```

- **Response:** Created task object

#### Get Task Details

- **Method:** GET
- **URL:** `/api/tasks/{id}/`
- **Headers:** Authorization required
- **Response:** Task details object

#### Update Task

- **Method:** PUT
- **URL:** `/api/tasks/{id}/`
- **Headers:**
  - Authorization required
  - Content-Type: application/json
- **Request Body:**

```json
{
  "title": "Updated Task",
  "description": "Updated Description",
  "status": "IN_PROGRESS",
  "due_date": "2025-05-15T00:00:00Z"
}
```

- **Response:** Updated task object

#### Delete Task

- **Method:** DELETE
- **URL:** `/api/tasks/{id}/`
- **Headers:** Authorization required
- **Response:** 204 No Content

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Successful request
- 201: Resource created
- 204: Resource deleted
- 400: Bad request (invalid data)
- 401: Unauthorized (invalid or missing authentication)
- 403: Forbidden (insufficient permissions)
- 404: Resource not found
- 500: Server error

Error responses include a message describing the error:

```json
{
  "error": "Error message description"
}
```
