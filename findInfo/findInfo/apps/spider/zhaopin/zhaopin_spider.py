#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, time
from __init__ import _headers
from spider_base import SpiderBase

class ZhaopinSpider(SpiderBase):

    def __init__(self):
        self._url = ""
        self.headers = _headers
        super(SpiderBase, self).__init__()

    def _get_company_name(self, content):
        pattern = '<li\sid="jobCompany"\sclass="cJobDetailInforWd1\smarb">\s*<a\starget="_blank"\shref=".*?">(.*?)</a>\s*</li>'
        return self._parse_content(pattern, content)

    def _get_company_property(self, content):
        pattern = '公司行业：</li>\s*<li\sclass="cJobDetailInforWd2"\stitle="(.*?)">.*?</li>'
        return self._parse_content(pattern, content)

    def _get_company_scale(self, content):
        pattern = '公司规模：</li>\s*<li\sclass="cJobDetailInforWd2">(.*?)</li>'
        return self._parse_content(pattern, content)

    def _get_company_intro(self, content):
        pass

    def _get_job_name(self, content):
        pattern = '<h1\sid="JobName"\sclass="cJobDetailInforTitle">\s*(.*?)\s*<span\sclass="cIcon\scIcon_zl\sml10">\s*</span>\s*</h1>'
        return self._parse_content(pattern, content)

    def _get_job_type(self, content):
        pattern = '职位类别：</li>\s*<li\sclass="cJobDetailInforWd2\smarb">(.*?)</li>'
        return self._parse_content(pattern, content)

    def _get_job_salary(self, content):
        pattern = '薪：</li>\s*<li\sclass="cJobDetailInforWd2\smarb">\s*(.*?)\s*</li>'
        return self._parse_content(pattern, content)

    def _get_job_edu_back(self, content):
        pattern = '历：</li>\s*<li\sclass="cJobDetailInforWd2\smarb">\s*(.*?)\s*</li>'
        return self._parse_content(pattern, content)

    def _get_job_place(self, content):
        pattern = '工作地点：</li>\s*<li\sid="currentJobCity"\sclass="cJobDetailInforWd2\smarb"\sjct=".*?"\stitle=(.*?)>'
        return self._parse_content(pattern, content)

    def _get_job_need(self, content):
        pattern = '招聘人数：</li>\s*<li\sclass="cJobDetailInforWd2\smarb">(.*?)</li>'
        return self._parse_content(pattern, content)

    def _get_job_intro(self, content):
        pattern = '<p\sclass="mt20">(.*?)</p>\s*<div\sclass="clearfix\scJob_Delivery\smt24">'
        return self._parse_content(pattern, content)

    def _get_announce_date(self, content):
        pattern = '发布时间：</li>\s*<li\sclass="cJobDetailInforWd2\smarb">(.*?)</li>'
        return self._parse_content(pattern, content)

def main(url_list):
    zhaopin = ZhaopinSpider()
    for val in url_list:
        time.sleep(3)
        print 'link =', val
        zhaopin._url = val
        zhaopin.fetch()
        zhaopin.show()
        zhaopin.save()