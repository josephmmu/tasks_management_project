from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

class Task(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task: {self.title} assigned to {self.assigned_to.username}"
