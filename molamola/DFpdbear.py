import pandas as pd
import numpy as np
from sklearn.preprocessing import  LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import  ColumnTransformer


df = pd.DataFrame([['green', 'M', 10.1 , 'class1'],
                   ['red', 'L',20, 'class2'],
                   ['blue','XL',11.2, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']

print(df)
print()

size_mapping = {
    'XL':3,
    'L':2,
    'M':1
}
df['size'] = df['size'].map(size_mapping)
print(df)
# 맵핑한건 붙여두자.

#inv_size_mapping= {v:k for k , v in size_mapping.items()}
#df['size].map(inv_size_mapping)

class_mapping = { label: idx for idx, label in enumerate ( np.unique(df['classlabel']))}
print(class_mapping)
print()

df['classlabel'] = df['classlabel'].map(class_mapping)
print(df)
print()

class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)
print(y)
print()

X = df[['color','size','price']].values
color_le = LabelEncoder()

X[:,0] = color_le.fit_transform(X[:,0])
print(X)
print()

#one= OneHotEncoder(categories=[0]) 실패~  다시하자~~~
#one.fit_transform(X).toarray()
#print(one)

oh_enc= OneHotEncoder(categories='auto')
col_trans= ColumnTransformer([('oh_enc', oh_enc, [0])], remainder = 'passthrough')
print(col_trans.fit_transform(X))

print(pd.get_dummies(df[['color','size','classlabel']]))
print(pd.get_dummies(df[['color','size','classlabel']], drop_first=True))

# 이것이 바로 원 핫 인 코 딩 이 다~~~~!!!!!