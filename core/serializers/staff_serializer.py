from core.models import CustomStaff
from rest_framework import serializers

class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomStaff
        fields = '__all__'