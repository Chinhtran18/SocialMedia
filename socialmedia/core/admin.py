from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import CustomUser, AlumniProfile, LecturerProfile

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        qs = qs.filter(is_superuser=False)
        return qs


admin.site.register(AlumniProfile)
admin.site.register(LecturerProfile)



