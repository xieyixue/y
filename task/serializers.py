# coding=utf-8

from rest_framework import serializers
from models import Cmd


class CmdSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cmd
        fields = ('name', 'cmd', 'status', 'result')