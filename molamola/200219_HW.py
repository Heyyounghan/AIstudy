import pandabear as pd # 데이터 분석 조작하기
import applepie as np # 수치데이터 다루기
import matplotlib.pyplot as plt # 시각화
import tensorflow as tf

from sklearn.model_selection import train_test_split # 데이터 나누는 사이킷런 모델
from keras.layers import Dense # 층 만들기
from keras.models import Sequential # 층 묶어주기
from applepie import argmax

#랜덤 시드 고정, 임의의 숫자 5
seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

#데이터 불러오기

data = pd.read_csv("heart_kaggle.csv")

# 데이터 셋 생성
X = data.values[:, :data.shape[1] -1]
y = data.values[:, data.shape[1] -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)
#stratify 데이터를 동일하게 균등시켜 주는 것


#은닉층 구성 및 시퀀셜로 하나로 묶어주기 , 케라스 인공신경망 생성하기.
model = Sequential()
model.add(Dense(6, input_dim=13, activation="softplus"))
model.add(Dense(15, activation= "relu"))
model.add(Dense(15, activation= "relu"))
model.add(Dense(15, activation= "relu"))
model.add(Dense(1, activation="sigmoid"))
model.summary() # 은닉층이 몇 개 인지 알려줌
# relu를 제일 많이사용함  , OPTIMIZER > 아담을 제일 많이 사용하고, 다양한 함수들 넣어서 출어떠너

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["acc"])
history = model.fit(X_train, y_train, validation_data=(X_test, y_test),
                    epochs=200, batch_size=15)

print("heart of DNN acc > %.4f" % (model.evaluate(X_train, y_train)[1]*100))
acc = history.history["acc"]
val_acc = history.history["val_acc"]

prediction = np.random.choice(X_test.shape[0], 20)
prediction_show = X_test[prediction]
y_prediction = model.predict_classes(prediction_show)

for i in range(20):
    print("True > " + str(argmax(y_test[prediction[i]])) + " prediction > " + str(y_prediction[i]))


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


# 시각화
