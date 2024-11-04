import numpy as np
import pandas as pd

# series 와 data frame 으로 구성되어 있다. 
# serise 는 numpy array와 유사하다.
# data frame 은 serise을 모아둔 것이라 생각하면 된다.

np.random.seed(101)
data = np.random.randn(5,4)
df = pd.DataFrame(data)

print(df)

df = pd.DataFrame(data, columns=['A','B','C','D']) # 데이터에 컬럼을 매겨준다.

print(df)
print(df.columns) # 데이터의 컬럼을 알려준다.
print(df.info())  # 데이터의 정보를 알려준다
print(df.describe()) # 데이터의 분포를 알려준다

# 컬럼별 보기

print(df['A']) #
print(df.A)    # 동일 한 결괏값으로 A 컬럼에 대한 정보를 알려준다.
print(df[['A','C']]) # 여러개를 반환

# 컬럼 추가 삭제

df['NEW'] = df['A'] + df['B']
print(df)   # NEW 의 생성
df.drop('NEW', axis=1) # 메모리 안에서만 삭제
df.drop('NEW', axis=1, inplace=True) # 실제 데이터에서 삭제

# 미싱 데이터 관리
df = pd.DataFrame({'A':[1,np.nan,3],'B':[1,2,np.nan],'C':[np.nan,2,3]})
df.dropna()       # nan 삭제
df.dropna(axis=1) # 삭제
df.fillna(value=0) # nan을 0으로 채워라
df.fillna(df['A'].mean()) # nan을 A의 평균 값으로 채워라

df = pd.read_csv('winequality-red.csv', sep=';') # sep은 데이터를 나누는 특수문자를 나타낸다 default는 , 

print(df)
print(df.head())
print(df.tail())