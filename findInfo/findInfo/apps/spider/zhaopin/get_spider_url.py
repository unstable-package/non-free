#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re, os, time
import zhaopin_spider
from bs4 import BeautifulSoup as bs
from __init__ import _headers, root_url, init_url


class UrlList(object):

    def __init__(self, _cur_url):
        self.headers = _headers
        self.cur_url = _cur_url

    def get_cur_page(self):
        for i in xrange(5):
            try:
                response = requests.get(self.cur_url, headers=self.headers)
            except requests.RequestException:
                time.sleep(3)
            else:
                return response.text.encode('utf-8')
        return None

    def get_url_list(self, page_text):
        soup = bs(page_text, 'html.parser', from_encoding='utf-8')
        link_list = soup.find_all('a', class_='fl __ga__fullResultcampuspostname_clicksfullresultcampuspostnames_001')
        link_set = set(link.get('href') for link in link_list)
        return link_set

    def get_next_page_url(self, page_text):
        soup = bs(page_text, 'html.parser', from_encoding='utf-8')
        next_page_span = soup.find('span', class_='font12 pageNext')
        next_page_li = next_page_span.find_parent('li')
        next_page_url = next_page_li.find('a').get('href')
        if next_page_url:
            self.cur_url = root_url + str(next_page_url)
            return True
        else:
            return False


def start(count):
    url_list = UrlList(init_url)
    print 'init_url =', init_url
    for i in range(count):
        page_text = url_list.get_cur_page()
        if page_text and url_list.get_next_page_url(page_text):
            print url_list.cur_url
            link_set = url_list.get_url_list(page_text)
            zhaopin_spider.main(link_set)
        else:
            print url_list.cur_url
            raise requests.RequestException
