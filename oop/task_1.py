import operator


class Summarizer:
    '''класс калькулятор'''

    __first_number: float
    __second_number: float
    sign: str

    def __init__(self, first_number, second_number, sign="+"):
        self.__first_number = first_number
        self.__second_number = second_number
        self.sign = sign
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '^': operator.xor,
        }

    def set_info(self, first_number, second_number, sign):
        '''изменим данные в классе'''

        self.__first_number = first_number
        self.__second_number = second_number
        self.sign = sign

    def __str__(self):
        '''изменим данные в классе'''

        if (self.sign in self.ops):
            return f"{self.__first_number}{self.sign}{self.__second_number}={self.ops[self.sign](self.__first_number, self.__second_number)}"
        else:
            return "not found operator"

    def __eq__(self, other):
        '''сравнение классов'''

        return self.ops[self.sign](
            self.__first_number,
            self.__second_number) == other.ops[other.sign](
                other.__first_number, other.__second_number)

    def __add__(self, other):
        '''сложим результат'''
        try:
            return self.ops[self.sign](
                self.__second_number,
                self.__first_number) + other.ops[self.sign](
                    self.__first_number, self.__second_number)
        except:
            raise ZeroDivisionError

    @staticmethod
    def get_obj(first_number, second_number, sign):
        '''вернем обьект класса'''

        return Summarizer(first_number, second_number, sign)
