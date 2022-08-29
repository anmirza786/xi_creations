from django.contrib import admin
from core.models import WorkCategory


class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryTitle']


admin.site.register(WorkCategory, WorkCategoryAdmin)
