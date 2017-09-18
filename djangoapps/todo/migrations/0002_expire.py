# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateTimeField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Todo')),
            ],
        ),
    ]
