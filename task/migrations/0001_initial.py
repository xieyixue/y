# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('cmd', models.CharField(max_length=256)),
                ('status', models.IntegerField(default=0)),
                ('result', models.TextField()),
            ],
            options={
                'db_table': 'cmd',
            },
        ),
    ]
