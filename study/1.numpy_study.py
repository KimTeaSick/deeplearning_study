import numpy as np

# 뉴럴 네트워크는 벡터의 내적으로 계산된다.

# 스칼라 Scalar
x = 1

# 백터 Vector
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x.shape) # (3,)
print(np.dot(x,y)) # 벡터의 내적 계산함수

# 가장 큰 인덱스 값을 찾는 함수
print(np.argmax(x)) # 2
print(x.argmax()) # 2

# 메트릭스 Metrix
x = np.array([[1,2,3],[2,3,4],[5,6,7]])
print(x.shape) # (4, 3)

# [1,2,3]
# [2,3,4]
# [5,6,7]

print(x[:2,1:])   #앞에는 row, 뒤에는 col을 나타낸다. [[2 3],[3 4]]
print(x[1:2, :2]) #앞에는 row, 뒤에는 col을 나타낸다. [[2 3]]
print(np.arange(9).reshape(3,3)) #[[0,1,2][3,4,5][6,7,8]]
print(np.transpose(x)) # col 과 row 가 뒤바뀐다 [[1 2 5][2 3 6][3 4 7]]


# 텐서 Tensor
x = np.array([[[[0],[4]],[[8],[12]],[[16],[20]],[[24],[28]]]])

