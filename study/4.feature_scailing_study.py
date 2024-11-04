# feature scailing : 데이터의 크기가 비슷해질 수 있도록 변경하는 작업 
# standard scailing, min max scailing, simple feature scailing 등이 있다.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


x = np.arange(-3,6).astype('float32').reshape(-1,1) # 메트릭스 형태의 넘파이 자료
x = np.vstack([x,[20]])

#simple

x_simple = x / x.max()
print(x_simple) # 이미지 처리에서 많이 사용하는 심플 스케일 예제

# min max
x_minmax = (x-x.min()) / (x.max() - x.min()) # 정석 계산

sc = MinMaxScaler()
x_minmax2 = sc.fit_transform(x) # 라이브러리 사용

# standard scailing

x_standard = (x -x.mean()) / x.std()

sc = StandardScaler()
x_standard2 = sc.fit_transform(x) # 라이브러리 사용