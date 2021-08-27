from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel(r'.\酿酒白葡萄降维后.xlsx')
#data=data.drop('样品',axis=1)
#print(data)
X=np.array(data)
X_scaled=preprocessing.scale(X)
X_scaled=pd.DataFrame(X_scaled)
print(X_scaled)

model=KMeans(n_clusters=5)
y_pred=model.fit_predict(X_scaled)
for i in range(1,30):
    print("编号"+str(i)+"的类别为"+str(y_pred[i-1]))


''' km = KMeans(n_clusters=5).fit(X_scaled)
# 标签结果
rs_labels = km.labels_
# 每个类别的中心点
rs_center_ids = km.cluster_centers_

# 描绘各个点
plt.scatter(X[:, 0], X[:, 1], c=rs_labels, alpha=0.5)
# 描绘质心
# plt.scatter(rs_center_ids[:, 0], rs_center_ids[:, 1], c='red')

plt.show() '''
