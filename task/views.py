# coding=utf-8
from rest_framework import viewsets
from models import Cmd
from serializers import CmdSerializers
from rest_framework.response import Response
from rest_framework import status

from tasks import start_cmd


class CmdViewSet(viewsets.ModelViewSet):
    queryset = Cmd.objects.all()
    serializer_class = CmdSerializers

    def create(self, request, *args, **kwargs):
        serializer = CmdSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            cmd = serializer.save(status=1)
            start_cmd.delay(cmd)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)