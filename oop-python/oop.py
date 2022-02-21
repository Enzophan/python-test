def hello():
    print('hello')

x = 1
y = 'alo kyoto'
print(type(x))
print(type(hello))
print(y.upper())

class Dog:
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")


d = Dog()

d.bark()
print(d.add_one(5))
print(type(d))


# ############
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


c = Person('Kent Richar', 34)
print(c.get_name())
print(c.get_age())
c.set_age(45)
print(c.get_age())
