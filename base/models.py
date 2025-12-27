from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

def default_deadline():
    return timezone.now() + timedelta(hours=24)


class Task(models.Model):

    PRIORITY_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    )

    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,  blank=True)

    deadline = models.DateTimeField(default=default_deadline, null=True, blank=True)

    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default="Medium")

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    