from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from xgboost import XGBClassifier
from xgboost import plot_importance
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
data = pd.read_excel("1_final.xls", sheet_name="0")
print(data.info())
X, y = data.iloc[:, :-1], data.iloc[:, -1]


def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Accuracy")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training Acc")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation Acc")

    plt.legend(loc="best")
    return plt



# 图二



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
print("AUC: %.4f" % metrics.roc_auc_score(y_test, y_pred))
print('ACC: %.4f' % metrics.accuracy_score(y_test, y_pred))
print('Recall: %.4f' % metrics.recall_score(y_test, y_pred))
print('F1-score: %.4f' % metrics.f1_score(y_test, y_pred))
print('Precesion: %.4f' % metrics.precision_score(y_test, y_pred))

plot_importance(model)
plt.show()


X,y=x_smote_resampled,y_smote_resampled
title = r"Learning Curves (xgboost)"
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
estimator = XGBClassifier(learning_rate=0.1,
                          n_estimators=3000,
                          max_depth=6,
                          min_child_weight=1,
                          gamma=0,
                          subsample=0.8,
                          colsample_bytree=0.8,
                          nthread=4,
                          scale_pos_weight=1,
                          seed=27)    # 建模
plot_learning_curve(estimator, title, X, y, (0.7, 1.01), cv=cv, n_jobs=1)
plt.savefig("learning_state.png")
plt.show()


'''
AUC: 0.9240
ACC: 0.9234
Recall: 0.9381
F1-score: 0.9216
Precesion: 0.9057
'''
