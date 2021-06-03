string_mas = ["Hello", "world", "hello", "this", "beautiful world"]
from functools import reduce
def red_string(new_string):
    "складываем предыдущий и следующий аргумент массива"
    new_string = reduce(lambda prev_el,el: prev_el+" "+el, string_mas)
    return new_string
print(red_string(string_mas))