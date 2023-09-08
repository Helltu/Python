import random

set1 = set()
set2 = set()
for i in range(10):
    set1.add(random.randint(-10, 10))
    set2.add(random.randint(-10, 10))
print('Полученные множества: ')
print(set1)
print(set2)
print('Элементы первого множества, которые встречаются во втором множестве: ')
print(set1.difference(set1.difference(set2)))
