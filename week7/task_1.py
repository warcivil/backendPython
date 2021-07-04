from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def __init__(self, name_car, speed):
        self.name_car=name_car
        self.speed=speed
    @abstractmethod
    def __str__(self):
        return f"car name {self.name_car} his speed {self.speed}"
        
class Car(Base):
    def __init__(self, name_car, speed):
        Base.__init__(self, name_car, speed)
    def __str__(self):
        return Base.__str__(self)


if __name__ == '__main__':
    car = Car("honda", 120)
    print(car)