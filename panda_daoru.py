import pandas as pd 
# df = pd.read_excel('/Users/fangkai/Desktop/abroad/applying results.xlsx')
# print(df)
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
# print(load_iris().keys())
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
print(load_iris()['DESCR'])
iris = pd.DataFrame(load_iris()['data'])

#参数说明
# figsize=(10,10), 设置画布大小为10*10
# alpha=1，设置透明度，此处设置为不透明
# hist_kwds={"bins":20} 设置对角线上直方图参数
# 可通过设置diagonal参数为kde将对角图像设置为密度图
pd.plotting.scatter_matrix(iris, figsize=(10,10), alpha=1, hist_kwds={"bins":20})
plt.show()