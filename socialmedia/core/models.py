from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Media(models.Model):
    avatar = models.ImageField(upload_to='users/avatars/%Y/%m')
    cover_images = models.ImageField(upload_to='users/cover_images/%Y/%m')


class CustomUser(AbstractUser):
    media = models.ForeignKey(Media, on_delete=models.CASCADE, null=True)


class AlumniProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)
    confirmed = models.BooleanField(default=False)


class LecturerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Post(BaseModel):
    content = RichTextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')


class Comment(BaseModel):
    content = RichTextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')


class Reaction(BaseModel):
    REACTION_TYPES = [
        ('like', 'Like'),
        ('love', 'Love'),
        ('wow', 'Wow'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ]
    type = models.CharField(max_length=10, choices=REACTION_TYPES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')


class Survey(BaseModel):
    title = RichTextField()
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)


class Choice(models.Model):
    content = models.TextField()


class Event(BaseModel):
    content = RichTextField()


# Group.objects.get_or_create(name='AlumniProfile')
# Group.objects.get_or_create(name='LecturerProfile')
# Group.objects.get_or_create(name='Administrator')
