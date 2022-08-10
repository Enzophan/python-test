import sys

mygenerator = (i for i in range(10000) if i % 2 == 0)
# for i in mygenerator:
#     print(i)
# print(list(mygenerator))
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10000) if i % 2 == 0]
# print(mylist)
print(sys.getsizeof(mylist))
