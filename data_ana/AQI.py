from urllib import request, parse
import json
from pyecharts import Geo
import pandas as pd  # 导入pandas模块 并简写成 pd
import matplotlib.pyplot as plt  # 导入绘图包(今天的主角)
import numpy as np  # 导入numpy模块 并简写成 np
import xlrd
import os

# """获取excel表格中城市一列"""
# data = pd.read_excel('weather_contrast_20171207.xls')
# data.head()
## 删除包含缺失值的行
# df=data
##df = data.dropna()#
##df.info()
# for city in df.area_2:
#       # global city
#    #print(city)

data = []  # 定义城市及对应的AQI为list
# 获取txt文件
file = open('country.txt', 'r', encoding='utf-8')  # 打开城市列表文件
filelist = file.readlines()  # 读取每一行
for city in filelist:
    print(city)
    print('send data....')
    showapi_appid = "55331"  # 替换成你自己的，不要用笔者的哦
    showapi_sign = "264c3e6849ef4b25aacfd5279e47e34c"  # 替换成你自己的，不要用笔者的哦
    url = "http://route.showapi.com/104-29"
    send_data = parse.urlencode([
        ('showapi_appid', showapi_appid)
        , ('showapi_sign', showapi_sign)
        , ('city', city)

    ])

    req = request.Request(url)
    try:
        response = request.urlopen(req, data=send_data.encode('utf-8'), timeout=10)  # 10秒超时反馈
    except Exception as e:
        print(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)  # 解码json文件
    # print(result_json)
    try:

        ret_code = result_json['showapi_res_body']['ret_code']  # 取返回值
        print(ret_code)

    except Exception as a:
        print(a)
    if ret_code == 0:
        try:

            # print(result_json)
            city = result_json['showapi_res_body']['pm']['area']
            aqi = result_json['showapi_res_body']['pm']['aqi']
            zhi = (city, aqi)
            data.append(zhi)
            print(data)


        except Exception as  e:
            print(e)

geo = Geo("全国主要城市实时空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
          width=1200, height=600, background_color='#404a59')
print(data)
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
# geo.show_config()
geo.render()
