class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and {self.age} years old")

    def speak(self):
        print("I don't know what i say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"i am {self.name} and {self.age} years old and {self.color} color")
 


class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet('Mimi', 10)
p.show()
p.speak()

c = Cat('Tony', 11, 'Red')
c.show()
c.speak()

d = Dog('Bod', 19)
d.show()
d.speak()

f = Fish('Yan', 1)
f.show()
f.speak()