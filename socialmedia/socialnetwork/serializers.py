from rest_framework import serializers
from .models import *


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'avatar', 'cover_image', 'role']
#
#
# class AlumniProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = AlumniProfile
#         fields = ['user', 'student_id', 'confirmed']
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class AlumniProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AlumniProfile
        fields = ['user', 'student_id', 'confirmed']

