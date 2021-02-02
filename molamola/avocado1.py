import pandabear as pd
from pandabear import DataFrame

# 데이터 불러오기

data = pd.read_csv("avocado.csv")

# 데이터로 지역을 숫자로 전처리 해주기.

# 빈 리스트 생성하기

state = []
number = 0

for i in range(len(data)-1):
    if data.loc[i, "region"] == data.loc[i+1, "region"]:
# "" 내부에는 처리하려는 데이터에 존재하는 칼럼 이름을 넣어줘야 한다.
        state.append(number)
    else:
        state.append(number)
        number +=1


# .loc > label 을 통해 값을 찾을 수 있다. 정수형으로는 찾을 수 없고 .ix 는 판다스에서 내부 사용할 수 있는데
# 여기서는 못쓰나보당~~~ 검색해보기.

# conventinal = 1 organic = 0
# index 를 0으로 인덱스 삭제하기.
# 데이터를 정하고 데이터를 보고 어떤 부분을 전처리할지 한번 볼 것 .

mapping_type = {
    "conventional" : 1,
    "organic" : 0
}

data["type"] = data["type"].map(mapping_type)


#conventional  = 1 , organic = 0 이다.

print(data.numbering["region"])