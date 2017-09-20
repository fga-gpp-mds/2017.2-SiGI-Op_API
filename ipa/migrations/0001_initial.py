# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('site_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('bandwidth', models.IntegerField()),
                ('IPa_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('type_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='type_site',
            field=models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                to='ipa.SiteType'),
        ),
    ]