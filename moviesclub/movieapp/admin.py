from django.contrib import admin

from django.contrib import admin
from .models import movies

@admin.register(movies)
class crudadmin(admin.ModelAdmin):
    list_display= ["name","img","summary"]
