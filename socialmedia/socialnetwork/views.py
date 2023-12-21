from django.shortcuts import render
from .models import AlumniProfile
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from socialnetwork.serializers import AlumniProfileSerializer


class AlumniViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfile.objects.filter(confirmed=True)
    serializer_class = AlumniProfileSerializer


# Create your views here.

#
# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#
#         # Custom logic to create AlumniProfile associated with the new user
#         alumni_data = {'user': user.id, 'student_id': request.data.get('student_id', ''), 'confirmed': False}
#         alumni_serializer = AlumniProfileSerializer(data=alumni_data)
#         alumni_serializer.is_valid(raise_exception=True)
#         alumni_serializer.save()
#
#         return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)