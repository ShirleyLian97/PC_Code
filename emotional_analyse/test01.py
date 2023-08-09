# 打好python基础很重要！

# 练习时间：2022/9/17 21:01
import tensorflow as tf
from  sklearn.model_selection import train_test_split
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt

(X_train_full, y_train_full),(X_test,y_test) = keras.datasets.fashion_mnist.load_data()
print(X_train_full)