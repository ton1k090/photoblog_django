from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models
from django.contrib import admin

from .models import Biography, Photo


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'image']
    prepopulated_fields = {'slug': ('first_name',)}


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}


# @admin.register(models.Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'website', 'created_at']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image")
    readonly_fields = ("get_image",)
    prepopulated_fields = {'slug': ('name',)}


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="80"')