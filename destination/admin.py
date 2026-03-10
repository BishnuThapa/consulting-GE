from django.contrib import admin
from .models import Destination
from django.utils.html import format_html
# Register your models here.


@admin.register(Destination)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'thumbnail', 'created_at', 'updated_at']

    prepopulated_fields = {
        'slug': ['title', ]
    }


    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="border-radius:5%;" />',
                obj.image.url
            )
        return "—"
