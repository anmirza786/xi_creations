from django.db import models
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False,
                            verbose_name="Name")
    email = models.EmailField(blank=False, null=False,
                              verbose_name="Email Address")
    message = models.TextField(blank=False, null=False, verbose_name="Message")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
