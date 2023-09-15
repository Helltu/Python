import random

number = input('Введите натуральное число больше 1: ')
if number.isdigit():
    number = int(number)
    if (number >= 2):
        print('Полученные целые числа: ')
        numbersArray = [random.randint(-100, 100) for i in range(number)]
        print(numbersArray)
        resArray = []
        for i in range(0, len(numbersArray)-1):
            resArray.append(numbersArray[i]+numbersArray[i+1])
        print('Полученные список, состоящий из сумм соседних чисел: ', resArray)
    else:
        print('Вы ввели не натуральное число больше 1')
else:
    print('Вы ввели не число')
