from django.db import models


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} - {self.text}'

