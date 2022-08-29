from core.models import Work
from rest_framework import permissions
from core.serializers import SingleWorkSerializer
from rest_framework.generics import RetrieveAPIView


class SingleWorkApiView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SingleWorkSerializer
    queryset = Work.objects.all()
