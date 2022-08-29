import re
from ckeditor import fields
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateField(auto_now=True)
    content = fields.RichTextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    smalldescription = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def save(self):
        slug = self.title
        slug = slug.lower()
        slug = slug.replace(" ", "_")
        slug = re.sub("[^A-Za-z0-9]", "", slug)
        self.slug = slug
        return super().save()
