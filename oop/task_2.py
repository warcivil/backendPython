class BaseCar:
    car: str

    def __init__(self, car) -> None:
        self.car = car

    def __str__(self) -> str:
        return f"car {self.car}"


class TypeCar(BaseCar):
    __type_car: str

    def __init__(self, car, type_car):
        BaseCar.__init__(self, car)
        self.__type_car = type_car

    def __str__(self):
        type_name = BaseCar.__str__(self) + " type:" + self.__type_car
        return type_name


class TypeCar(BaseCar):
    __type_car: str

    def __init__(self, car, type_car):
        BaseCar.__init__(self, car)
        self.__type_car = type_car

    def __str__(self):
        answer = BaseCar.__str__(self) + "\ntype:" + self.__type_car
        return answer


class UpdateCar(BaseCar):
    def update(self):
        answer = BaseCar.__str__(self) +"\n"+ "update: " + "engine"
        return answer