import applepie as np
import pandabear as pd
from sklearn.impute import SimpleImputer # 보간법
import re


data = pd.read_csv("hotel_bookings.csv")

# print(data.isnull().sum()) 데이터 결측치 값 추정하기.

# pandas 라이브러리가 결측치를 인식할 수 있도록 변경하기.
# data= data.replace(' NULL' , np.nan)
#결측치 0으로 채워주기, fillna는 제일 귀찮을때
#data.fillna(0,inplace=True)
"""
imr = SimpleImputer(missing_values=np.nan, strategy='mean')
imr.fit(data["company"].values.reshape(-1,1))
Fix_data= imr.transform(data["company"].values.reshape(-1,1))

[[189.26673532]
 [189.26673532]
 [189.26673532]
 ...
 [189.26673532]
 [189.26673532]
 [189.26673532]
 """

# test = data["company"].fillna(method='ffill')
# 여기서는 ffill은 적절한 전처리 방법은 아님.


#null 값은 대부분 전체를 평균으로 쳐서 계산해버리는 경우가 많고.
#결측치를 없앤거임.


def mappingpoint(data, target, c=1):
    a=[]
    b= 0
    for i in range(len(data)-1):
        if data.loc[i, target] == data.loc[i + 1, target]:
            a.append(b)

        else:
            a.append(b)
            b += 1
    a.append(c)
    return a


a = mappingpoint(data=data, target='hotel')
# a 라는 리스트에 mappingpoint 0,1로 나누어 담은거임.

def mappingdic(i,j):
    a = list(i)
    c ={}
    for key in range(len(a)):
        c[a[key]] = j[key]

    return c

mapping_hotel= mappingdic(i=data["hotel"], j= a)

# print(mapping_hotel) # 딕셔너리 {'Resort Hotel': 0, 'City Hotel': 1}

data["hotel"] = data["hotel"].map(mapping_hotel)

# 호텔 맵핑 완료
# 데이터 Resort = 0, City Hotel = 1


# 식사 패키지  자동 넘버링  SC= 0, 식사 없음 BB=1, 침대,조식 HB= 2, 2끼 FB=3, 3끼

 # meal_mapping = {label: idx for idx, label in
   #               enumerate(np.unique(data['meal']))}

meal = data["meal"].unique()
#데이터 조회 # ['BB' 'FB' 'HB' 'SC' 'Undefined']

test = list(range(5))
# [0, 1, 2, 3, 4]

mapping_meal= {}

for key in range(len(meal)):
    mapping_meal[meal[key]] = test[key]

data["meal"] = data["meal"].map(mapping_meal)

# print(data['meal']) # {'BB': 0, 'FB': 1, 'HB': 2, 'SC': 3, 'Undefined': 4}

# meal part mapping done

data_month = data["arrival_date_month"].unique()
month_list = list(data_month)
#['July' 'August' 'September' 'October' 'November' 'December' 'January'
# 'February' 'March' 'April' 'May' 'June']

month_data = list((range(12)))
month_mapping= {}

for key in range(len(month_list)):
    month_mapping[month_list[key]] = month_data[key]

data["arrival_date_month"] = data["arrival_date_month"].map(month_mapping)

''''
    if data.loc[key, "arrival_date_month"] == data.loc[key+1, "arrival_date_month"]:
        month.append(m)
    else:
        month.append(m)
        m +=1
'''

#단순하고 짧은 코드를 찾아보쟝....
#data.loc = 데이터 경로


# arrival_Date_month= mapping 끝 !


data_market = data["market_segment"].unique()
'''['Direct' 'Corporate' 'Online TA' 'Offline TA/TO' 'Complementary' 'Groups'
 'Undefined' 'Aviation']'''

marketlist1 = list(data_market)
marketlist= list(range(8))
market_mapping={}

for key in range(len(data_market)):
        market_mapping[marketlist1[key]] = marketlist[key]

data['market_segment'] = data['market_segment'].map(market_mapping)

# market segment mapping 끝.

data_status = data["reservation_status"].unique()
#['Check-Out' 'Canceled' 'No-Show']
statuslist1= list(data_status)
statuslist = list(range(4))
ss=0
status_mapping = {}
for key in range(len(data_status)):
    status_mapping[statuslist1[key]] = statuslist[key]

data['reservation_status'] = data['reservation_status'].map(status_mapping)

# 예약 고객 상태 현황mapping

data_customer = data["customer_type"].unique()
print(data_customer)
customer = list(data_customer)
cuslist = list(range(4))
customer_mapping = {}
for key in range(len(data_customer)):
    customer_mapping[data_customer[key]] = cuslist[key]
print("cutomer mapping > \n", customer_mapping)
data_customer = data["customer_type"].map(customer_mapping)
#['Transient' 'Contract' 'Transient-Party' 'Group']


data_deposit = data["deposit_type"].unique()
#['No Deposit' 'Refundable' 'Non Refund']
deposit = list(data_deposit)
depolist = list(range(3))
deposit_mapping = {}
for key in range(len(data_deposit)):
    deposit_mapping[data_deposit[key]] = depolist[key]
print("deposit mapping > \n", deposit_mapping)
data_deposit = data["deposit_type"].map(deposit_mapping)

data["country"] = data["country"].fillna("PRT")
#print(data["country"].isnull().sum())

# print(dt["agent"].value_counts())
'''9.0      31961
240.0    13922
1.0       7191
14.0      3640
7.0       3539
         ...  
213.0        1
433.0        1
197.0        1
367.0        1
337.0        1
'''
data["agent"] = data["agent"].fillna(9)
# print(dt["agent"].isnull().sum())
data["company"] = data["company"].fillna(40)
#print(dt["company"].isnull().sum())
data["children"] = data["children"].fillna(0)
#print(data["children"].isnull().sum())


# data.to_csv("realhotel2.csv")
data.to_csv("realhotel.csv", index=False)



