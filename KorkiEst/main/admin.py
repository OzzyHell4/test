from django.contrib import admin
from .models import ProgLang, Course

@admin.register(ProgLang)
class ProgLangAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['progLang','name', 'slug', 'image', 'description', 'price', 'created', 'update']
    list_filter = ['created', 'update', 'progLang']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}

