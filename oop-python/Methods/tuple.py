# https://www.youtube.com/watch?v=Kes8YRV73Io

myTuple = ("max", 12, True, "Test")
myTuple2 = "max", 12, True, "Test"
myTuple3 = tuple(["max", 12, True, "Test"])

print(myTuple)
print(myTuple2)
print(type(myTuple2))
print(myTuple3)
print(myTuple3[0])
print(myTuple3[-2])

# For loop
print("======For loop======")
for i in myTuple:
    print(i)

if "Test" in myTuple:
    print("Yes")
else:
    print("No")

myTuple4 = ("a", "b", "c", "a", "x", "y")
print(len(myTuple4))
print(myTuple4.count("a"))
print(myTuple4.index("a"))

# Convert tuple to list
myList = list(myTuple4)
print(myTuple4)
print(myList)

# copy tuple
a = (1, 6, 7, 8, 9, 3, 2, 4, 10)
b = a[2:5]

print(a)
print(b)

# revert
print(a[::-1])


student = ("Mint", 18, True)
name, age, gen = student
print(name)
print(age)
print(gen)

i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)

# Check memory storage between list and tuple
import sys
checkTuple = ("Mint", 18, True, 12.99)
checkList = ["Mint", 18, True, 12.99]
print(sys.getsizeof(checkTuple), 'bytes')
print(sys.getsizeof(checkList), 'bytes')

# Check time when create between list and tuple
import timeit
print(timeit.timeit(stmt="(1,2,3,4,5,6)", number=1000000))
print(timeit.timeit(stmt="[1,2,3,4,5,6]", number=1000000))