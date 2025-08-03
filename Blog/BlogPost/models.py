# models.py

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# views.py

from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import viewsets

class BlogPostView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer