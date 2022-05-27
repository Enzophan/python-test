# https://www.youtube.com/watch?v=QLTdOEn79Rc

mylist = ["banana", "cherry", "apple"]
mylist2 = list()
mylist3 = [12, True, "test", 12.99]


print(mylist)
print(mylist2)
print(mylist3)

mylist.append("lemon")
print(mylist)
mylist.insert(2, "strawberry")
print(mylist)
mylist.pop()
print(mylist)
mylist.remove("cherry")
print(mylist)
mylist.reverse()
print(mylist)

# Sort
mylist2 = [12, 3, 4, 1, 0, 29]
print(mylist2)
mylist2.sort()
print(mylist2)
mylist2.insert(3, 222)
newList = sorted(mylist2)
print(mylist2)
print(newList)

# Create array
mylist4 = [0] * 5
print(mylist4)
mergeList = mylist4 + mylist2
print(mergeList)
print(mergeList[5:8])
print(mergeList[:-1])
print(mergeList[::-1])


# Clone list
list_cpy = mylist
list_cpy.append("watermelon")
print(mylist)
print(list_cpy)

list_cpy1 = mylist.copy()
list_cpy1.append("melon")
print(mylist)
print(list_cpy1)

list_cpy2 = list(mylist)
list_cpy2.append("peach")
print(mylist)
print(list_cpy2)

list_cpy3 = mylist[:]
list_cpy3.append("Orange")
print(mylist)
print(list_cpy3)

# calculation in list
listNum = [1, 2, 3, 4, 5, 6]
b = [i * i for i in listNum]
print(listNum)
print(b)