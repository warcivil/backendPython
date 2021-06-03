def solve(lst):
    '''
    если наш обьект это int или float, то добавляем 1
    если это str, то смотрим, если он есть в словаре, то преобразуем в цифру из 16сс иначе ничего
    не делаем
    если это кортеж или массив выводим его длину
    если операция не найдена, то пишем not found operation
    '''
    key_word = dict(a=10, b=11, c=12, d=13, e=14, f=15)
    for i in range(len(lst)):
        if(isinstance(lst[i], int) or isinstance(lst[i], float)):
            lst[i] = lst[i]+1
        elif(isinstance(lst[i], str)):
            if(lst[i] in key_word):
                lst[i] = key_word[lst[i]]
        elif(isinstance(lst[i], tuple) or isinstance(lst[i], list)):
            lst[i] = len(lst[i])
        else:
            lst[i] = "not found operation"
    return lst
lst=[1, 2, 3]
print(isinstance(lst[0], int))
print(solve([1, 2, 3, "a", type(10), (1, 2, 3)]))


