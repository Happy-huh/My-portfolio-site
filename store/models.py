from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    date = models.DateField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    image =models.ImageField()
    description = models.TextField()
    github = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    video_link = models.CharField(max_length=200, blank=True, null=True)

    @property
    def image_url(self):
        if self.image:
            ans = self.image.url
        else:
            ans = ''
        return ans
