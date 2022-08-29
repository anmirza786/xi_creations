from django.db import models


class OurClient(models.Model):
    logo = models.ImageField(upload_to='clients', blank=False, null=False,help_text="Upload a black and white png with no background in it and the logo in white.")
    siteURL = models.URLField(blank=False, null=False)
