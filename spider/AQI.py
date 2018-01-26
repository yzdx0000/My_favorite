#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by ustcwq
import urllib
from urllib import request
import threading
from time import ctime
from bs4 import BeautifulSoup
import random
import re


#该模块主要为了获取城市和对应的AQI


def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    html = urllib.request.urlopen(site)
    soup = BeautifulSoup(html)
    city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.sele  # ct(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述
    return (city.text, aqi.text)


def one_thread():  # 单线程
    print('One_thread Start: ' + ctime() + '\n')
    getPM25('beijing')


def two_thread():  # 多线程
    print('Two_thread Start: ' + ctime() + '\n')
    threads = []
    list = ["chongqing", "beijing", "tianjin", "bengbu", "hefei", "wuhu", "maanshan", "shenzhen", "xian", "changsha"
                                                                                                          "hunan",
            "hangzhou", "wulumuqi", "wuhan"]
    t1 = threading.Thread(target=getPM25, args=(list[0],))
    threads.append(t1)
    t2 = threading.Thread(target=getPM25, args=(list[1],))
    threads.append(t2)
    for t in threads:
        # t.setDaemon(True)
        t.start()


data = []
for i in ["chongqing", "beijing", "tianjin", "bengbu", "hefei", "wuhu", "maanshan", "shenzhen", "xian", "changsha"
                                                                                                        "hunan",
          "hangzhou", "wulumuqi", "wuhan"]:
    getPM25(i)
    data.append(getPM25(i))


def country():
    global data
    data = data
    print(data)
    return data


if __name__ == '__main__':
    # one_thread()
    # print('\n' * 2)
    # two_thread()
    country()
