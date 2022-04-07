from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE)
    name  = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
