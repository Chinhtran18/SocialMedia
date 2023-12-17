from django.contrib.auth.hashers import make_password
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


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatars/%Y/%m', null=True)
    cover_images = models.ImageField(upload_to='users/cover_images/%Y/%m', null=True)

    def __str__(self):
        return self.username


class AlumniProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)
    is_student = models.BooleanField(default=False)


class LecturerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.password = make_password('ou@123')
        super().save(*args, **kwargs)


class Post(BaseModel):
    content = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')


class Comment(BaseModel):
    content = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


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
    title = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='surveys')


class Question(models.Model):
    content = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')


class Notification(BaseModel):
    content = models.TextField()
    sender = models.ManyToManyField(CustomUser, related_name='notifications')


# Group.objects.get_or_create(name='AlumniProfile')
# Group.objects.get_or_create(name='LecturerProfile')
# Group.objects.get_or_create(name='Administrator')
