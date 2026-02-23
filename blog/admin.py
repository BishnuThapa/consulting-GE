from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.


class SeoInline(admin.TabularInline):
    model = Seo
    extra = 1
    max_num=1


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['title', 'thumbnail']

#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="150" height="100" style="border-radius:10%;" />'.format(object.image.url))

    # def has_add_permission(self, request, obj=None):
    #     return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    prepopulated_fields = {
        'slug': ['title', ]
    }
   
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'thumbnail', 'created_at', 'updated_at']
   
    prepopulated_fields = {
        'slug': ['title', ]
    }
    inlines = (SeoInline,)

    def thumbnail(self, object):
        return format_html('<img src="{}" width="100" height="80" style="border-radius:10%;" />'.format(object.image.url))