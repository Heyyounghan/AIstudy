import pandas as pd
import numpy as np
#%matplotlib inline 주피터에만 사용 가능 .
import matplotlib.pyplot as plt
from pandas.tseries.offsets import MonthEnd
# LSTM의형식.
df = pd.read_csv("cansim-0800020-eng-6674700030567901031.csv",
                 skiprows=6, skipfooter=9,
                 engine='python')


df['Adjustments'] = pd.to_datetime(df['Adjustments']) + MonthEnd(1)
# to_datetime = 문자열로 있는걸 객체로 바꿔주는 라이브러리.  MonthEnd (그 달의 맨 끝날짜에 맞춰서 전처리가 된다는 것)
df = df.set_index('Adjustments')
df.plot()

# 딥러닝에서 가장 중요한 전처리는 최대한 쓰레기 데이터를 없애주는 것.
# RNN에서 가장 중요한건 학습하기 유용하게 데이터를 맞춰줘야함. / 하이퍼블릿 탄젠트, 시그모이드를 많이 사용함../ 활성함수에 따라 결과값이 엄청 틀림.
# 지나친 일반화 안됌 날짜 개념 재정립. 테스트와 트레이닝 셋을 명확하게 해줘야함.
# train and test split 스플릿하는 과정.

split_date = pd.Timestamp('01-01-2011')
# 데이터에 대한 날짜 개념을 정확하게 알고 있어야함. 지나친 일반화는 값이 이상함
train = df.loc[:split_date, ['Unadjusted']]
test = df.loc[split_date:, ['Unadjusted']]

ax = train.plot() #트레이닝을 얼마나 하겠다 라는 의미
test.plot(ax=ax)
plt.legend(['train','test']) # 범주 설정하기
plt.show()

# 변수 스케일링

from sklearn.preprocessing import MinMaxScaler

'''머신러닝에서 데이터를 모델에 트레이닝할 때, 일반적으로 데이터를 Scaling 해서 사용한다. 
Scaling을 통해 데이터의 Scale을 맞추면 Weight의 scale도 일관성 있도록 맞출 수 있을 것이다.
MinMax Scaling은 최댓값 = 1, 최솟값 = 0으로 하여, 그 사에 값들이 있도록 하는 방법/
표준편차가 심할때는 스탠다드 스칼라~~(일반화 용) 장단점 파악해놓기. /민맥스는스케일조율 .. 
'''

sc = MinMaxScaler()
train_sc= sc.fit_transform(train)
test_sc= sc.transform(test)

# Pandas DataFrame 으로 변환하기

train_sc_df = pd.DataFrame(train_sc, columns=['Scaled'], index=train.index)
test_sc_df = pd.DataFrame(test_sc, columns=['Scaled'], index=test.index)

#Pandas shift 를 통한 Window 만들기

for s in range(1, 13):
    train_sc_df['shift_{}'.format(s)] = train_sc_df['Scaled'].shift(s)
    test_sc_df['shift_{}'.format(s)] = test_sc_df['Scaled'].shift(s)

# print((train_sc_df.head(13))) #dropna를 쓰는 경우.. 이런 경우가 극단적인 경우.. ;ㅅ;

X_train= train_sc_df.dropna().drop('Scaled', axis= 1)
y_train= train_sc_df.dropna()[['Scaled']]

X_test= test_sc_df.dropna().drop('Scaled', axis=1)
y_test= test_sc_df.dropna()[['Scaled']]


# 다시 Ndarray로 변환하기. #속도 향상을 위하여, numpy를 쓰는게 속도가 빠름. 성능향상을 위해서

X_train = X_train.values
X_test = X_test.values

y_train= y_train.values
y_test= y_test.values
'''
print(X_train.shape)
print(X_train)
print(y_train.shape)
print(y_train)
'''

# 최종 트레이닝 , 테스트 셋 X 만들기.
# Keras 에서 RNN 계열의 모델을 트레이닝 할 때 요구되는 데이터의 형식은 3차원 데이터
# 그 형태로 reshape 을 해줘야 한다.

X_train_t = X_train.reshape(X_train.shape[0],12, 1)
X_test_t = X_test.reshape(X_test.shape[0], 12,1)
'''
print("최종 데이터")
print(X_train_t.reshape)
print(X_train_t)
print(y_train)'''

# 최종 LSTM  모델 만들기
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping

K.clear_session()
model = Sequential() # 시퀀셜 모델
model.add(LSTM(20, input_shape=(12, 1))) # timestep, feature
model.add(Dense(1)) # output= 1
model.compile(loss='mean_squared_error', optimizer='adam')

model.summary()

early_stop = EarlyStopping(monitor='loss', patience=1, verbose=1)

model.fit(X_train_t, y_train, epochs=100,
          batch_size=30, verbose=1, callbacks=[early_stop])

print(X_test_t)

y_pred = model.predict(X_test_t)
print(y_pred)

plt.plot(y_pred, "r*--", marker='o')
plt.show()