# Abstract factory pattern
from abc import ABC, abstractmethod


class StatusBar(ABC):
    def __init__(self, system: str):
        self.system = system

    @abstractmethod
    def create(self):
        pass


class MainPage(ABC):
    def __init__(self, system: str):
        self.system = system

    @abstractmethod
    def create(self):
        pass


class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print("Created status bar for {}".format(self.system))


class WindowsMainPage(MainPage):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print("Created main page for {}".format(self.system))


class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print("Created status bar for {}".format(self.system))


class LinuxMainPage(MainPage):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print("Created main page for {}".format(self.system))


class GUIAbstractFactory(ABC):

    @abstractmethod
    def get_status_bar(self) -> StatusBar:
        pass

    @abstractmethod
    def get_main_page(self) -> MainPage:
        pass


class WindowsGUIFactory(GUIAbstractFactory):
    def get_status_bar(self) -> StatusBar:
        return WindowsStatusBar()

    def get_main_page(self) -> MainPage:
        return WindowsMainPage()


class LinuxGUIFactory(GUIAbstractFactory):
    def get_status_bar(self) -> StatusBar:
        return LinuxStatusBar()

    def get_main_page(self) -> MainPage:
        return LinuxMainPage()


class Application:
    def __init__(self, factory: GUIAbstractFactory):
        self.factory = factory

    def create_gui(self):
        status_bar = self.factory.get_status_bar()
        main_page = self.factory.get_main_page()
        status_bar.create()
        main_page.create()


def create_factory(system: str) -> GUIAbstractFactory:
    factory_dict = {
        "Windows": WindowsGUIFactory,
        "Linux": LinuxGUIFactory
    }
    return factory_dict[system]()


if __name__ == "__main__":
    system = "Linux"
    ui = create_factory(system)
    app = Application(ui)
    app.create_gui()

########################################
# Command Pattern
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def do(self):
        pass

    def undo(self):
        pass


class LunchCommand(Command):
    def __init__(self, lunch):
        self.lunch = lunch

    def do(self):
        self.lunch.make_lunch()

    def undo(self):
        self.lunch.stop_lunch()


class Lunch:
    def make_lunch(self):
        print("Lunch is being made")

    def stop_lunch(self):
        print("It was so tasty")


class MealInvoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.do()

    def stop(self):
        self.command.undo()


if __name__ == '__main__':
    lunch1 = Lunch()  # receiver
    command_lunch = LunchCommand(lunch1)  # concrete command

    meal_invoker = MealInvoker(command_lunch)  # invoker
    meal_invoker.invoke()
    meal_invoker.stop()


#######################################
# Facade pattern
class Ordering:  # Subsystem 1
    def order(self):
        print("Ordering")


class Preparing:  # Subsystem 2
    def prepare(self):
        print("Preparing...")


class Delivering:  # Subsystem 3
    def deliver(self):
        print("Delivering...")


class Operator:
    """
    Facade
    """
    def __init__(self):
        self.ordering = Ordering()
        self.preparing = Preparing()
        self.delivering = Delivering()

    def complete_order(self):
        self.ordering.order()
        self.preparing.prepare()
        self.delivering.deliver()


"""
main method
"""

if __name__ == "__main__":
    op = Operator()
    op.complete_order()


#####################################
# Factory Method Pattern
class Pizza:
    def __init__(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(5.5)


class PizzaMeat(Pizza):
    def __init__(self):
        super().__init__(9.5)


def create_pizza(pizza_type: Pizza) -> None:
    print("Creating your Pizza")
    ready_pizza = pizza_type.get_price()
    print(f"Please, pay: {ready_pizza}")


if __name__ == "__main__":
    create_pizza(PizzaMeat())


#######################################
# Interface
from abc import ABC, abstractmethod


class Device(ABC):

    @staticmethod
    @abstractmethod
    def power_on():
        pass


class Router(ABC):

    @staticmethod
    @abstractmethod
    def route():
        pass


class NetworkDevice(Device, Router):

    @staticmethod
    def power_on():
        print("Ready to process traffic")

    @staticmethod
    def route():
        print("Routify success")


r = NetworkDevice()
r.power_on()
r.route()


######################################
# Proxy
class Image:
    def __init__(self, filename):
        self.filename = filename

    def load_image_from_disk(self):
        print("loading " + self.filename)

    def display_image(self):
        print("display " + self.filename)


class Proxy:
    def __init__(self, subject):
        self.subject = subject
        self.proxystate = None


class ProxyImage(Proxy):
    def display_image(self):
        if self.proxystate is None:
            self.subject.load_image_from_disk()
            self.proxystate = 1
        print("display " + self.subject.filename)


image1 = ProxyImage(Image("photo 1"))
image2 = ProxyImage(Image("photo 2"))

image1.display_image()
image1.display_image()
image2.display_image()
image2.display_image()
image1.display_image()


########################################
# singleton
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=MetaSingleton):
    pass


config1 = Config()
config2 = Config()
print(config1, config2)
