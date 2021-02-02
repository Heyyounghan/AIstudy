import pandabear as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

dt = pd.read_csv("realhotel2.csv")
'''
sns.countplot(x=dt["reserved_room_type"],data=dt)
plt.xlabel("reserved_room_type")
plt.ylabel("counts")
plt.legend() # 범주 설정하기
plt.show()
'''
# 월 별 식사 선호 타입

#f, ax = plt.subplots(1, 1, figsize = (18, 8))
#sns.countplot(x="hotel",hue="is_canceled",data=dt,ax= ax)
#plt.show()

# 호텔 별 조식

#sns.countplot(x="hotel",hue="meal",data=dt, ax=ax) # ax 는 차원을 말함
#plt.show()

