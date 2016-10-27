# coding=utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from models import ToDo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ToDoSeriailzer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ToDo
        fields = ('url', 'name', 'done')