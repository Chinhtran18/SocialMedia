from django.contrib import admin
from .models import User, Alumni, Lecturer

# Register your models here.


class AlumniAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name']


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Lecturer, LecturerAdmin)