from core.models import CustomStaff
from rest_framework import permissions
from core.serializers import StaffSerializer
from rest_framework.generics import ListAPIView

class StaffListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StaffSerializer
    queryset = CustomStaff.objects.all()