from abc import ABC, abstractmethod, abstractstaticmethod
from datetime import datetime


class Worker(ABC):
    @abstractmethod
    def work(self):
        print("Doing job")


class Builder(Worker):
    def work(self):
        print("Building houses")


class Manager:
    def manage(self):
        print("Managing")


class SkyScraper:
    def creating(self, worker):
        print("Creating skyscraper")
        worker.work()


worker = Builder()

sc = SkyScraper()
sc.creating(worker)


#########################################
class Aircraft(ABC):

    @abstractmethod  # def fly(self):
    def fly(self):   # print(" My jet is flying")
        pass

    @abstractmethod
    def land(self):
        print("All systems worked well")


class Jet(Aircraft):

    def fly(self):
        print(" My jet is flying")

    def land(self):
        super().land()
        print("Jet has landed")


Boeing = Jet()
Boeing.fly()
Boeing.land()


###########################################
class Person(ABC):

    @staticmethod
    @abstractmethod
    def hello():
        print("This is a person")

    @staticmethod
    @abstractmethod
    def is_valid(age):
        pass


class Student(Person):

    @staticmethod
    def hello():
        print("This is a student")

    @staticmethod
    def is_valid(age):
        if 16 < age < 23:
            return True
        else:
            return False


class Adult(Person):

    @staticmethod
    def hello():
        print('Iam Adult')

    @staticmethod
    def is_valid(age):
        if age > 18:
            return True
        else:
            return False


Mike = Adult()
Mike.hello()
print(Mike.is_valid)


#########################################
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


a = Rectangle(10, 20)
print("area:", a.area())


##########################################
class Power:
    def __init__(self, func):
        self._func = func
        self._memory = []

    def __call__(self, a, b):
        result = self._func(a, b) * 2
        self._memory.append(result)
        return result

    def memory(self):
        return self._memory


@Power
def multiply(a, b):
    return a * b


print(multiply)
print(multiply(1, 2))
print(multiply(2, 2))
print(multiply(2, 4))
print(multiply.memory())


################################################
class Power:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, field1, field2):
        result = self.cls(2 * field1, 2 * field2)
        return result


@Power
class NormalClass:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __repr__(self):
        return self.field2 + self.field1


x = NormalClass("Mike", "Yatsenko")
print(x)


###############################################
class A:
    def __init__(self, a):
        self.a = a

    def __call__(self):
        return self.a


###############################################
class Dog:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def info(self):
        information = {"name": self.name, "weight": self.weight, "height": self.height}
        return information

    def barking(self):
        noise = ('{} is doing: Bark, Bark'.format(self.name))
        return noise


class AggressiveDog(Dog):
    def __init__(self, name, weight, height, aggression):
        super(AggressiveDog, self).__init__(name, weight, height)
        self.aggression = aggression

    def barking(self):
        return super().barking() + " .But stay away from it"

    """Aggressiveness could be medium or high"""

    def aggressiveness(self):
        print("This is {} and it is {} aggressive".format(self.name, self.aggression))
        return super().info()


class NonAggressiveDog(Dog):
    def __init__(self, name, weight, height, color):
        super(NonAggressiveDog, self).__init__(name, weight, height)
        self.color = color

    def happiness(self):
        print("{} its so friendly".format(self.name))
        return super().info()


Jack_Pug = NonAggressiveDog("Jack_Pug", 10, 20, "gray")
print(Jack_Pug.barking())
print(Jack_Pug.happiness())

# Mark_Boxer = AggressiveDog("Mark_Boxer", 20, 60, "mediumly")
# print(Mark_Boxer.barking())
# print(Mark_Boxer.aggressiveness())

print(NonAggressiveDog.mro())


##################################################
class A:
    def __init__(self, first, second):
        self.first = first
        self.second = second


obj1 = A(1, 2)

obj1.third = 3
obj1.fourth = 4
print(obj1.__dict__)


###################################################
class SlotClass:
    __slots__ = ('foo', 'bar')


class ChildSlotClass(SlotClass):
    __slots__ = ('baz',)


obj2 = ChildSlotClass()
obj2.foo = 1
obj2.bar = 2
obj2.baz = 3

print(SlotClass.__dict__)

