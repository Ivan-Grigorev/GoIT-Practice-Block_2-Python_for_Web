# Metaclass Introduction
# Everything in Python is an object
def sample():
    class IsItPossible:
        pass

    return IsItPossible


#####################################
# describing an idea of type function
class A:
    pass


def func():
    pass


print(type(A))
print(type(123))
print(type('string'))
print(type({}))
print(type(func))


#######################################
class MyList(list):
    def new_len(self):
        return len(self)


lst = MyList()
lst.append(1)
lst.append(4)
lst.append(2)
lst.append(3)
print(lst)
lst.sort()
print(lst.new_len())


########################################
# What is a type of a class?
class Test:
    pass


help(type)

print(Test())

Test2 = type('Test2', (), {})

print(Test2())

Test3 = type('Test3', (), {'some_name': "Mike"})

print(Test3().some_name)

t = Test3()
t.hello = 'Hello'
print(t.hello)


#########################################
# Full practise on type function
class Bar:
    def greeting(self):
        print("Hi")


def new_attr(self):
    self.z = 9


Test4 = type('Test3', (Bar,), {'some_name': "Mike", "new_attr": new_attr})
t = Test4()
t.new_attr()
print(t.z)

t.greeting()

MyLits2 = type('MyList', (list,), dict(new_len=lambda self: len(self)))
lst = MyList()
lst.append(1)
lst.append(4)
lst.append(2)
lst.append(3)
print(lst)
lst.sort()
print(lst.new_len())


############################################
class FirstMeta(type):
    def __new__(mcs, class_name, base, attrs):
        print(attrs)

        # after showing basic example
        return type(class_name, base, attrs)


class X(metaclass=FirstMeta):
    x = 12
    z = "some value"

    def hello(self):
        print('Hello!')


z = X()


##############################################
# Example of list meta
class MyMeta(type):
    def __new__(mcs, name, bases, attrs):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(mcs)
        return super(MyMeta, mcs).__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('-----------------------------------')
        print("Class init has been done", name)
        print(cls)
        print(attrs)
        super(MyMeta, cls).__init__(name, bases, attrs)


class MyClass(metaclass=MyMeta):

    def __init__(self):
        print("Object init has been done")


x = MyClass()


##############################################
# Call
class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        print('__call__ of ', str(cls))
        print('__call__ *args=', str(args))
        return type.__call__(cls, *args, **kwargs)


class MyClass(metaclass=MyMeta):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('MyClass object with a=%s, b=%s' % (a, b))

    def __call__(self):
        print(self.a * self.b)


print('gonna create foo now...')
foo = MyClass(1, 2)
foo()


#################################################
# second example
class FirstMeta(type):
    def __new__(mcs, class_name, base, attrs):
        print(attrs)

        # after showing basic example

        a = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value
        print(a)
        return type(class_name, base, a)


class JustNormal(metaclass=FirstMeta):
    x = 12
    z = 'some value'

    def hello(self):
        print('Hello!')


y = JustNormal()
print(y.x)


##############################################

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
