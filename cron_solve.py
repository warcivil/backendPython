import schedule


def decoException(func):
    def wrapper(fib):
        if(not isinstance(fib, Fib)):
            print("Проверьте данные которые передаются в генератор там должен быть обьект класса fib")
            return None
        from time import time
        time_now = time()
        gen = func(fib)
        print(f"время cоздания генератора: {time_now - time()}")
        return gen
    return wrapper

class Fib:
    '''итераток который возврашает числа фиббоначчи'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

@decoException
def fib_gen(fib):
    '''Генератор который возврашает числа фиббоначи благодаря классу итератору'''
    for i in fib:
        yield i
def start_gen(counter:int):
    fib = fib_gen(Fib(counter))
    for i in fib:
        print(i)
def start_iter(counter:int):
    fib=Fib(counter)
    for i in fib:
        print(i)

if __name__ == '__main__':
    from random import randint
    schedule.every(60*3).minutes.do(start_gen, counter=randint(30, 100))
    schedule.every().day.at("15:15").do(start_iter, counter=randint(20, 60))
    schedule.every().sunday.at("12:00").do(start_iter, counter=randint(20, 100))
