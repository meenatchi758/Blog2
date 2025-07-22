from django.db import models
from django.contrib.auth.models import User

class Bug(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='bug_images/', blank=True, null=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
