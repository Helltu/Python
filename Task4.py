def how_try_except_finally_work():
    try:
        number = int(input("Введите строку или число "));
        if number == 0:
            number/=0
        elif number > 0:
            number = number +'str';
        elif number < 0:
            number /=10;
    except TypeError:
        print('\tОшибка преобразования типов!')
        return 0
    except ZeroDivisionError:
        print('\tОшибка деления на ноль!')
        return 0
    except Exception:
        print('\tКакая-то другая ошибка!')
        return 0
    else:
        print('\tПоздравляю, ошибок не произошло!')
        return number
    finally: 
        print("\tТак или иначе функция закончила свою работу")

print(how_try_except_finally_work())