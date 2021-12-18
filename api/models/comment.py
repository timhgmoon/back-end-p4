from django.db import models
from django.contrib.auth import get_user_model
from .blog import Blog

class Comment(models.Model):
  name = models.CharField(max_length=15)
  content = models.CharField(max_length=120)
  blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
