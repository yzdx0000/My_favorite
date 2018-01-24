# 词云
# author:wx

# 导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread

# 读取一个txt文件

text = open(r'C:\Users\wx\Desktop\text.txt', 'rb').read().decode('utf-8')

# 读入背景图片

bg_pic = imread(r'C:\Users\wx\Desktop\3.jpg')

# 生成词云

wordcloud = WordCloud(mask=bg_pic, background_color='white', scale=1.5).generate(text)

image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片

wordcloud.to_file('test.jpg')
