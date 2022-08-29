from django.db import models
from core.models import Blog


class BlogPictures(models.Model):
    blog = models.ForeignKey(
        Blog, related_name='blog_picture', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(
        upload_to='blogPicturses', null=False, blank=False)
