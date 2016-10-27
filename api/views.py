from rest_framework import viewsets
from django.contrib.auth.models import User
from serializers import (
    UserSerializer,
    ToDoSeriailzer
)

from models import ToDo


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSeriailzer
