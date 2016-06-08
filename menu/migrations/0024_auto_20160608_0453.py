# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0023_auto_20160608_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
    ]
