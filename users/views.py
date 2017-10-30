from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserDetail(generics.ListCreateAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
    	return User.objects.all().filter(username=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

