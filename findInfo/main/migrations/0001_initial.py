# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company_name', models.TextField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('company_property', models.TextField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe6\x80\xa7\xe8\xb4\xa8', blank=True)),
                ('company_scale', models.TextField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe8\xa7\x84\xe6\xa8\xa1', blank=True)),
                ('company_intro', models.TextField(help_text=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\x8b\xe7\xbb\x8d', blank=True)),
            ],
            options={
                'db_table': 'company_info',
                'verbose_name': '\u516c\u53f8\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job_name', models.TextField(help_text=b'\xe8\x81\x8c\xe4\xbd\x8d\xe5\x90\x8d\xe7\xa7\xb0')),
                ('job_type', models.TextField(help_text=b'\xe8\x81\x8c\xe4\xbd\x8d\xe7\xb1\xbb\xe5\x9e\x8b', blank=True)),
                ('job_salary', models.TextField(help_text=b'\xe6\x9c\x88\xe8\x96\xaa', blank=True)),
                ('job_edu_back', models.TextField(help_text=b'\xe5\xad\xa6\xe5\x8e\x86', blank=True)),
                ('job_place', models.TextField(help_text=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x9c\xb0\xe7\x82\xb9', blank=True)),
                ('job_need', models.TextField(help_text=b'\xe6\x8b\x9b\xe8\x81\x98\xe4\xba\xba\xe6\x95\xb0', blank=True)),
                ('job_intro', models.TextField(help_text=b'\xe8\x81\x8c\xe4\xbd\x8d\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('announce_date', models.DateField(help_text=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('company_id', models.ForeignKey(to='main.CompanyInfo')),
            ],
            options={
                'db_table': 'job_info',
                'verbose_name': '\u804c\u4f4d\u4fe1\u606f',
            },
        ),
    ]
