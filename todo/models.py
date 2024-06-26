from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)