from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name