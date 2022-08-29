from django.contrib import admin
from core.models import Work, WorkImage


class WorkImageAdmin(admin.TabularInline):
    model = WorkImage
    extra = 0
    max_num = 6
    min_num = 1


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    inlines = [
        WorkImageAdmin,
    ]
    list_display = ['title', 'client_name', 'date', 'category']
