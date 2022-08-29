from core.models import WorkCategory
from rest_framework import serializers


class WorkCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkCategory
        fields = '__all__'