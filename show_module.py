from work_module import list_to_dict, string_intersec, longest_ascending_seq
from time import time
import random
def show_info(func, *args):
    print(f"имя функции: {func.__name__}")
    try:
        time_now = time()
        print(func(*args))
        print(f"время исполнения {time_now-time()}")
    except Exception as e:
        print(e)
    finally:
        print(end="\n")

def test():
    function_name = input("Введите выражение для вызова функции\n1.(l)ist_to_dict\n2.(s)tring_intersec\n3.(lo)ngest_ascending_seq \n")
    if(function_name == "l"):
        lst = [random.randint(-10, 10) for i in range(100)]
        print(f"сгенерированный массив {lst}")
        show_info(list_to_dict, lst)
    elif(function_name == "s"):
        letters = "abcdefg"
        str1 = ''.join(random.choice(letters) for i in range(10))
        str2 = ''.join(random.choice(letters) for i in range(10))
        print(f"сгенерированные строки\n{str1}\n{str2}")
        show_info(string_intersec, str1, str2)
    elif(function_name == "lo"):
        lst = [random.randint(1, 10) for i in range(15)]
        print(f"сгенерированный список: {lst}")
        show_info(longest_ascending_seq, lst)

def auto_test(counter:int) -> None:
    while (counter > 0):
        print(f"TEST{counter}")

        show_info(list_to_dict, [random.randint(-10, 10) for i in range(100)])
       
        letters = "abcdefg"
        str1 = ''.join(random.choice(letters) for i in range(10))
        str2 = ''.join(random.choice(letters) for i in range(10))
        show_info(string_intersec, str1, str2)
        
        show_info(longest_ascending_seq, [random.randint(1, 10) for i in range(15)])
        counter-=1

if __name__ == '__main__':
    test()
    auto_test(15)