# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workplace', '0003_auto_20170310_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('note_number', models.AutoField(primary_key=True, serialize=False)),
                ('note_name', models.CharField(max_length=200)),
                ('note_starttime', models.DateTimeField()),
                ('note_endtime', models.DateTimeField()),
            ],
        ),
    ]
