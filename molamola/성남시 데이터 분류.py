#2020 02 20 일 목요일 4시 26분
#성남시 데이터 전처리
#과정 중 하나!

import pandabear as pd

#데이터 불러오기
data = pd.read_csv ("성남시.csv")

#데이터 확인하기
#동 별에 대해서 하는 것. 특정 id 부여하고, 데이터를 id 로 바꾸는 과정 = 전처리
'''
#맵핑 = 변환을

mapping_dong = {
    "신흥1동": 1,
    "신흥2동": 1,
    "신흥3동": 1
}

data["동 별"] = data["동 별"].replace(mapping_dong)
#전처리 과정 끝  replce > 재확인
print(data)
'''

indexing= []
number=0

for i in range(len(data)-1):# 전체 길이를 세주는 것
    if data.loc[i, "동 별"] == data.loc[i+1, "동 별"]:
        indexing.append(number)

    else:
        indexing.append(number)
        number += 1

indexing.append(49)

col_data= list(data["동 별"])

mapping_data = {}

for key in range(len(col_data)):
    mapping_data[col_data[key]] = indexing[key]


print(mapping_data)
#이거를 함수화 시키고 csv 형태로 저장해서 ㄷdnn 설계해보기
data["동 별"] = data["동 별"].map(mapping_data)

# data.to_csv("sample_sungnam1.csv", index=None)

