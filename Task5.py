jewelry = {'браслет': ['золото', 15, 3], 'кольцо': ['серебро', 5, 32], 'ожерелье': ['бронза', 1, 15], 'перстень': ['алмаз', 500, 2], 'браслет изумредный': [
    'изумруд', 200, 10], 'кольцо серебряное': ['серебро', 50, 100], 'браслет уникальный': ['метеорит', 100, 1], 'кольцо новое': ['рубин', 5, 320]}
cont_loop = True
while cont_loop:
    key = input("Выберите пункт меню:\n\t1)Просмотр описания\n\t2)Просмотр цены\n\t3)Просмотр количества\n\t4)Всю информацию\n\t5)Покупка\n\t6)До свидания\n")
    if key == '1':
        name = input('Введите название изделия, описание которого хотите просмотреть: ')
        if name in jewelry:
            print('Описание изделия "' + name + '": ' + jewelry.get(name)[0])
        else:
            print('В магазине нет такого изделия')
    elif key == '2':
        name = input('Введите название изделия, цену которого хотите просмотреть: ')
        if name in jewelry:
            print('Цена изделия "' + name + '": ' + str(jewelry.get(name)[1]))
        else:
            print('В магазине нет такого изделия')
    elif key == '3':
        name = input('Введите название изделия, количество которого хотите просмотреть: ')
        if name in jewelry:
            print('Количество изделия "' + name + '": ' + str(jewelry.get(name)[2]))
        else:
            print('В магазине нет такого изделия')
    elif key == '4':
        print('Вся информация обо всех изделиях магазина:')
        for item in jewelry:
            print('\t' + item + ':\n\t\tСостав: ' + jewelry.get(item)[0] + '\n\t\tЦена: ' + str(
                jewelry.get(item)[1]) + '\n\t\tКоличество: ' + str(jewelry.get(item)[2]))
    elif key == '5':
        name = input('Введите название изделия: ')
        amount = input('Ввелите количество изделий: ')
        if (not (amount.isdigit())):
            print('Введено некорректное значение количества')
        else:
            amount = int(amount)
            got = jewelry.get(name)
            if not (got):
                print('\tВ магазине нет такого изделия')
            elif got[2] < amount:
                print('\tВ магазине нет такого количество данного изделия')
            else:
                print('\tОбщая стоимость купленных изделий: ' +
                      str(got[1]*amount))
                print(
                    '\tКоличество данных изделий оставшихся в магазине: ' + str(got[2]-amount))
                jewelry[name][2] -= amount
    elif key == '6':
        print('\tПрограмма прекращает свою работу...')
        cont_loop = False
    else:
        print('Выберите корректный вариант')
