import matplotlib.pyplot as plt
from catboost import CatBoostClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
data=pd.read_excel("1_1_2.xls",sheet_name="咳嗽")
print(data.info())
X_train, X_validation, y_train, y_validation = train_test_split(
    data.iloc[:, :-1], data.iloc[:, -1], test_size=0.3, random_state=1234)

categorical_features_indices = [0 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
print(categorical_features_indices)
model = CatBoostClassifier(iterations=50, depth=3, cat_features=categorical_features_indices, learning_rate=0.03, loss_function='Logloss',
                           logging_level='Verbose')
model.fit(X_train, y_train, eval_set=(X_validation, y_validation), plot=True,verbose=True)

print(model.get_best_score())


fea_ = model.feature_importances_
fea_name = model.feature_names_
print(fea_name,fea_)
plt.figure(figsize=(10, 10))
plt.barh(fea_name, fea_, height=0.5)
plt.savefig("p1.png")
plt.show()
