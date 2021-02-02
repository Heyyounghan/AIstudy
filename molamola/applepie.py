import pandabear as pd
import numpy as np
# 200309 numpy 를 사용해서 행렬만들기
# 파이썬에서 산술 계산을 위한 라이브러리

dt = np.random.randn(3,3)
'''
print("데이터의 표현>\n", dt)

# 덧셈
data_sum = dt + dt
print("result of sum > \n", data_sum)

# 뺄셈
data_minus = dt - dt
print("result of minus > \n", data_minus)

# 곱셈
data_multiple = dt * dt
print("result of multiple> \n", data_multiple)

# 나눗셈
# 작성해보기

#numpy에 0으로 가득 행렬 채우기

data_zero = np.zeros(9)
# 순수한 행렬을 만들어서 이 값에 대해 다른 값을 넣고싶을 때 사용하기

test_dt = list(range(14))

np_range = np.arange(13)
print(np_range)
print(test_dt)
'''
# randomseed 값을 고정시켜주는 것, 값에 있는 표준편차를 일정하게 고정시켜 주는 것
seed = 7
np.random.seed(seed)

# 값을 고정시키는데 최적의 함수 텐서플로우와 함께 값 고정하는데 잘 쓸 수 있음 !


