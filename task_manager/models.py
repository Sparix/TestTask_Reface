import re

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        related_name="workers"
    )

    def __str__(self):
        return f"User: {self.username}, Position: {self.position}"


def validate_hex_color(color):
    match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", color)
    if match:
        return color

    raise ValidationError(
        f"This {color} hex color is not valid"
    )


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=20, validators=[validate_hex_color])

    def __str__(self):
        return f"{self.name}, color: {self.color}"


CHOICES_PRIORITY = (
    ("URGENT", "Urgent"),
    ("HIGH", "High"),
    ("MEDIUM", "Medium"),
    ("LOW", "Low")
)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=CHOICES_PRIORITY)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ("deadline", "priority",)

    def __str__(self):
        return (
            f"Task name: {self.name}, "
            f"is complicated: {self.is_completed}, "
            f"Type task: {self.task_type}"
        )
