from core.models import Work
from rest_framework import permissions
from core.serializers import WorkSerializer
from rest_framework.generics import ListAPIView

class WorkListApiView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WorkSerializer
    queryset = Work.objects.all()