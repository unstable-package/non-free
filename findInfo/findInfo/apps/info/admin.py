#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from models import CompanyInfo, JobInfo


class JobInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_id', 'job_name', 'job_type', 'job_salary', 'job_edu_back', 'job_place', 'job_need', 'announce_date', 'job_intro')
    search_fields = ('id', 'company_id', 'job_name', 'job_type', 'job_salary', 'job_edu_back', 'job_place', 'job_need', 'announce_date', 'job_intro')
    list_filter = ('id', 'company_id', 'job_name', 'job_type', 'job_salary', 'job_edu_back', 'job_place', 'job_need', 'announce_date')
    ordering = ('id',)
    actions_on_top = True;
    actions_on_bottom = True;


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'company_property', 'company_scale', 'company_intro')
    search_fields = ('id', 'company_name', 'company_property', 'company_scale', 'company_intro')
    list_filter = ('id', 'company_name', 'company_property', 'company_scale')
    ordering = ('id',)
    actions_on_top = True;
    actions_on_bottom = True;


admin.site.register(JobInfo, JobInfoAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
