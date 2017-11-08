# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-27 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170423_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dpartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u90e8\u95e8\u540d\u5b57')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u4eba\u5458\u540d\u79f0')),
                ('number1', models.IntegerField(verbose_name='\u7f16\u53f7')),
                ('gz', models.IntegerField(verbose_name='\u5de5\u8d44')),
                ('dpartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Dpartment')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u8001\u516c', 'verbose_name_plural': '\u8001\u516c'},
        ),
    ]