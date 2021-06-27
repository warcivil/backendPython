import zope.interface as interface


class ICar(interface.Interface):
    "интерфейс машины"

    def set_speed():
        "изменить скорость машины"

    def set_name():
        "изменить имя машины"


@interface.implementer(ICar)
class Car():
    def __init__(self, name_car, speed):
        self.name_car = name_car
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def set_name(self, name_car):
        self.name_car = name_car

    def __str__(self):
        return f"car name {self.name_car} his speed {self.speed}"


if __name__ == '__main__':
    car = Car("honda", 120)
    car.set_name("toyota")
    print(car)