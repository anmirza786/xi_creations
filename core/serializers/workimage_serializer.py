from dataclasses import fields
from core.models import WorkImage
from rest_framework import serializers


class WorkImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkImage
        fields = ['image', 'id']
