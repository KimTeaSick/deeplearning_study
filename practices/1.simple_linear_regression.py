import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
# 단 변수 선형 회귀
dia = datasets.load_diabetes()
print(dia.feature_names)
print(dia.data.shape)
print(dia.target.shape)

df = pd.DataFrame(dia.data, columns=dia.feature_names)

# 데이터 불러오고 값 설정

dia_X = df['bmi'].values.reshape(-1, 1)

dia_X_train = dia_X[:-20]
dia_X_test = dia_X[-20:]

dia_Y_train = dia.target[:-20]
dia_Y_test = dia.target[-20:]

# 학습자료와 테스트 셋으로 분류

regr = linear_model.LinearRegression()
regr.fit(dia_X_train, dia_Y_train) # 선형 학습 

regr.coef_ #기울기
regr.intercept_ #절편

y_pred = regr.predict(dia_X_test)

plt.scatter(dia_X_test, dia_Y_test, label = 'true value')
plt.plot(dia_X_test, y_pred, color='red', label='pradicted')
plt.xlabel('bmi')
plt.ylabel('progress')
plt.legend()

# 학습후 그래프 그리기

print('r2_score', r2_score(dia_Y_test, y_pred))
print('mean_squared_error', mean_squared_error(dia_Y_test, y_pred))

# 모델 평가

# 다 변수 선형 회귀
# dia_X = df['bmi','bp'].values # 두개는 이미 메트릭스 구조이니 reshape 과정이 필요없다.
dia_X = df.values # 이미 메트릭스 구조이니 reshape 과정이 필요없다.
dia_X_train = dia_X[:-20]
dia_X_test = dia_X[-20:]

dia_Y_train = dia.target[:-20]
dia_Y_test = dia.target[-20:]

# 학습자료와 테스트 셋으로 분류

regr = linear_model.LinearRegression()
regr.fit(dia_X_train, dia_Y_train) # 선형 학습 

regr.coef_ #기울기
regr.intercept_ #절편

y_pred = regr.predict(dia_X_test)

plt.scatter(dia_X_test, dia_Y_test, label = 'true value')
plt.plot(dia_X_test, y_pred, color='red', label='pradicted')
plt.xlabel('bmi')
plt.ylabel('progress')
plt.legend()

# 학습후 그래프 그리기

print('r2_score', r2_score(dia_Y_test, y_pred))
print('mean_squared_error', mean_squared_error(dia_Y_test, y_pred))