from pyecharts import Geo
from spider import  AQI

#城市的AQI绘图


## Scatter 类型
#geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
#          width=1200, height=600, background_color='#404a59')
#attr, value = geo.cast(data)
#geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
#geo.show_config()
#geo.render()
#
##HeatMap 类型
#geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
#background_color='#404a59')
#attr, value = geo.cast(data)
#geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300], visual_text_color='#fff')
#geo.show_config()
#geo.render()

data=AQI.country()
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.show_config()
geo.render()