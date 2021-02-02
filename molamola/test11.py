
"""
def delete_a_list_element(list_data,element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        return list_data
    else:
        return "False"

list_data=['a',1,'gachon','2016.0']
element= float(2016)
result= delete_a_list_element(list_data, element)

print(result)

def add_number(original_list):
    original_list += [1]
mylist=[1,2,3,4]
add_number(mylist)
print(set(mylist))

a= [3, 'appple', 2016, 4]
b= a.pop(0)
c= a.pop(1)

print(b+c)

def week_seven(sentence):
    cells= set(sentence.replace('','').lower())
    return cells

sentence_a="The quick brown fox jumps over the lazy dog"
sentence_b="I love you"

print(len(week_seven(sentence_a)-week_seven(sentence_b)))

tuple_1=(1,2,3)
tuple_2=(4,5,6)

def quiz_1(data_1, data_2):
    result= [ ]

    for i in (tuple_1+tuple_2):
        result.append(i)
    return result

print(quiz_1(tuple_1,tuple_2))

dict_1={2:1, 4:2, 6:3, 8:4, 10:6}

dict_keys= list(dict_1.keys())
dict_values= list(dict_1.values())

dict_2= dict()

for i in range(len(dict_keys)):
    dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])

animal =['cat','snake', 'monkey','ant','spider']
legs=[4,0,2,4,8]
animal_legs_dict= {}
for i in range(len(animal)):
    animal_legs_dict[legs[i]]= animal[i]

animal_legs_dict['ant']=6
print(animal_legs_dict)

sentence= list("You Love Me? ")
result= ''
for i in range(len(sentence)):
    if i % 3 == 0:
        result += sentence.pop()
    else:
        result += sentence.pop(0)
print(result)

number=[5,6,7,8,9,1,2,3,4]
result=[]
result.append(number.pop(0))
result.append(number.pop())
result.append(number.pop(1))
result.append(number.pop())
result.append(number.pop(0))
print(number[0]+result[-1])
"""

data_1={'one':(1,2,3,4,5,6), 'two':[1,2,3,4,5,6], 'three':{'four':4, 'five':5}}

for k in ['one','two','three']:
    try:
        print(data_1[k][:1])
    except TypeError:
        print("error")

for k in ['one','two','three']:
    try:
        data_1[k][-1] ="a"
        print(data_1[k][-1])
    except TypeError:
        print("error")

class_category = ["A","B","c","d"]
student_category = ["sam","sarah","jane","john"]

class_student_cate={}

for i in range(len(class_category)):
    class_student_cate[class_category[i]] = student_category[i]
print(class_student_cate)


fact= "Python is funny"

print(str(fact.count('n')+fact.find('n')+fact.rfind('n')))

text1='Gachon Cs50 - programming with python'
text2='Human cs50 knowledge belongs to the world'

text1.lower()

print(text1[:5]+text1[-1]+text1[6]+text2.split()[0])

class_name = 'introduction programmming with python'

for i in class_name:
    if i == 'python':
        i= i.upper()

print(class_name)

number=10
day=3
print(" I eat %d oranges every day" %number)

number=10
day="three"
print(" I eat {} oranges {} days".format(number,day))

result = "CODE2018"
print("{0},{1}".format(result[-1],result[-2]))

str_a= "this is"
str_b= "PythoN"
print(str_a.title() + "" + str_b.upper())

e=""
for e in range(1,21,2):
    print("{:^20}".format("*"*e)
