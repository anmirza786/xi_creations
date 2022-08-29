from django.db import models
from .work_model import Work


class WorkImage(models.Model):
    work = models.ForeignKey(
        Work, related_name='work_image', null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to='work/images', null=False, blank=False)
