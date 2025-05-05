from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.shortcuts import get_object_or_404
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            project__owner=self.request.user
        ) | Task.objects.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        try:
            latest_project = Project.objects.filter(owner=self.request.user).latest(
                "id"
            )
            serializer.save(project=latest_project)
        except Project.DoesNotExist:
            raise ValidationError(
                "You need to create a project first before creating tasks."
            )

    def perform_update(self, serializer):
        if serializer.instance.project.owner != self.request.user:
            raise PermissionDenied("You don't have permission to modify this task.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.project.owner != self.request.user:
            raise PermissionDenied("You don't have permission to delete this task.")
        instance.delete()
