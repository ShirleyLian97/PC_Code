# 打好python基础很重要！

# 练习时间：2022/8/18 16:13

# 数据导入
import numpy as np
import pandas as pd
df=pd.read_csv("data/评论采集.csv")
df.columns = ["comments"]
print(df.head(5))


# 数据描述
print(df.describe())

# 情感分析
from snownlp import SnowNLP
df['emotion']=df["comments"].apply(lambda x: SnowNLP(x).sentiments)
print(df.head())

# 情感描述
print(df.describe())

# 绘制情感直方图
import matplotlib.pyplot as plt
import numpy as py

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

bins = np.arange(0,1.1,0.1)   #输出初始值为0，步长为0.1，终点值为1.1（不包含）的排列
plt.hist(df["emotion"],bins,color = '#4F94CD', alpha=0.9)
plt.xlim(0,1)     #plt.xlim() 显示的是x轴的作图范围
plt.xlabel("情感分析")
plt.ylabel("数量")
plt.title("情感分析直方图")

from wordcloud import WordCloud
import jieba

myfont = r'C:\Windows\Fonts\simhei.ttf'
w = WordCloud(font_path=myfont)

text=''
for i in df["comments"]:
    text+=i

data_cut=" ".join(jieba.lcut(text))
stoplist = [i.strip() for i in open('data/stopwords_zh.txt',encoding='utf-8').readlines()]
texts = [word for word in data_cut.lower().split() if word not in stoplist]
corpus=" ".join(texts)   #将字符串列表转化为字符串

w.generate(corpus)
image = w.to_file('词云图1.png')
image

# 关键词抽取
from jieba import analyse
key_words=jieba.analyse.extract_tags(sentence=corpus, topK=10, withWeight=True, allowPOS=())  #sentences必须是字符串
print(key_words)

# 积极评论与消极评论占比
pos,neg=0,0
for i in df["emotion"]:
    if i>=0.5:
        pos+=1
    else:
        neg+=1

print('积极评论数目为:', pos, '\n消极评论数目为：', neg)

#  积极消极评论占比
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

pie_labels = 'positive', 'negative'
plt.pie([pos, neg], labels=pie_labels, autopct='%1.2f%%', shadow=True)

plt.show()
