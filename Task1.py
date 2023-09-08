number = input('Введите натуральное число ')
if number.isdigit():
    SUMM = 0
    for i in range(0, len(number), 2):
        SUMM += int(number[i])
    print(SUMM)
else:
    print('Вы ввели не натуральное число')
