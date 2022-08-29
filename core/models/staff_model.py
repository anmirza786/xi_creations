from django.db import models


class CustomStaff(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    designation = models.CharField(max_length=255, blank=False, null=False)
    image = models.FileField(upload_to='staff/images', null=False, blank=False)
