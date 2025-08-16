from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Blog_view(APIView):
    def get(request):
        # try-except block to error handle from database
        try:
            blog = Blog.objects.all()
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status_HTTP_200_OK)