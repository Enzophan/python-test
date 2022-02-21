# Overriding Methods
# https://youtu.be/39m3rstTN8w
# Doc: https://www.codingem.com/python-__add__-method/#:~:text=The%20__add__()%20method%20in%20Python%20is%20a%20special%20method,__add__(o2).&text=This%20error%20says%20Weight%20objects%20do%20not%20support%20addition%20with%20%2B%20operator.

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coords = (self.x , self.y)

    def move (self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __len__(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self,p):
        return self.__len__() > p.__len__()

    def __ge__(self,p):
        return self.__len__() >= p.__len__()

    def __lt__(self,p):
        return self.__len__() < p.__len__()

    def __le__(self,p):
        return self.__len__() <= p.__len__()

    def __eq__(self,p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p5, p6, p7)

print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)