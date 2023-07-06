from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)



