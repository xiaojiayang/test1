# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170505_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u6b63\u6587', blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
        ),
        migrations.AlterField(
            model_name='furniture',
            name='img_file',
            field=models.ImageField(upload_to='/static/imgs', verbose_name='\u56fe\u7247'),
        ),
    ]
