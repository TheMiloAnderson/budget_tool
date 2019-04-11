from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, User
from rest_framework.authentication import TokenAuthentication


class UserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = ''

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ''
    authentication_classes = (TokenAuthentication, )
