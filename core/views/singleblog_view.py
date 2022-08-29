from core.models import Blog
from rest_framework import permissions
from core.serializers import SingleBlogSerializer
from rest_framework.generics import RetrieveAPIView


class SingleBlogView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SingleBlogSerializer
    queryset = Blog.objects.all()
