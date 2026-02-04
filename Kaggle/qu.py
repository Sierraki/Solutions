import pandas as pd
import numpy as np

train=pd.read_csv('Kaggle/titanic/train.csv')
# 导入测试数据集
test = pd.read_csv("Kaggle/titanic/test.csv")


print(train.head())

print(train.columns)
