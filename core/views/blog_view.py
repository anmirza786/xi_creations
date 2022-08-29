from rest_framework import permissions
from core.models import Blog
from core.serializers import BlogSerializer
from rest_framework.generics import ListAPIView


class BlogsListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.filter(status=1)
        return queryset
