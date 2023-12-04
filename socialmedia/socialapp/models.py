from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatars', null=True)
    cover = models.ImageField(upload_to='users/covers', null=True)
    is_Lecturer = models.BooleanField(default=False)

    def change_password_lecturer(self):
        if self.is_Lecturer.__eq__(True):
            self.set_password("ou@123")


class Alumni(User):
    student_id = models.CharField(max_length=11, unique=True)


class Lecturer(User):
    password = "ou@123"
