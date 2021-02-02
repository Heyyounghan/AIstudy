import applepie as np
import pandabear as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# 데이터분석하고 데이터 자동분류하고, DNN 으로 하기 .
# 시각화를 이용한 데이터 분석. 일단 데이터 전처리 먼저해야대애애애애액
# 전처리 과정 설명을 써두고  보고서 작성하기.


data = pd.read_csv('hotel_bookings.csv')

# 연관 관계 짓기.

f, ax= plt. subplots(1, 1,figsize=(18,8))
sns.countplot('hotel', hue='is_canceled',data=data, ax=ax)
plt.show()

f, ax = plt.subplots(1, 1, figsize=(18, 8))
sns.countplot('children', hue='is_repeated_guest', data=data, ax=ax) # hue 는 어떤 칼럼을 주체적으로 할 것인지.
plt.show()

sns.relplot(x="reserved_room_type", y="stays_in_week_nights", hue="country", data=data)
plt.show()