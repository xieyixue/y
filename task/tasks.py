# coding=utf-8
from celery import task
from time import sleep
import commands

@task()
def start_cmd(cmd):
    result = commands.getoutput(cmd.cmd)
    cmd.result = result
    cmd.status = 2
    cmd.save()
    return cmd
