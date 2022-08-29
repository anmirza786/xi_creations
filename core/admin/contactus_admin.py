from django.contrib import admin
from core.models import Contact

class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False
    readonly_fields = ['email', 'message']
    list_display = ['email', 'name', 'message']


admin.site.register(Contact, ContactAdmin)