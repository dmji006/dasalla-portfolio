from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ("id", "title", "description", "owner", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="assigned_to"
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "project",
            "assigned_to",
            "assigned_to_id",
            "status",
            "due_date",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")
