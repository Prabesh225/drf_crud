from django.contrib import admin

from .models import *

@admin.register(students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'address')