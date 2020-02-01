# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-01 15:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20200126_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Заявка')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 1, 20, 7, 23, 982761), verbose_name='Дата')),
                ('status', models.PositiveIntegerField(verbose_name='Статус')),
                ('changeddate', models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 1, 20, 7, 23, 982761), verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'заявка',
                'verbose_name_plural': 'заявки',
                'db_table': 'Orders',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 1, 20, 7, 23, 981761), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 1, 20, 7, 23, 981761), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 1, 20, 7, 23, 982761), verbose_name='Опубликована'),
        ),
    ]