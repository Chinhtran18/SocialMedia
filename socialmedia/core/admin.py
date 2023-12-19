from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.html import mark_safe

from .models import CustomUser, AlumniProfile, LecturerProfile, Post

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar', 'cover_images']

    def avatar(self, user):
        if user:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'.format(url=user.image.name)
            )


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostForm


class AlumniAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'user', 'is_student']
    search_fields = ['student_id', 'user.username']


admin.site.register(CustomUser, UserAdmin)
admin.site.register(AlumniProfile, AlumniAdmin)
admin.site.register(LecturerProfile)
admin.site.register(Post)



