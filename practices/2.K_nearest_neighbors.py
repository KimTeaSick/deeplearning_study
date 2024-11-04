# 데이터가 커지면 느려진다는 치명적인 단점이 있다. 
# 아웃레이어, 미싱 벨류의 영향이크다.
# 구현이 쉽다는 장점이 있다.
# 피타고라스에 의한 거리 데이터를 구한다.

import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix

import seaborn as sns

import matplotlib.pyplot as plt

# 내장 데이터 가져오기
iris = load_iris()

X = iris.data[:,:2]
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0) #test 데이터 크기와 데이터를 랜덤으로 섞는 프롭
 
clf = KNeighborsClassifier(n_neighbors=15, weights='uniform')
clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test) 

result = accuracy_score(Y_test, Y_pred) # 점수 계산

print('result :',result)

for i in range(3):
  plt.scatter(X_train[Y_train == i, 0],X_train[Y_train == i, 1], label=i)

plt.legend()

cm = confusion_matrix(Y_test, Y_pred)

ax = sns.heatmap(cm)