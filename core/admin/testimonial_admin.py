from django.contrib import admin
from core.models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client', 'company', 'review']


admin.site.register(Testimonial, TestimonialAdmin)
