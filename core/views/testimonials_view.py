from core.models import Testimonial
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from core.serializers import TestimonialSerializer


class TestimonialListApiView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()
