#coding=utf8
import lxml
from lxml import etree
import requests
import sys
from importlib import reload
import os
import re
from lxml import etree
from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import pymongo
import base64
import urllib
import time, requests
import datetime, random
from etl.utils.log_conf import configure_logging
import traceback
from etl.data_gather.settings import SAVE_MONGO_CONFIG, RESOURCE_DIR
from etl.common_spider.donwloader02 import Downloader
from selenium import webdriver
from urllib.parse import urljoin
from urllib import parse
from urllib.parse import urlunparse
from posixpath import normpath
import chardet
import threading

client = pymongo.MongoClient('xxx', 0)
db1 = client.lz_data_gather_ai
col1 = db1.company_baisc_data_maintenance_table
headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
            # 'Referer': '',
            # 'Host': self.host,
        }
configure_logging("QYGW_news_host_url.log")  # 日志文件名
logger = logging.getLogger("spider")
downloader = Downloader(logger, need_proxy=False)

def spider01(text):
    with open(text, 'r', encoding='utf-8') as f:
        for num, i in enumerate(f.readlines()):
            # print(num+1)
            if num < 3000:
                continue

            i = i.replace('\n','')
            name = i.split(',')[0]
            url = i.split(',')[1]
            record = {}
            if ('taobao' in url) or ('tmall' in url):
                continue



            r_in_db = col1.find_one({"website": url})  # 唯一标识字段来去重
            if not r_in_db:
                resp = downloader.crawl_data(url, None, headers, "get")
                time.sleep(2)
                if resp:
                    record['company_name'] = name
                    record['website'] = url
                    record['success'] = 1
                    record['news_list_page_url'] = []
                    col1.insert_one(record)
                    print(threading.currentThread().getName() + str(' is Starting,')+'num:'+str(num+1), ',',resp, url,',succeed',)
                else:
                    record['company_name'] = name
                    record['website'] = url
                    record['success'] = 0
                    record['news_list_page_url'] = []
                    col1.insert_one(record)
                    print(threading.currentThread().getName() + str(' is Starting,')+'num:'+str(num+1),',',resp, url,',failed',)
            else:
                print('pass')


if __name__ == '__main__':
    t1 = threading.Thread(name='threading01', target=spider01, args=('lz_data_combine_company_name001.txt',))
    t2 = threading.Thread(name='threading02', target=spider01, args=('lz_data_combine_company_name002.txt',))
    t3 = threading.Thread(name='threading03', target=spider01, args=('lz_data_combine_company_name003.txt',))
    t4 = threading.Thread(name='threading04', target=spider01, args=('lz_data_combine_company_name004.txt',))
    t5 = threading.Thread(name='threading05', target=spider01, args=('lz_data_combine_company_name005.txt',))
    t6 = threading.Thread(name='threading06', target=spider01, args=('lz_data_combine_company_name006.txt',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
