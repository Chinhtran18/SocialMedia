from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    media = models.ForeignKey('Media', on_delete=models.CASCADE)


class Media(models.Model):
    avatar = models.ImageField(upload_to='users/%Y/%m')
    cover = models.ImageField(upload_to='users/%Y/%m')


class StudentProfile(models.Model):
    student_id = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class LecturerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.Pa

