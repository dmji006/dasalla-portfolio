# Rate Limiting API

This project implements a custom rate limiting decorator for Django API endpoints that limits the number of incoming requests within a specific timeframe.

## API Endpoints

### Test Endpoint

- **Method**: GET
- **URL**: `/api/test/`
- **Rate Limit**: 5 requests per 60 seconds
- **Headers**:
  - No special headers required

#### Sample Response (Success - 200 OK)

```json
{
  "message": "Success! This is a test endpoint",
  "timestamp": "2025-05-06 12:00:00"
}
```

#### Sample Response (Rate Limit Exceeded - 429 Too Many Requests)

```json
{
  "error": "Too many requests",
  "message": "Please wait 60 seconds before trying again"
}
```

## Rate Limiting Details

- The rate limiting is implemented using client IP addresses
- Each client is limited to 5 requests per 60-second window
- The rate limit is enforced using Django's cache system
- When the rate limit is exceeded, the API returns a 429 status code

## Testing the Rate Limit

To test the rate limiting:

1. Make a GET request to `/api/test/`
2. Repeat the request quickly 6 times
3. After the 5th request within 60 seconds, you'll receive a 429 error
4. Wait 60 seconds for the rate limit window to reset
