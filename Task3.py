import random

number = input('Введите натуральное число: ')
if number.isdigit():
    number = int(number)
    numbersArray = []
    print('Полученные целые числа: ')
    for i in range(number):
        numbersArray.append(random.randint(-100, 100))
        print(numbersArray[-1])
    resArray = []
    for i in range(0, len(numbersArray)-1):
        resArray.append(numbersArray[i]+numbersArray[i+1])
    print('Полученные список, состоящий из сумм соседних чисел: ', resArray)
else:
    print('Вы ввели не натуральное число')
