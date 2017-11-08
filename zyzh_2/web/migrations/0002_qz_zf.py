# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-23 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u4e08\u592b\u540d\u5b57')),
                ('age', models.IntegerField(max_length=200, verbose_name='\u5e74\u9f84')),
            ],
        ),
        migrations.CreateModel(
            name='Qz',
            fields=[
                ('zf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.Zf')),
                ('name', models.CharField(max_length=100, verbose_name='\u59bb\u5b50\u540d\u5b57')),
                ('age', models.IntegerField(max_length=200, verbose_name='\u5e74\u9f84')),
            ],
        ),
    ]