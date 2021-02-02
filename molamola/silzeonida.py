import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import algorithm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel


df_wine= pd.read_csv("https://archive.ics.uci.edu/"
                     "ml/machine-learning-databases/wine/wine.data",
                     header=None)
print(df_wine)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid','Ash',
                   'Alcalinty of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocvanins',
                   'Color intensity','Hue', '0D280/0D315 of diluted wines',
                   'Proline']

print('클래스 레이블', np.unique(df_wine['Class label']))
print(df_wine.head())

X, y = df_wine.iloc[:,1:].values, df_wine.iloc[:,0].values
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0, stratify=y)
# stratify - 데이터를 일정한 기준으로 맞춰주는거 테스트싸이즈 7대 3 혹은 8ㄷㅐ 2

mms= MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)

stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.fit_transform(X_test)
print()
LogisticRegression(solver='liblinear', penalty='l1')
print()
lr= LogisticRegression(solver='liblinear', multi_class='auto',
                       penalty='l1', random_state=42)

lr.fit(X_train_std, y_train)

print('훈련 정확도', lr.score(X_train_std, y_train)*100)
print('테스트 정확도:', lr.score(X_test_std, y_test)*100)
print()
print(lr.intercept_)
print()
print(np.set_printoptions(8))
print(lr.coef_[lr.coef_ !=0].shape)
print(lr.coef_)


fig = plt.figure()
ax = plt.subplot(111)

colors = ['blue', 'green','red','cyan',
          'magenta', 'yellow','black',
          'pink','lightgreen', 'lightblue',
          'gray', 'indigo', 'orange']

weights, params = [], []
for c in np.arange(-4.,6.):
    lr = LogisticRegression(solver='liblinear', multi_class='auto',
                            penalty= 'l1', C=10.**c, random_state= 0)
    lr.fit(X_train_std, y_train)
    weights.append(lr.coef_[1])
    params.append(10**c)

weights = np.array(weights)

for column, color in zip(range(weights.shape[1]),colors):
    plt.plot(params, weights[:,column],
             label=df_wine.columns[column + 1],
             color=color)

plt.axhline(0, color='black', linestyle= '--', linewidth=3 )
plt.xlim([10**(-5), 10**5])
plt.ylabel(['weights coefficient'])
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc= 'upper left')
ax.legend(loc= 'upper center',
          #bbox_to_anchor =(1.38, 1.03),
          ncol=1, fancybox=True)

plt.show()


