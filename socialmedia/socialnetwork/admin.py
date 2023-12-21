from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import User, AlumniProfile, Post, Survey, Notification, Question, Selection
# Register your models here.


class SocialNetworkAdminSite(admin.AdminSite):
    site_header = "Mạng Xã Hội Cựu Sinh Viên OU"

    def get_urls(self):
        return [

        ] + super().get_urls()

admin_site = SocialNetworkAdminSite(name='myadmin')


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'role']


class AlumniAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_id', 'confirmed']


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_date', 'active']
    form = PostForm


class QuestionInlineAdmin(admin.StackedInline):
    model = Question
    pk_name = 'survey'


class SelectionInlineAdmin(admin.StackedInline):
    model = Selection
    pk_name = 'question'


class QuestionAdmin(admin.ModelAdmin):
    inlines = [SelectionInlineAdmin]


class SurveyAdmin(admin.ModelAdmin):
    list_display = ['user']
    inlines = [QuestionInlineAdmin]


admin_site.register(User, UserAdmin)
admin_site.register(AlumniProfile, AlumniAdmin)
admin_site.register(Post)
admin_site.register(Survey, SurveyAdmin)
admin_site.register(Notification)
admin_site.register(Question, QuestionAdmin)
admin_site.register(Selection)