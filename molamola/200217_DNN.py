import pandabear as pd
import applepie as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split  #훈련, 테스트 데이터 분리, 그리드 서치 등의 기능 제공
from keras.layers import Dense #은닉층
from keras.models import Sequential # 신경망으로 묶기.
from keras.utils import to_categorical # 다중분류시에 사용

# 재현율 확보를 위한 Seed 사용

seed = 0

np.random.seed(seed)
tf.set_random_seed(seed) # 랜덤한 값을 고정시키기 위한 값 ,재현율 고정 f

# 텐서플로우에는 random 이 없고 set random seed 사용

data = pd.read_csv("sample_iris.csv")
X = data.values[:, :data.shape[1] -1]
y = data.values[:, data.shape[1] -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y) #stratify 데이터를 동일하게 균등시켜 주는 것

y_binary_train = to_categorical(y_train)
y_binary_test = to_categorical(y_test)


model = Sequential()
model.add(Dense(10, input_dim=5, activation="sigmoid"))
model.add(Dense(12, activation= "relu"))
model.add(Dense(12, activation= "relu"))
model.add(Dense(12, activation= "relu"))
model.add(Dense(3, activation="softplus"))
model.summary() # 은닉층이 몇 개 인지 알려줌
# 은닉층을 생성했다. 냠냠

model.compile(loss= "categorical_crossentropy", optimizer="adam", metrics=["acc"])
# 손실 함수를 정하는 것이다 3개 이상은 다중 분류를 사용한다.
history = model.fit(X_train, y_binary_train, validation_data=(X_test, y_binary_test),epochs=100, batch_size= 5)
# 테스트랑 트레이닝 셋을 비교해야한다. epochs , 학습주기  batch size  몇번을 끊어서 학습시킬건지.
print("iris_DNN of acc > %.4f" % (model.evaluate(X_test,y_binary_test)[1]*100))
print("iris_DNN of acc > %.4f" % (model.evaluate(X_train,y_binary_train)[1]*100))

y_prediction = model.predict_classes(X_train) # 학습을 했고 신경망이 다음과 같이 구분을 했다.
print(y_prediction)
# DNN 설계

# 시각화

acc = history.history["acc"]
val_acc = history.history["val_acc"]


plt.plot(acc, "r*--", label = "acc")
plt.plot(val_acc, "b*--", label = "val_acc")
plt.legend()
plt.show()

loss = history.history["loss"]
val_loss = history.history["val_loss"]

plt.plot(loss, "c^--", label = "loss")
plt.plot(val_loss, "d--", label = "val_loss")
plt.legend()
plt.show()

