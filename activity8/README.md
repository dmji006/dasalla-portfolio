# User Registration API with Photo Upload

This API provides endpoints for user registration, authentication, and profile management with photo upload capabilities.

## API Endpoints

### 1. User Registration

- **URL:** `/api/register/`
- **Method:** POST
- **Content-Type:** multipart/form-data
- **Request Body:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "photo": "file (optional)"
  }
  ```
- **Response (201 Created):**
  ```json
  {
    "token": "string",
    "user": {
      "id": "integer",
      "username": "string",
      "email": "string",
      "photo": "string (URL)"
    }
  }
  ```

### 2. User Login

- **URL:** `/api/login/`
- **Method:** POST
- **Content-Type:** application/json
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "token": "string",
    "user": {
      "id": "integer",
      "username": "string",
      "email": "string",
      "photo": "string (URL)"
    }
  }
  ```

### 3. User Profile

- **URL:** `/api/profile/`
- **Method:** GET
- **Authentication:** Required (Token)
- **Headers:**
  ```
  Authorization: Token <token_string>
  ```
- **Response (200 OK):**
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string",
    "photo": "string (URL)"
  }
  ```

## File Upload Constraints

- Supported image formats: JPEG, PNG, WebP
- Maximum file size: 2MB
- Images will be automatically cropped to 1:1 aspect ratio
