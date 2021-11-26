import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Альтернативный конструктор
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


x = Date(2000, 12, 11)

print(x.year)
print(Date.today().year)


##############################
from abc import ABC, abstractmethod


# SRP
class NewRectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw(self):
        print("Drawing the example")

    def area(self):
        return self.height * self.width


class GeometricRectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Rectangle(GeometricRectangle):
    def draw(self):
        print("Drawing the example")


# OCP
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def __repr__(self):
        return f"User: {self.username}, {self.age} years old"


###################################
class GameUser:
    def __init__(self, username, age, favorite_game):
        self.username = username
        self.age = age
        self.favorite_game = favorite_game

    def __repr__(self):
        return f"User: {self.username}, {self.age} years old, favorite game: {self.favorite_game}"


###################################
class NewUser:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def __repr__(self):
        return f"User: {self.username}, {self.age} years old"


class Gamer(NewUser):
    def __init__(self, username, age, favorite_game):
        super().__init__(username, age)
        self.favorite_game = favorite_game

    def __repr__(self):
        return f"User: {self.username}, {self.age} years old, favorite game: {self.favorite_game}"


######################################
# Liskov principle
class Car:
    def charge(self):
        pass

    def pump_petrol(self):
        pass


class Tesla(Car):
    def charge(self):
        print('Charging...')

    def pump_petrol(self):
        raise Exception('Not a gasoline car')


class AudiA3(Car):
    def charge(self):
        raise Exception('Not an electric car')

    def pump_petrol(self):
        print('Pumping...')


def recharge_car(car):
    car.charge()


tesla_car = Tesla()
audi_a3_car = AudiA3()
recharge_car(tesla_car)  # print Charging...
recharge_car(audi_a3_car)  # THIS RAISES EXCEPTION!


class Car:
    pass


class ElectricCar(Car):
    def charge(self):
        pass


class GasolineCar(Car):
    def pump_petrol(self):
        pass


class Tesla(ElectricCar):
    def charge(self):
        print('Charging...')


class AudiA3(GasolineCar):
    def pump_petrol(self):
        print('Pumping...')


def recharge_car(electric_car):
    electric_car.charge()


def pump_petrol(gasoline_car):
    gasoline_car.pump_petrol()


tesla_car = Tesla()
audi_a3_car = AudiA3()
recharge_car(tesla_car)  # print Charging...
pump_petrol(audi_a3_car)


######################################
# ISP
class GeometricInterface(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_diameter(self):
        pass


class Square(GeometricInterface):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_diameter(self):
        raise NotImplementedError


class Circle(GeometricInterface):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * 3.14 ** 2

    def get_diameter(self):
        return self.radius * 2


##################################
class GeometricInterface(ABC):

    @abstractmethod
    def get_area(self):
        pass


class CircleInterface(GeometricInterface, ABC):

    @abstractmethod
    def get_diameter(self):
        pass


class RectangleInterface(GeometricInterface, ABC):
    pass


class NewSquare(RectangleInterface):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width


class NewCircle(CircleInterface):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * 3.14 ** 2

    def get_diameter(self):
        return self.radius * 2


#########################################
# DIP
class Garage:
    def __init__(self):
        self.cars = []

    def add_car_to_garage(self, name, capacity):
        self.cars.append((name, capacity))  # eg: ('Tesla1', 50)


class ChargingStation:
    def __init__(self, garage):
        num = len([car for car in garage.cars if car[1] < 50])
        print(f'We need to charge {num} cars')


gar = Garage()
gar.add_car_to_garage('Tesla1', 50)
gar.add_car_to_garage('Tesla2', 30)
gar.add_car_to_garage('Tesla1', 80)
station = ChargingStation(gar)


#######################################
from abc import ABC, abstractmethod


class NewGarage(ABC):
    def __init__(self):
        self.cars = []

    @abstractmethod
    def add_car_to_garage(self, name, capacity):
        pass

    @abstractmethod
    def get_cars_that_needs_charge(self):
        pass


class MyGarage(NewGarage):
    def add_car_to_garage(self, name, capacity):
        self.cars.append((name, capacity))

    def get_cars_that_needs_charge(self):
        return [car for car in self.cars if car[1] < 50]


class ChargingStation:
    def __init__(self, garage):
        num = len(garage.get_cars_that_needs_charge())
        print(f'We need to charge {num} cars')


gar = MyGarage()
gar.add_car_to_garage('Tesla1', 50)
gar.add_car_to_garage('Tesla2', 30)
gar.add_car_to_garage('Tesla3', 80)
station1 = ChargingStation(gar)
