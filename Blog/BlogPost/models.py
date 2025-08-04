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


# views.py

from .models import BlogPost
from .serializers import BlogPostSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BlogSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get("search", '')
        if query:
            posts = BlogPost.objects.filter(Q(title_icontains=query) | Q(content_icontains=query))
        else:
            posts = BlogPost.objects.none()
            serializers = BlogPostSerializer(posts, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)


# pagination.py

from rest_framework.pagination import PageNumberPagination

class CustomePageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


# view.py

from .pagination import CustomePageNumberPagination
from .serializers import BlogPostSerializer
from rest_framework.generics import ListAPIView

class BlogPostListView(ListAPIView):
    serializer_class = BlogPostSerializer
    pagination_class = CustomePageNumberPagination