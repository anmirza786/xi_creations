from core.models import OurClient
from rest_framework import serializers


class OurClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurClient
        fields = '__all__'
