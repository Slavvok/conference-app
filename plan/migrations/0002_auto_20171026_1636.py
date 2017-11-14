# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presentation',
            options={},
        ),
        migrations.RenameField(
            model_name='presentation',
            old_name='essay',
            new_name='description',
        ),
        migrations.AddField(
            model_name='presentation',
            name='upload',
            field=models.FileField(null=True, upload_to='presentation'),
        ),
    ]