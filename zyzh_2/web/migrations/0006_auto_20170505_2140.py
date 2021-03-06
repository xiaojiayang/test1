# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-05 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170501_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('enable', models.IntegerField(choices=[(1, '\u662f'), (0, '\u5426')])),
            ],
            options={
                'verbose_name': '\u5bb6\u5177\u5206\u7c7b',
                'verbose_name_plural': '\u5bb6\u5177\u5206\u7c7b',
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='\u7b2c\u4e00\u4e2a\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='\u6700\u540e\u4e00\u4e2a\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u4e66\u540d'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='dpartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Dpartment', verbose_name='\u90e8\u95e8'),
        ),
    ]
