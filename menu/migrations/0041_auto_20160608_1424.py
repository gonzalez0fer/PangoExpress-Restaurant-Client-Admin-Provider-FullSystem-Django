# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0040_auto_20160608_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato_en_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MENU'),
        ),
    ]
