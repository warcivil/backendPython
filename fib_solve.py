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
    for i in fib_gen(fib):
        print(i)