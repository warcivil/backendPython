from random import randint


def logical_posl():
    '''генерируем случайную последовательность,а потом с помощью признаком делимости фильтруем ее'''
    lst = [randint(1, 100) for i in range(20)]
    return list(filter(lambda x: x % 2 == 1 or x %
                             6 == 0 and x % 3 == 0, lst))


print(logical_posl())
