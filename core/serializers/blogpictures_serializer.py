from core.models import BlogPictures
from rest_framework import serializers


class BlogPicturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPictures
        fields = ['id', 'picture']
