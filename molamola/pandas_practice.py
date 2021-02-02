import pandabear as pd

# 딕셔너리로 판다스 : 시리즈 만들기
'''
dict_data = {'a': 1, 'b': 2, 'c': 3}
series_dt = pd.Series(dict_data)

print(type(series_dt))
print('\n')
print(series_dt.index)
print(series_dt.values)
'''
#리스트로 판다스: 시리즈 만들기
'''
list_dt = [ '붕어', '개복치','금붕어',274,3.14]
series_dt = pd.Series(list_dt)

print(type(list_dt))
print('\n')
print(series_dt)
print(series_dt.index)
print(series_dt.values)

# 튜플로 판다스: 시리즈 만들기

tup_dt = ( '금붕어', '1996년생', '미녀붕어',True)
series_dt = pd.Series(tup_dt, index=['이름','출생년도','별명','사실여부'])

print(series_dt[[1,2]])
print(series_dt['별명']) '''

# 데이터 프레임 , 딕셔너리

dict_frame = {
    'a1': [1,2,3],
    'a2': [4,5,6],
    'a3': []
}