from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from functools import wraps
from datetime import datetime, timedelta
import time


def rate_limit(requests=5, window=60):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            # Get client IP
            client_ip = request.META.get(
                "HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR")
            )
            cache_key = f"ratelimit_{client_ip}"

            # Get request history
            requests_history = cache.get(cache_key, [])
            now = datetime.now()

            # Clean old requests
            requests_history = [
                req_time
                for req_time in requests_history
                if now - req_time < timedelta(seconds=window)
            ]

            # Check if limit is exceeded
            if len(requests_history) >= requests:
                return JsonResponse(
                    {
                        "error": "Too many requests",
                        "message": f"Please wait {window} seconds before trying again",
                    },
                    status=429,
                )

            # Add current request timestamp
            requests_history.append(now)
            cache.set(cache_key, requests_history, window)

            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator


@rate_limit(requests=5, window=60)
def test_endpoint(request):
    return JsonResponse(
        {
            "message": "Success! This is a test endpoint",
            "timestamp": str(datetime.now()),
        }
    )
