from django.contrib import admin
from .models.user import User
from .models.blog import Blog
from .models.comment import Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Comment)
