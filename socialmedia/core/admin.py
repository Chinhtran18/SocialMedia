from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        qs = qs.filter(is_superuser=False)
        return qs


admin.site.register(CustomUser, CustomUserAdmin)


