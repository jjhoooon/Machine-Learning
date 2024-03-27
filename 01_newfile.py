import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# numpy : array(list) ---> serires
# pandas : series ---> dataframe

a=[1,2,3]
# print(type(a))
# <class 'list'>

b = np.array(a)

# print(b)

# print(type(b)) 
# <class 'numpy.ndarray'>

# print(a*3)
#list : for문 형식으로 출력

# print(b*3)
#array : 결합법칙 적용.

# print(b.shape)
# (3,) : 차원표시

# print(a[0], b[0])
#list, array : 둘다 index 출력 가능.

# b=np.array([[1,2,3],[4,5,6]])

# print(b.shape)
# print(type(b))
# (2, 3)
# <class 'numpy.ndarray'>

# print(b[0][2])

a = [1,2,3,4,5]
a_array = np.array(a) #list -> array
a_series = pd.Series(a)

# print(a)
# print(a_array)

# print(a_series)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# print(type(a_series))
# <class 'pandas.core.series.Series'>

# n = pd.Series([10,20,30], index = ['a','a_array','a_series'])
# print(n)
# a           10
# a_array     20
# a_series    30
# dtype: int64


# raw_data = {'col0':[1,2,np.NAN,4],
#             'col1':[10,20,30,40],
#             'col2':[100,200,300,400]}
# print(raw_data, type(raw_data))
#<class 'dict'>

# data = pd.DataFrame(raw_data)

# print(data)
#    col0  col1  col2
# 0     1    10   100
# 1     2    20   200
# 2     3    30   300
# 3     4    40   400

# print(data['col1'])
# 0    10
# 1    20
# 2    30
# 3    40

# print(type(data['col1']))
# Name: col1


# print(type(data))
# <class 'pandas.core.frame.DataFrame'>

df = pd.DataFrame({
    'A': 1.,
    'C': pd.Series(),
});
