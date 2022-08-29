from unicodedata import category
from ckeditor import fields
from django.db import models
from .workcategory_model import WorkCategory


class Work(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    client_name = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateField(auto_now_add=False)
    category = models.ForeignKey(
        WorkCategory, related_name='work_cats', on_delete=models.SET_NULL, null=True)
    introduction = fields.RichTextField()
    description = models.TextField(blank=False, null=False)
    small_video = models.CharField(max_length=255, null=False, blank=False,
                                   verbose_name="Small video Link Id", help_text="Hint:    https://youtu.be/sENM2wA_FTg in this link after https://youtu.be/  is id of the video")
