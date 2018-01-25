# 词云
# author:wx

# 导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import sys
import os

# 读取一个txt文件
tools = os.path.dirname(os.getcwd()) + r"\Word_Cloud\tools"  # 获取附件绝对路径
jpg = r"%s\xinxing.jpg" % tools  # 背景图片
txt = r'C:\Users\wx\Desktop\test.txt'

if os.path.exists(txt):
    text = open(txt, 'rb').read().decode('utf-8')

else:
    print("txt文件不存在")
    sys.exit()  # 不存在txt则退出程序，不再执行以后的代码,此处用quit()也可以

# 读入背景图片

bg_pic = imread(jpg)

# 生成词云

wordcloud = WordCloud(mask=bg_pic, font_path=r"C:\Windows\Fonts\simhei.ttf", background_color='white',
                      scale=1.5).generate(text)

image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片

wordcloud.to_file('test.jpg')
