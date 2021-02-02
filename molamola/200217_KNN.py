
import pandabear as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
# KNN 알고리즘 사용을 위한 모듈

 #1. 전처리 하기 전 데이터 확인

data = pd.read_csv ("sample_iris.csv")
print(data.head())

# 지도학습 데이터

X = data.values[:, :data.shape[1] - 1]
Y = data.values[:, data.shape[1] - 1]

# X 트레인과 Y 트레인 train test split : 데이터를 마구 섞는다.

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.3,random_state=1)

# 2개의 개체를 다음과 같이 나눈다. 값을 유지시키기 위해서 고정값 1


knn = KNeighborsClassifier(n_neighbors=5)
# 거리값  K  거리값 정의하고 학습하는 것

knn.fit(X_train,Y_train)
#이 트레이닝으로 학습을 하겠다. 라는 의미
print('KNN iris of acc > ' , format(knn.score(X_test, Y_test)*100)) # X Y 트레인을 비교해서 값을 나타낸 것,

train_acc = [] # 트레이닝 정확도
test_acc = []  # 테스트 정확도를 리스트에 담아둠
k_list = range(1, 100) # 1부터 31까지를 / 거리값을 계산시 위치를 바꿔주면됌
for k in k_list:
    clf = KNeighborsClassifier(n_neighbors=k) #1부터 30까지의 모든 거리 값을 다 계산
    clf.fit(X_train, Y_train)
    train_acc.append(clf.score(X_train, Y_train)) # 리스트 증가 clf = knn
    test_acc.append(clf.score(X_test, Y_test)) # 트레이닝한거 테스트한거

# 시각화
plt.plot(k_list, test_acc, label= 'test_acc of ')
plt.plot(k_list, train_acc, label = 'train _ acc of')


plt.xlabel('k')
plt.ylabel('acc')
plt.legend()
plt.show()

 # > 여기까지가 KNN

