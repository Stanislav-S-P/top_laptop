from django.contrib import admin
from .models import Laptop


class LaptopAdmin(admin.ModelAdmin):
    """Класс - с настройками модели админ в админ-панели"""
    list_display = ('brand', 'title')
    list_display_links = ('brand', 'title')
    search_fields = ('brand', 'title')


admin.site.register(Laptop, LaptopAdmin)
