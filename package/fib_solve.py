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

def decoException(func):
    def wrapper(fib):
        if(not isinstance(fib, Fib)):
            print("Проверьте данные которые передаются в генератор там должен быть обьект класса fib")
            return None
        from time import time
        time_now = time()
        gen = func(fib)
        for i in gen:
            print(i)
        print(f"время выполнения: {time_now - time()}")
    return wrapper
@decoException
def fib_gen(fib):
    '''Генератор который возврашает числа фиббоначи благодаря классу итератору'''
    for i in fib:
        yield i


if __name__ == '__main__':
    fib = Fib(100)
    print("ИТЕРАТОР")
    for i in fib:
        print(i)
    print("ГЕНЕРАТОР")
    fib_gen(fib)