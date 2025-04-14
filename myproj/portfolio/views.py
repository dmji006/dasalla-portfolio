from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import status


# Create your views here.
def index(request):
    return render(request, "pages/portfolio.html")


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Return 401 Unauthorized if no valid token is provided
        # The authentication class will handle this automatically
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
