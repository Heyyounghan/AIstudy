import applepie as np
import pandabear as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential

# 데이터 불러오기

data = pd.read_csv("sample_sungnam1.csv")

#random seed 값 설정하기

seed = 0

np.random.seed(seed)
tf.set_random_seed(seed)

# 데이터 값 설정하기

x = data.values[:, :data.shape[1] -1]
y = data.values[:, data.shape[1] -1]# 어느 칼럼에 있는지
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

#데이터 검증하기.



#은닉층 설계