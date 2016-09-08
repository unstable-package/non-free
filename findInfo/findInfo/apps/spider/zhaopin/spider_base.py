#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import requests
from __init__ import _headers
from info.models import JobInfo, CompanyInfo


class SpiderBase(object):

    def save(self):
        company_info, created = CompanyInfo.objects.get_or_create(
            company_name=self._company_name)
        company_info.company_name = self._company_name
        company_info.company_name = self._company_name
        company_info.company_property = self._company_property
        company_info.company_scale = self._company_scale
        company_info.company_intro = self._company_intro if self._company_intro is not None else ''
        company_info.save()

        job_info, created = JobInfo.objects.get_or_create(
            company_id=company_info, job_name=self._job_name)
        job_info.company_id = company_info
        job_info.job_name = self._job_name
        job_info.job_type = self._job_type
        job_info.job_salary = self._job_salary
        job_info.job_edu_back = self._job_edu_back
        job_info.job_place = self._job_place
        job_info.job_need = self._job_need
        job_info.job_intro = self._job_intro
        job_info.announce_date = self._announce_date
        job_info.save()
        


    def __init__(self):
        self.headers = _headers

    def _get_company_name(self, content):
        pass

    def _get_company_property(self, content):
        pass

    def _get_company_scale(self, content):
        pass

    def _get_company_intro(self, content):
        pass

    def _get_job_name(self, content):
        pass

    def _get_job_type(self, content):
        pass

    def _get_job_salary(self, content):
        pass

    def _get_job_edu_back(self, content):
        pass

    def _get_job_place(self, content):
        pass

    def _get_job_need(self, content):
        pass

    def _get_job_intro(self, content):
        pass

    def _get_announce_date(self, content):
        pass


    def _parse_content(self, pattern, content):
        m = re.search(pattern, content)
        if m is None:
            return ""
        else:
            return m.group(1)


    def show(self):
        print 'company_name:'
        try:
            print self._company_name
        except AttributeError:
            pass

        print 'company_property:'
        try:
            print self._company_property
        except AttributeError:
            pass

        print 'company_scale:'
        try:
            print self._company_scale
        except AttributeError:
            pass

        print 'company_intro:'
        try:
            print self._company_intro
        except AttributeError:
            pass

        print 'job_name:'
        try:
            print self._job_name
        except AttributeError:
            pass

        print 'job_type:'
        try:
            print self._job_type
        except AttributeError:
            pass

        print 'job_salary:'
        try:
            print self._job_salary
        except AttributeError:
            pass

        print 'job_edu_back:'
        try:
            print self._job_edu_back 
        except AttributeError:
            pass

        print 'job_place:'
        try:
            print self._job_place 
        except AttributeError:
            pass

        print 'job_need:'
        try:
            print self._job_need 
        except AttributeError:
            pass

        print 'job_intro:'
        try:
            print self._job_intro 
        except AttributeError:
            pass

        print 'announce_date:'
        try:
            print self._announce_date 
        except AttributeError:
            pass

    def fetch(self):
        for i in xrange(5):
            try:
                response = requests.get(self._url, headers=self.headers)
            except requests.RequestException:
                time.sleep(3)
            else:
                break
        
        self._content = response.text.encode('utf-8')


        self._company_name = self._get_company_name(self._content)
        self._company_property = self._get_company_property(self._content)
        self._company_scale = self._get_company_scale(self._content)
        self._company_intro = self._get_company_intro(self._content)
        
        self._job_name = self._get_job_name(self._content)
        self._job_type = self._get_job_type(self._content)
        self._job_salary = self._get_job_salary(self._content)
        self._job_edu_back = self._get_job_edu_back(self._content)
        self._job_place = self._get_job_place(self._content)
        self._job_need = self._get_job_need(self._content)
        self._job_intro = self._get_job_intro(self._content)
        self._announce_date = self._get_announce_date(self._content)

