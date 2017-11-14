# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20171029_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='pres_part',
        ),
        migrations.AddField(
            model_name='participant',
            name='presentation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pres', to='plan.Presentation'),
        ),
    ]