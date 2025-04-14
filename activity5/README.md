# Authentication API Documentation

This API provides user authentication functionality using JWT (JSON Web Tokens).

## Prerequisites

- Python 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt
- requests

## Installation

1. Install the required packages:

```bash
pip install djangorestframework djangorestframework-simplejwt requests
```

2. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## API Endpoints

### 1. User Registration

- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Request Body**:

```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "user123!@#",
  "password2": "user123!@#"
}
```

- **Success Response**:

```json
{
  "user": {
    "email": "user@example.com",
    "username": "username"
  },
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 2. User Login

- **URL**: `/api/auth/login/`
- **Method**: `POST`
- **Headers**: `Content-Type: application/json`
- **Request Body**:

```json
{
  "email": "user@example.com",
  "password": "user123!@#"
}
```

- **Success Response**:

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 3. Protected Routes

- **URL**: `/api/auth/protected/`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Bearer <access_token>`
- **Success Response**:

```json
{
  "message": "You are authenticated"
}
```

To access protected routes, include the JWT token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Error Responses

### 400 Bad Request

```json
{
  "error": "Invalid input data"
}
```

### 401 Unauthorized

```json
{
  "error": "Invalid credentials"
}
```

## Security Features

- Passwords are securely hashed using Django's built-in password hashing
- JWT tokens for stateless authentication
- Token expiration and refresh mechanism
- Password validation using Django's built-in validators

## Testing the API

You can test the API endpoints using any HTTP client like Postman, curl, or Python's requests library. Make sure to include the JWT token in the Authorization header for protected endpoints:

```
Authorization: Bearer <access_token>
```

### Example using curl

```bash
# Login and get token
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'

# Access protected endpoint with token
curl -X GET http://localhost:8000/api/auth/protected/ \
  -H "Authorization: Bearer <access_token>"
```

### Example using PowerShell

```powershell
# Login and get token
$loginBody = @{
    email = "user@example.com"
    password = "password123"
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://localhost:8000/api/auth/login/" `
    -Method POST `
    -Body $loginBody `
    -ContentType "application/json"

# Extract the access token from the response
$token = ($response.Content | ConvertFrom-Json).access

# Access protected endpoint with token
$headers = @{
    "Authorization" = "Bearer $token"
}

Invoke-WebRequest -Uri "http://localhost:8000/api/auth/protected/" -Headers $headers
```
