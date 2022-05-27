mydict = {"name": "Mint", "age": 9, "city": "Da Nang"}
mydict2 = dict()
mydict3 = dict(name="May", age=3)

print(mydict)
print(mydict2)
print(mydict3)
print(mydict3["age"])

mydict["email"] = "test@gmail.com"
print(mydict)
del mydict["city"]
print(mydict)
mydict.pop("age")
print(mydict)
mydict.popitem()
print(mydict)


if "name" in mydict3:
    print(mydict3["name"])

try:
    print(mydict3["city"])
except:
    print("Error")


# For loop
for key in mydict3.keys():
    print(key)

for value in mydict3.values():
    print(value)

for key, value in mydict3.items():
    print(key, value)


# Copy dictionary
mydict = {"name": "Mint", "age": 9, "city": "Da Nang"}
mydict_cpy = mydict
mydict_cpy["email"] = "kent@gmail.com"
print(mydict)
print(mydict_cpy)

mydict_cpy1 = mydict.copy()
mydict_cpy1["email"] = "mint@gmail.com"
print(mydict)
print(mydict_cpy1)

mydict_cpy2 = dict(mydict)
mydict_cpy2["email"] = "may@gmail.com"
print(mydict)
print(mydict_cpy2)


# Update dictionary
mydict = {"name": "Mint", "age": 9, "city": "Da Nang"}
mydict2 = dict(name="May", age=3)
mydict.update(mydict2)
print(mydict)

# Tuple and Dictionary
numDic = {3: 9, 6: 29, 9: 19}
print(numDic[3])

myTuple = (6, 7)
numDic2 = {myTuple: 4}
print(numDic2)
