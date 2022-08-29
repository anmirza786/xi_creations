from core.models import Blog
from rest_framework import serializers
from .blogpictures_serializer import BlogPicturesSerializer


class BlogSerializer(serializers.ModelSerializer):
    blog_picture = BlogPicturesSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'smalldescription',
            'created_on',
            'blog_picture'
        ]
