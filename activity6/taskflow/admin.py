from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "assigned_to", "status", "due_date")
    search_fields = ("title", "description")
    list_filter = ("status", "due_date", "created_at")
