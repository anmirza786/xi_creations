from core.models.staff_model import CustomStaff
from django.contrib import admin


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'image']


admin.site.register(CustomStaff, StaffAdmin)
