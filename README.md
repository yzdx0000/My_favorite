# _windows X86-64bit下操作_ 

# python环境搭建
1. 安装python3:https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe

1. git下载地址:https://github-production-release-asset-2e65be.s3.amazonaws.com/23216272/cd0c54e0-ff9e-11e7-944d-faa11800472e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180125%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180125T132806Z&X-Amz-Expires=300&X-Amz-Signature=9dbdb7d100acff58f1357ff72ebee623d851b68f11edcbaf7eabb0006812c00f&X-Amz-SignedHeaders=host&actor_id=34368790&response-content-disposition=attachment%3B%20filename%3DGit-2.16.1-64-bit.exe&response-content-type=application%2Foctet-stream
1. 打开cmd窗口，下载git项目到本地：git clone https://gitee.com/yzdx0000/My_favorite/
1. python IDE工具:https://download.jetbrains.8686c.com/python/pycharm-community-2017.3.3.exe
1. 使用pycharm打开本地项目My_favorite

# wordcloud-使用步骤

1. 打开cmd窗口,安装依赖库，pip install -r  wordcloud_requirements.txt

1. 若安装不上wordcloud，请到相关目录下先安装whl文件:pip install wordcloud-1.3.3-cp37-cp37m-win_amd64.whl

# data_ana(数据分析与可视化)
1. geo_test.py用于城市AQI指标的地图显示，调用的是spider下的AQI.py模块，AQI.py用于爬取pm2.5网站的数据
![AQI](https://gitee.com/uploads/images/2018/0127/013333_6d71da15_1734289.png "AQI.png")