from core.models import Blog, BlogPictures
from django.contrib import admin


class BlogPictureAdmin(admin.TabularInline):
    model = BlogPictures
    extra = 0
    max_num = 3
    min_num = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        BlogPictureAdmin,
    ]
    list_display = [
        'title',
        'author',
        'updated_on',
        'created_on',
        'status'
    ]
    exclude = ['slug']
    list_filter = ("status",)
    search_fields = ['title', 'content']

    class Meta:
        model = Blog
