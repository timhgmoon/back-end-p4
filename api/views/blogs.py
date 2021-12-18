from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied

from ..serializers.blog import BlogSerializer
from ..models.blog import Blog

class BlogsView(APIView):

  def post(self, request):
    request.data['author'] = request.user.id
    blog = BlogSerializer(data=request.data)
    if blog.is_valid():
      blog.save()
      return Response(blog.data, status=status.HTTP_201_CREATED)
    return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request):
    blogs = Blog.objects.filter(author=request.user.id)
    data = BlogSerializer(blogs, many=True).data
    return Response(data)

#single blog
class BlogView(APIView):
    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        # Check the blog's author against the user making this request
        if request.user != blog.author:
            raise PermissionDenied('Unauthorized, you do not own this blog')
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if request.user != blog.author:
            raise PermissionDenied('Unauthorized, you do not own this blog')
        data = BlogSerializer(blog).data
        return Response(data)
    
    def patch(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        # Check the blog's author against the user making this request
        if request.user != blog.author:
            raise PermissionDenied('Unauthorized, you do not own this blog')
        # Ensure the author field is set to the current user's ID
        request.data['author'] = request.user.id
        updated_blog = BlogSerializer(blog, data=request.data)
        if updated_blog.is_valid():
            updated_blog.save()
            return Response(updated_blog.data)
        return Response(updated_blog.errors, status=status.HTTP_400_BAD_REQUEST)


