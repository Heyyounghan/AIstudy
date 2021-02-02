import pandabear as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# KNN 분류학습 모델. import는 해당 모든 기능을 사용한다는 것  from 해당 기능으로부터 무엇을 사용하겠다는 의미


data = pd.read_csv('iris.csv')

#매핑mapping을 이용한 데이터 전처리 과정

mapping_data = {
    'Iris-setosa': 0, # 데이터에서 이 기능을 들어간다는 의미
    'Iris-versicolor': 1,
    'Iris-virginica' : 2
}

data[4]= data[4].map(mapping_data) # 부를 땐 대괄호 , map 함수는 해당 함수의 기능을 바꿔줌

print(data) #setosa 말고 다른 애들은 모
data_save = data.to_csv('sample_iris.csv')# 두 결측치라그럼

#> 여기까지가 데이터전처리
# 기계학습 Test day






