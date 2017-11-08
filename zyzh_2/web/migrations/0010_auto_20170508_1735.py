# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_blog1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='\u6807\u9898')),
                ('img_file', models.ImageField(upload_to='/static/imgs', verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u5bb6\u5177\u8be6\u60c5',
                'verbose_name_plural': '\u5bb6\u5177\u8be6\u60c5',
            },
        ),
        migrations.AlterModelOptions(
            name='blog1',
            options={'verbose_name': '\u535a\u5ba21', 'verbose_name_plural': '\u535a\u5ba21'},
        ),
    ]
