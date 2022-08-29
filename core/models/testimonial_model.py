from django.db import models


class Testimonial(models.Model):
    client = models.CharField(max_length=255, blank=False, null=False)
    company = models.CharField(max_length=255, blank=False, null=False)
    review = models.TextField(null=False, blank=False)
    client_picture = models.ImageField(
        upload_to='testimonials/clients', blank=False)
