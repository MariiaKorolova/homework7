#1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
    а) Создать список и поместить туда имя самого молодого человека.
        Если возраст совпадает - поместить все имена самых молодых.
    б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
    в) Посчитать среднее количество лет всех людей из начального списка.

persons = [
    {"name": "Mary", "age": 15},
    {"name": "Alex", "age": 25},
    {"name": "Tim", "age": 45},
    {"name": "Vera", "age": 13}
]
min_age = 1110
for i in persons:
    if min_age > i['age']:
        min_age = i['age']
    result_list = []
l = min([i['age'] for i in persons])
result = [i['name'] for i in persons if i['age'] == l]
print(result)
for i in persons:
    if min_age == i['age']:
        result_list.append(i['name'])
print(result_list)

my_list_2 = ["Vlad", "Pavel", "Igor", "Vladislav", 'Tim']
for name in my_list_2:
    if name in ("Vlad", "Igor", "Tim"):
        print(name)

import numpy
inp_lst = [15, 25, 45, 13]
lst_avg = numpy.average(inp_lst)
print("Average value of the list:\n")
print(lst_avg)
print("Average value of the list with precision upto 3 decimal value:\n")
print(round(lst_avg,3))


#2)Даны два словаря my_dict_1 и my_dict_2.
    а) Создать список из ключей, которые есть в обоих словарях.
    б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
    в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
    г) Объединить эти два словаря в новый словарь по правилу:
        если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
        если ключ есть в двух словарях -
        поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
        {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}


my_dict_1 = {'family': 5, 'cats': 2, 'dogs': 4, 'fruits': 15}
my_dict_2 = {'girls': 8, 'boys': 3, 'students': 18, 'books': 7}
new_dict = dict(i for i in my_dict_1.items() if i[0] not in my_dict_2.keys())
print (new_dict)
my_dict_2.update(my_dict_1)
print (my_dict_2)