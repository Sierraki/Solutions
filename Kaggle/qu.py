import pandas as pd
import numpy as np

train=pd.read_csv('Kaggle/titanic/train.csv')
#导入测试数据集
test=pd.read_csv('Kaggle/titanic/test.csv')
print('训练数据集：',train.shape,'测试数据集',test.shape)


#合并数据集，方便对数据进行清洗
full = pd.concat([train, test], ignore_index=True)