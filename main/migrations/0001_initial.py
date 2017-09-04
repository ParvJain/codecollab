# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 15:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('snippet', models.TextField()),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'permissions': (('can_reivew_code', 'Can add comments to the code'),),
            },
        ),
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Code')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Coder')),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='coder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Coder'),
        ),
    ]
