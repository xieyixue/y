# coding=utf-8
from django.db import models


class Cmd(models.Model):
    name = models.CharField(max_length=256)
    cmd = models.CharField(max_length=256)
    # 0:未开始 1:进行中 2:已完成
    status = models.IntegerField(default=0, blank=True)
    result = models.TextField(blank=True)

    class Meta:
        db_table = 'cmd'
