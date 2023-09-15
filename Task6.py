import random

set1 = {random.randint(-10, 10) for i in range(20)}
set2 = {random.randint(-10, 10) for i in range(20)}
print('Полученные множества: ')
print(set1)
print(set2)
print('Элементы первого множества, которые встречаются во втором множестве: ')
print(set1 & set2)
