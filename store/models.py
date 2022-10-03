from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()

