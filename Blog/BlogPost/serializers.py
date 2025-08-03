from rest_framework import serializers
from .models import BlogPost
import math

class BlogPostSerializer(serializers.ModelSerializer):
    read_time = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'read_time']

    def get_read_time(self, obj):
        content = obj.content or ""
        word_count = len(content.split())
        average_speed = 200
        read_time_minutes = math.ceil(word_count/average_speed)
        return f"{read_time_minutes} min read"