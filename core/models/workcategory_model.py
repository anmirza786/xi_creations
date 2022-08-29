from django.db import models


class WorkCategory(models.Model):
    categoryTitle = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.categoryTitle
