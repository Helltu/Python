def my_func(a):
    try:
        if isinstance(a, list):
            sum = 0
            count = 0
            for item in a:
                if isinstance(item, int) or isinstance(item, float):
                    sum += item
                    count += 1
            if(count != 0):
                return (sum/count)
            else:
                return 0;
        elif type(a) == type(5):
            res = list(str(a))
            res.reverse()
            return int(''.join(res))
        elif type(a) == type({}):
            return dict(sorted(a.items(), key=lambda a: a[0]))
        elif type(a) == type('asd'):
            arr = a.split()
            arr = sorted(arr, key=len)
            print(arr[-1])
            return len(a.split())
        else:
            print('Данный параметр не подходит ни под один из заданных случаев')
            return False
    except Exception:
        print('Произошла ошибка!')
        return 0


print(myFunc([1.12, 1.666, 2]))
