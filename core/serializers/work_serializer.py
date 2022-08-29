from unicodedata import category
from core.models import Work
from rest_framework import serializers

from core.serializers.workcategory_serializer import WorkCategorySerializer
from .workimage_serializer import WorkImageSerializer


class WorkSerializer(serializers.ModelSerializer):
    work_image = WorkImageSerializer(read_only=True, many=True)
    category = WorkCategorySerializer(read_only=True)

    class Meta:
        model = Work
        fields = ['id',  'title', 'client_name', 'date',
                  'description', 'category', 'work_image']
