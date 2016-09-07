#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CompanyInfo(BaseModel):
    company_name = models.TextField(blank=False, help_text='公司名称')
    company_property = models.TextField(blank=True, help_text='公司性质')
    company_scale = models.TextField(blank=True, help_text='公司规模')
    company_intro = models.TextField(blank=True, help_text='公司介绍')

    class Meta:
        db_table = 'company_info'
        verbose_name = _(u"公司信息")


class JobInfo(BaseModel):
    company_id = models.ForeignKey('CompanyInfo')
    job_name = models.TextField(blank=False, help_text='职位名称')
    job_type = models.TextField(blank=True, help_text='职位类型')
    job_salary = models.TextField(blank=True, help_text='月薪')
    job_edu_back = models.TextField(blank=True, help_text='学历')
    job_place = models.TextField(blank=True, help_text='工作地点')
    job_need = models.TextField(blank=True, help_text='招聘人数')
    job_intro = models.TextField(blank=True, help_text='职位描述')
    announce_date = models.DateField(blank=True, help_text='发布时间')

    class Meta:
        db_table = 'job_info'
        verbose_name = _(u"职位信息")
