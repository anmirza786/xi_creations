from core.models import Testimonial
from rest_framework import serializers

class TestimonialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Testimonial
        fields = '__all__'