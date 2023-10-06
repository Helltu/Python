import math


def is_prime(a):
    try:
        for i in range(2, round(math.sqrt(a))):
            if a % i == 0:
                return False
        return True
    except Exception:
        print('Произошла ошибка!')
        return 0

print(is_prime(19))
