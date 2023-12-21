from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatars')
    cover_image = models.ImageField(upload_to='users/cover_images')
    role_choices = [('alumni', 'Alumni'),
                    ('lecturer', 'Lecturer'),
                    ('admin', 'Admin')]
    role = models.CharField(max_length=20, choices=role_choices)

    def save(self, *args, **kwargs):
        super().save()


class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'student_id')


class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='group_members')


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = RichTextField()


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = RichTextField()


class Reaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reaction_set')
    reaction_types = [('like', 'Like'),
                      ('love', 'Love'),
                      ('haha', 'Haha')]

    type = models.CharField(max_length=10, choices=reaction_types, null=True)

    def __str__(self):
        return self.type


class Survey(Post):
    pass


class Question(BaseModel):
    content = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')


class Selection(models.Model):
    content = models.TextField()
    is_selected = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='selections')


class SurveyResponse(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='surveys')


class QuestionResponse(BaseModel):
    survey_response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE, related_name='question_responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_set')
    selection = models.ManyToManyField(Selection, related_name='selections')


class Notification(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    recipients_users = models.ManyToManyField(User, related_name='notifications_received')
    recipients_groups = models.ManyToManyField(Group, related_name='notifications_received')