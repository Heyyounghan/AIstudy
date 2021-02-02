import pandas as pd
from io import StringIO
from sklearn.impute import SimpleImputer
import numpy as np


csv_dt = \
"""
A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,,8.0
10.0,11.0,12.0
"""

df= pd.read_csv(StringIO(csv_dt))

imr= SimpleImputer(missing_values = np.NaN , strategy = 'mean') #기본값이 np.num . missing value/ 차원 안써도 됌
imr= imr.fit(df.values)
imputed_data = imr.transform(df.values)
print(imputed_data)
""" 보간법 이다 ~ ~ ~ 막 쓰지 마라아아~~~~ 성질을 보고 판단해서 보간법을 써라~~~ 막연한 일반화를 방지하기 """
print(df)

