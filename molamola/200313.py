#비트코인 데이터 RNN + LSTM

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping


dt= pd.read_csv("bitstampUSD_1-min_data_2012-01-01_to_2019-08-12.csv")

# 전처리할 목록 1. 유닉스타임으로 설정된 Timestamp 2.
# NaN값을 없애줘야하고,  변수 스케일링 해주고, 순서 쓰지말기...

dt['date']= pd.to_datetime(dt['Timestamp'], unit='s').dt.date
group = dt.groupby('date')
Real_price= group['Weighted_Price'].mean()

# split data  데이터 쪼개기  시간을 나눠서 데이터 그룹화시킨

splitday=365
train1= Real_price[:len(Real_price)-splitday]
test1= Real_price[len(Real_price)-splitday:]

# 비트코인 가격 예측.
'''
# 길이값에 따른 정보 변경 
train = dt.loc[:splitday, ['Weighted_Price']]
test = dt.loc[splitday:, ['Weighted_Price']]
'''
ax = train1.plot() #트레이닝을 얼마나 하겠다 라는 의미
test1.plot(ax=ax)
plt.legend(['train1','test1']) # 범주 설정  하기
plt.show()

#  data preprocess

trainset = train1.values
trainset = np.reshape(trainset,(len(trainset),1))

sc= MinMaxScaler()
trainset = sc.fit_transform(trainset)
# NaN 값 다 채워주기.
X_train= trainset[0:len(trainset)-1]
y_train= trainset[1:len(trainset)]
X_train= np.reshape(X_train,(len(X_train),1,1))
                    #np.reshape 함수는 기존 데이터는 유지하고 차원과 형상만 변경

# building the model

model=Sequential()
model.add(LSTM(units=1, activation='sigmoid', input_shape=(None,1)))

model.add(Dense(units=1))

#RNN 컴파일링
model.compile(optimizer= 'adam', loss='mean_squared_error')
early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)
model.fit(X_train,y_train, batch_size= 30, epochs=100, verbose=1, callbacks=[early_stop])

prediction= model.predict(X_train)
plt.plot(prediction)
plt.show()
# visuallizing

