# coding=utf-8
from django.db import models

# Create your models here.


class ToDo(models.Model):
    name = models.CharField(max_length=256)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'todo'
