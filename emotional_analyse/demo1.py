# 打好python基础很重要！

# 练习时间：2022/8/17 16:50
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from itertools import accumulate
# 设置matplotlib绘图时的字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

# 统计句子长度及长度出现的频数
df=pd.read_csv("data/data_single.csv")
# print(df.head())   #查看数据
group=df.groupby('label')  #分组
# # df.groupby()  函数返回的对象是一系列键值对，其中键是分组的字段值，值是该字段值下的数据表。分组的结果是无法直接输出的，print()只能看到该结果的数据类型。可以用循环对分组后的结果进行遍历。
print(group["label"].count())  # print(group.size())

df["length"]=df["evaluation"].apply(lambda x:len(x)) #计算每一行长度且新增了一列长度在df中
# # print(df.head())
len_df=df.groupby("length").count()  #计数

sent_length=len_df.index.tolist()  #将索引转化为列表

sent_freq=len_df["evaluation"].tolist()  #转化为列表


# # 绘制句子长度及出现频数统计图
# plt.bar(sent_length,sent_freq)
# plt.title('句子长度及出现频数统计图',fontproperties=my_font)
# plt.xlabel('句子长度',fontproperties=my_font)
# plt.ylabel('句子长度出现的频数',fontproperties=my_font)
# plt.show()
# plt.close()
# # 绘制句子长度累积分布函数(CDF)
sent_pentage_list=[(count/sum(sent_freq)) for count in accumulate(sent_freq)]
print(sent_pentage_list)
# 绘制CDF
plt.plot(sent_length,sent_pentage_list)
# 寻找分位点为quantile的句子长度
quantile=0.91
print(list(sent_pentage_list))
for length,per in zip(sent_length,sent_pentage_list):  #zip将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    if round(per,2)==quantile:  #round函数用来对数值进行四舍五入，2表示保留2为小数
        index=length
        break
print('\n分位点为%s的句子长度：%d.'%(quantile,index))

# plt.show()
# plt.close()

# 绘制句子长度累积分布函数图
plt.plot(sent_length,sent_pentage_list)
plt.hlines(quantile,0,index,colors='c',linestyles='dashed')
plt.vlines(index,0,quantile,colors='c',linestyles='dashed')
plt.text(0,quantile,str(quantile))
plt.text(index,0,str(index))
plt.title('句子长度累计分布函数图',fontproperties=my_font)
plt.xlabel('句子长度',fontproperties=my_font)
plt.ylabel('句子长度累积频率',fontproperties=my_font)
plt.show()
plt.close()

# LSTM模型
import pickle
import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM,Dense,Embedding,Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load dataset
# ['evaluation'] is feature, ['label'] is label
def load_data(filepath,input_shape=20):
    df=pd.read_csv(filepath)

    # 标签及词汇表
    labels,vocabulary=list(df['label'].unique()),list(df['evaluation'].unique())

    # 构造字符级别的特征
    string=''
    for word in vocabulary:
        string+=word

    vocabulary=set(string)

    # 字典列表
    word_dictionary={word:i+1 for i,word in enumerate(vocabulary)}
    with open('word_dict.pk','wb') as f:
        pickle.dump(word_dictionary,f)
    inverse_word_dictionary={i+1:word for i,word in enumerate(vocabulary)}
    label_dictionary={label:i for i,label in enumerate(labels)}
    with open('label_dict.pk','wb') as f:
        pickle.dump(label_dictionary,f)
    output_dictionary={i:labels for i,labels in enumerate(labels)}

    # 词汇表大小
    vocab_size=len(word_dictionary.keys())
    # 标签类别数量
    label_size=len(label_dictionary.keys())

    # 序列填充，按input_shape填充，长度不足的按0补充
    x=[[word_dictionary[word] for word in sent] for sent in df['evaluation']]
    x=pad_sequences(maxlen=input_shape,sequences=x,padding='post',value=0)
    y=[[label_dictionary[sent]] for sent in df['label']]
    '''
    np_utils.to_categorical用于将标签转化为形如(nb_samples, nb_classes)
    的二值序列。
    假设num_classes = 10。
    如将[1, 2, 3,……4]转化成：
    [[0, 1, 0, 0, 0, 0, 0, 0]
     [0, 0, 1, 0, 0, 0, 0, 0]
     [0, 0, 0, 1, 0, 0, 0, 0]
    ……
    [0, 0, 0, 0, 1, 0, 0, 0]]
    '''
    y=[np_utils.to_categorical(label,num_classes=label_size) for label in y]
    y=np.array([list(_[0]) for _ in y])

    return x,y,output_dictionary,vocab_size,label_size,inverse_word_dictionary

# 创建深度学习模型，Embedding + LSTM + Softmax
def create_LSTM(n_units,input_shape,output_dim,filepath):
    x,y,output_dictionary,vocab_size,label_size,inverse_word_dictionary=load_data(filepath)
    model=Sequential()
    model.add(Embedding(input_dim=vocab_size+1,output_dim=output_dim,
                        input_length=input_shape,mask_zero=True))
    model.add(LSTM(n_units,input_shape=(x.shape[0],x.shape[1])))
    model.add(Dropout(0.2))
    model.add(Dense(label_size,activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    '''
        error:ImportError: ('You must install pydot (`pip install pydot`) and install graphviz (see instructions at https://graphviz.gitlab.io/download/) ', 'for plot_model/model_to_dot to work.')
        版本问题：from keras.utils.vis_utils import plot_model
        真正解决方案：https://www.pianshen.com/article/6746984081/
    '''

    plot_model(model,to_file='./model_lstm.png',show_shapes=True)
    # 输出模型信息
    model.summary()

    return model

# 模型训练
def model_train(input_shape,filepath,model_save_path):
    # 将数据集分为训练集和测试集，占比为9：1
    # input_shape=100
    x,y,output_dictionary,vocab_size,label_size,inverse_word_dictionary=load_data(filepath,input_shape)
    train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.1,random_state=42)

    # 模型输入参数，需要根据自己需要调整
    n_units=100
    batch_size=32
    epochs=5
    output_dim=20

    # 模型训练
    lstm_model=create_LSTM(n_units,input_shape,output_dim,filepath)
    lstm_model.fit(train_x,train_y,epochs=epochs,batch_size=batch_size,verbose=1)

    # 模型保存
    lstm_model.save(model_save_path)

    # 测试条数
    N= test_x.shape[0]
    predict=[]
    label=[]
    for start,end in zip(range(0,N,1),range(1,N+1,1)):
        print(f'start:{start}, end:{end}')
        sentence=[inverse_word_dictionary[i] for i in test_x[start] if i!=0]
        y_predict=lstm_model.predict(test_x[start:end])
        print('y_predict:',y_predict)
        label_predict=output_dictionary[np.argmax(y_predict[0])]
        label_true=output_dictionary[np.argmax(test_y[start:end])]
        print(f'label_predict:{label_predict}, label_true:{label_true}')
        # 输出预测结果
        print(''.join(sentence),label_true,label_predict)
        predict.append(label_predict)
        label.append(label_true)

    # 预测准确率
    acc=accuracy_score(predict,label)
    print('模型在测试集上的准确率:%s'%acc)

if __name__=='__main__':
    filepath='data/data_single.csv'
    input_shape=180
    model_save_path='data/corpus_model.h5'
    model_train(input_shape,filepath,model_save_path)
