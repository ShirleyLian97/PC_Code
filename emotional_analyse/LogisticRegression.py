# 打好python基础很重要！

# 练习时间：2022/9/15 23:02
import numpy as np
import pandas as pd
# 读取数据
data= pd.read_excel('data/伊利-京东评论按分类-好中差评.xlsx')
# print(data.head())
content=data['评价内容'].tolist()
score=data['评论类型'].tolist()
corpus=[]
for i in range(len(data)):
    if score[i]=='好评' and len(corpus)<350:
        corpus.append(content[i])
    if score[i]=='差评' and len(corpus)<650:
        corpus.append(content[i])
# #特征选取
# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer=CountVectorizer()
# x=vectorizer.fit_transform(corpus).toarray()
import jieba
import gensim
from gensim.models import word2vec
# 载入停用词
stoplist = [i.strip() for i in open('data/stopwords_zh.txt',encoding='utf-8').readlines()]
sentence=[[word.strip() for word in jieba.lcut(line) if word not in stoplist] for line in content]

# 构建一个简易词典
dic_corpus = []
for li in sentence[:1000]:
    dic_corpus += li
emotion_dic = {li:dic_corpus.count(li) for li in dic_corpus}
emotion_dic = list(emotion_dic.items())
emotion_dic.sort(key=lambda x:-x[1])

bad_corpus = []
for li in sentence[-300:]:
    bad_corpus += li
bad_dic = {li:bad_corpus.count(li) for li in bad_corpus}
bad_dic = list(bad_dic.items())
bad_dic.sort(key=lambda x:-x[1])

good_emotion = []
for li in emotion_dic[:50]:
    if li[0] not in bad_dic and li[0]!=' ' and len(li[0])>1:
        good_emotion.append(li[0])
# print(good_emotion)

model=word2vec.Word2Vec(sentence, vector_size=20,min_count=10,seed=30)
w2v_text=[]

import jieba
for item in corpus:
    tp=[]
    for word in jieba.lcut(item):
        if word in model.wv:
            tp.append(model.wv[word])
    if tp==[]:
        w2v_text.append([0]*20)
    else:
        w2v_text.append(sum(tp)/len(tp)) ##注意如果word2vec存在oov的词，则跳过
x = w2v_text
# print(type(x))

y=[]
for i in range(300):
    y.append(1)
for i in range(300):
    y.append(0)
test_y=[1 for i in range(50)]

have_good_words = []
for li in corpus:
    signal = 0
    for word in good_emotion:
        if word in li:
            signal = 1
            have_good_words.append(1)
            break
    if signal==0:
        have_good_words.append(0)


# print(y)
# 建模
# 模型1-逻辑回归
# from sklearn.linear_model import LogisticRegression
# lr_clf=LogisticRegression()
# lr_clf=lr_clf.fit(x[50:],y)

# 模型2-MLP
import tensorflow as tf
from  sklearn.model_selection import train_test_split
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
x=np.array(x,dtype=np.float32)
y=np.array(y,dtype=np.float32)
test_y=np.array(test_y,dtype=np.float32)

# 创建序贯模型，这是神经网络中最简单的keras模型，仅有顺序单层堆叠而成
model=keras.models.Sequential()
# model.add(keras.layers.Flatten(input_shape = x.shape[1:]))
model.add(keras.layers.Dense(8, activation='relu', input_shape = x.shape[1:]))
model.add(keras.layers.Dropout(0.2))
# model.add(keras.layers.Dense(4, activation='relu'))
#输出层
model.add(keras.layers.Dense(2, activation='sigmoid'))
model.compile(loss=keras.losses.sparse_categorical_crossentropy, optimizer = 'sgd', metrics = 'accuracy')
history = model.fit(x[50:], y, epochs=5, validation_split=0.1)
result = model.evaluate(x[:50], test_y)
print(result)

# 模型3-随机森林
# x=pd.DataFrame(x)
# x['have_good_words'] = have_good_words
# y=np.array(y)
# test_y=np.array(test_y)

# 随机森林

# from sklearn.ensemble import RandomForestClassifier
# rfc = RandomForestClassifier(class_weight='balanced',random_state=37)
# rfc = rfc.fit(x[50:], y)
# score_r = rfc.score(x[:50], test_y)
# from sklearn.metrics import f1_score,precision_score,recall_score
# pred_r=rfc.predict(x[:50])
# precision_r=precision_score(pred_r,test_y)
# f1_r=f1_score(pred_r,test_y)
# recall_r=recall_score(pred_r,test_y)
# print(score_r,precision_r,f1_r,recall_r,sep='\n')
# #预测

# pred=lr_clf.predict(x[:50])
# # 评估
# print('train_score:',lr_clf.score(x[50:],y))
# print('test_score:',lr_clf.score(x[:50],test_y))
# # sklearn.metrics.f1_score(y_true, y_pred, *, labels=None, pos_label=1,average='binary', sample_weight=None,zero_division="warn"):
# from sklearn.metrics import f1_score,precision_score,recall_score
# f1 = f1_score(pred, test_y)
# print(f1)
# precision = precision_score(pred, test_y)
# recall=recall_score(pred,test_y)
# print(precision,recall,sep='\n')
# print((2*precision*recall)/(precision+recall))
