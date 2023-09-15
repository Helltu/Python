number = input('Введите натуральное число ')
if number.isdigit():
    SUMM = 0
    for i in range(0, len(number), 2):
        SUMM += int(number[i])
    print('Сумма четных цифр введенного натурального числа: ' + str(SUMM))
else:
    print('Вы ввели не натуральное число')
