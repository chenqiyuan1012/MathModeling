import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import  PCA
def read_excel(filename):
    #返回值是Dataframe的形式
    data=pd.read_excel(filename,sheet_name='Sheet1')
    return data

def standard_scaler(colum):
    #输入数据是一列
    average=float(sum(colum))/len(colum)
    total=0
    for value in colum:
        total+=(value-average)**2

    stdev=math.sqrt(total/len(colum))

    return pd.DataFrame([(x-average)/stdev for x in colum])

def pca(filename):
    data=read_excel(filename)
    pca=PCA(n_components='mle')
    pca.fit(data)
    reduced=pca.fit_transform(data)
    reduced=pd.DataFrame(reduced)
    #print(reduced)
    print(pca.explained_variance_ratio_)
    #print(pca.components_)

def correlation_matrix(data,score):
    data=pd.concat([data,score], axis=1)
    matrix=np.array(data)
    correlation_matrix=np.corrcoef(matrix)
    print(correlation_matrix)
    return correlation_matrix

def get_exception_value(filename):
    data=read_excel(filename)
    _,cols=data.shape
    index=data.columns.values
    print(filename+'异常值检测')
    for i in range(1,cols+1):
        outlier=data.boxplot(return_type='dict')
        x=outlier['fliers'][i].get_xdata()
        y=outlier['fliers'][i].get_ydata()
        y=list(y)
        print(str(index[i])+'的异常值为'+str(y))


#get_exception_value('白葡萄芳香物质.xlsx')
#get_exception_value('红葡萄芳香物质.xlsx')
#get_exception_value('白葡萄酒芳香物质.xlsx')
get_exception_value('红葡萄酒芳香物质.xlsx')
