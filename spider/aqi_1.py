import  urllib
from  urllib import  request
import  json
#import  curl
import pandas as pd               # 导入pandas模块 并简写成 pd
import matplotlib.pyplot as plt   # 导入绘图包(今天的主角)
import numpy as np                # 导入numpy模块 并简写成 np
import xlrd
from pyecharts import Geo
#from spider import  AQI

"""获取excel表格中城市一列"""
data = pd.read_excel('weather_contrast_20171207.xls')
data.head()
# 删除包含缺失值的行
df = data.dropna()
data1=[]
for city in df.simcode:
       # global city
    print(city)
#
    #token='5j1znBVAsnSf5xQyNQyq'
    site='http://api.k780.com/?app=weather.pm25&weaid=%s&appkey=31408&sign=a744485d78e931058e95b9a0efb93e9d&format=json'%city
    #url="http://api.k780.com/?app=weather.pm25&weaid=城市编号&appkey=APPKEY&sign=SIGN&format=json"
    #curl.Curl.url
    #print(site)
    f=urllib.request.urlopen(site)
    nowapi_call = f.read()
    a_result = json.loads(nowapi_call)
    #print(a_result)
    datalist=a_result['result']
    #print(datalist)
    data1.append(datalist['citynm'])

    print(data1)
   #if a_result:
   #  if a_result['success'] != '0':
   #    print (a_result['result'])
   #  else:
   #    print (a_result['msgid']+' '+a_result['msg'])
   #else:
   #  print ('Request nowapi fail.')

geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
#geo.show_config()
geo.render()