# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0017_auto_20170727_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itempic',
            field=models.FileField(default=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='profpic',
            field=models.FileField(default='/media/def.png', upload_to=''),
        ),
    ]
