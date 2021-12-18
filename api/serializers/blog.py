from rest_framework import serializers
from ..models.blog import Blog
from .comment import CommentSerializer

class BlogSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=False, partial=True)
  
  class Meta:
    model = Blog
    fields = ('id', 'title', 'content', 'comments', 'author')