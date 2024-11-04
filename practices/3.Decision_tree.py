# 합쳐서 앙상블 모델을 만들 수 있다.
# 딥러닝의 기초가 된다.
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


iris = load_iris()

X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target, test_size=3, random_state=0)

clf = tree.DecisionTreeClassifier(max_depth=2, criterion='entropy')

clf.fit(X_train, Y_train)

y_pred = clf.predict(X_test)

accuracy_score(Y_test, y_pred)