#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RecruitInfo(BaseModel):
    pass
