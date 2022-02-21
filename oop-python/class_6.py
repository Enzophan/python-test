# Static Methods and Class Methods

class Dog:
    dogs = []
    
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """bark n times"""
        for _ in range(n):
            print("bark")


tim = Dog("Tim")
joe = Dog("Joe")

print(Dog.num_dogs())
print(Dog.bark(5))