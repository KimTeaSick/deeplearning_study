import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 점찍기
plt.plot(3,2,'o',c='r')
plt.show()

# 선긋기
plt.plot([1,2,3],[4,5,1])
plt.show()

# 타이틀 달아주기
x = [5,8,10]
y = [12,16,6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.plot(x,y)
plt.plot(x2,y2)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

# 바차트 
plt.bar(x, y)
plt.bar(x2, y2)
plt.title('bar chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

# 산점도
plt.scatter(x, y, label='x')
plt.scatter(x2, y2, label='x2')

plt.title('Scatter plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend() # 범례

# Histogram
x = np.random.randn(1000)
plt.hist(x, bins=10) #bins는 간격

plt.title('histogram')
plt.ylabel('Y axis')
plt.xlabel('X axis')