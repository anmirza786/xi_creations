from django.contrib import admin
from core.models import OurClient


class ClientAdmin(admin.ModelAdmin):
    list_display = ['logo', 'siteURL']


admin.site.register(OurClient, ClientAdmin)
