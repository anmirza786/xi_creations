from rest_framework import permissions
from core.models import OurClient
from core.serializers import OurClientSerializer
from rest_framework.generics import ListAPIView


class OurClientView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OurClientSerializer

    def get_queryset(self):
        queryset = OurClient.objects.all()
        return queryset
