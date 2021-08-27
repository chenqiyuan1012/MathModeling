from sklearn import metrics
from xgboost import XGBClassifier
from xgboost import plot_importance
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
data = pd.read_excel(
    r"D:\document\数学建模\比赛代码与文件\202107培训\22hz\T1\头晕头昏头痛\头晕头昏头痛.xlsx", sheet_name="Sheet1")
print(data.info())
X,y=data.iloc[:, :-1], data.iloc[:, -1]


groupby_data_orginal = data.groupby('label').count()
print(groupby_data_orginal)
model_smote = SMOTE()  # 建立smote模型对象
x_smote_resampled, y_smote_resampled = model_smote.fit_resample(X, y)
x_smote_resampled = pd.DataFrame(x_smote_resampled)
y_smote_resampled = pd.DataFrame(y_smote_resampled)
smote_resampled = pd.concat([x_smote_resampled, y_smote_resampled], axis=1)
groupby_data_smote = smote_resampled.groupby('label').count()
print(groupby_data_smote)
X_train, X_test, y_train, y_test = train_test_split(
    x_smote_resampled, y_smote_resampled, test_size=0.3, random_state=1234)


model = XGBClassifier(learning_rate=0.1,
                      n_estimators=1000,
                      max_depth=6,
                      min_child_weight=1,
                      gamma=0,
                      subsample=0.8,
                      colsample_bytree=0.8,
                      nthread=4,
                      scale_pos_weight=1,
                      seed=27)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
print('ACC: %.4f' % metrics.accuracy_score(y_test, y_pred))
print('Recall: %.4f' % metrics.recall_score(y_test, y_pred, average='macro'))
print('F1-score: %.4f' % metrics.f1_score(y_test, y_pred, average='macro'))
print('Precesion: %.4f' % metrics.precision_score(
    y_test, y_pred, average='macro'))


plot_importance(model)
plt.savefig(r"D:\document\数学建模\比赛代码与文件\202107培训\22hz\T1\头晕头昏头痛\importance.png")
plt.show()
y_predict = pd.DataFrame(model.predict(X), columns=["predict"])
final = pd.concat([X, y, y_predict], axis=1)
print(final)
final.to_excel(r'D:\document\数学建模\比赛代码与文件\202107培训\22hz\T1\头晕头昏头痛\result.xlsx')

'''
ACC: 0.9052
Recall: 0.9062
F1-score: 0.9048
Precesion: 0.9047
'''
