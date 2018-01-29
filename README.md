# _windows X86-64bit下操作_ 

# Python 3环境搭建
1. 安装python3:https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe

1. git下载地址:https://github-production-release-asset-2e65be.s3.amazonaws.com/23216272/cd0c54e0-ff9e-11e7-944d-faa11800472e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180125%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180125T132806Z&X-Amz-Expires=300&X-Amz-Signature=9dbdb7d100acff58f1357ff72ebee623d851b68f11edcbaf7eabb0006812c00f&X-Amz-SignedHeaders=host&actor_id=34368790&response-content-disposition=attachment%3B%20filename%3DGit-2.16.1-64-bit.exe&response-content-type=application%2Foctet-stream
1. 打开cmd窗口，下载git项目到本地：git clone https://gitee.com/yzdx0000/My_favorite/
1. python IDE工具:https://download.jetbrains.8686c.com/python/pycharm-community-2017.3.3.exe
1. 使用pycharm打开本地项目My_favorite

# 关于使用jenkins执行cmd窗口python中文乱码的解决
![输入图片说明](https://gitee.com/uploads/images/2018/0129/123635_5eb9eaf1_1734289.png "jenkins.png")

# wordcloud-使用步骤

1. 打开cmd窗口,安装依赖库，pip install -r  wordcloud_requirements.txt

1. 若安装不上wordcloud，请到相关目录下先安装whl文件:pip install wordcloud-1.3.3-cp37-cp37m-win_amd64.whl
1. 一个DBA qq群聊天记录效果图![效果图](https://gitee.com/uploads/images/2018/0127/190004_fbed5eef_1734289.png "Figure_1.png")

# data_ana(数据分析与可视化)
1. country.txt为echarts支持的城市列表
1. 所有AQI指数来源均调用[易源数据](https://www.showapi.com/)提供的API
1. AQI.py文件制图使用的是[echarts](http://echarts.baidu.com/)的开源库
1. 注意:AQI.py包含本人的API账号，但请不要使用本人的API账号，去各API网站自行注册或者申请，谢谢配合
1. ![效果图](https://gitee.com/uploads/images/2018/0127/183410_70c0aac2_1734289.png "1.png")
1. ![数据](https://gitee.com/uploads/images/2018/0127/183447_cb72586d_1734289.png "2.png")
1. ![这里是列表文本](https://gitee.com/uploads/images/2018/0128/143116_1a42a60e_1734289.png "我的第一个图表.png")