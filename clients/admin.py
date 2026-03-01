from django.contrib import admin
from .models import Client
from django.utils.html import format_html   
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 
                    'is_active', 'created_at', 'updated_at')
    list_editable = ('is_active', )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" style="border-radius:5%;" />',
                obj.image.url
            )
        return "—"
