# https://www.youtube.com/watch?v=Qs3BSFZnZSI
# Sets: unordered, mutable, no duplicates

print("{:=^52}".format(" Create new Set type "))
myset = {1, 2, 3, 4, 1, 2}
myset2 = set([1, 2, 3, 4, 5])
myset3 = set("Hello!")
myset4 = set()
myset5 = frozenset([1, 2, 3, 4, 5])

print(myset)
print(myset2)
print(myset3)
print(type(myset4))

myset4.add(4)
myset4.add(1)
myset4.add(2)
print(myset4)

myset4.remove(4)
print(myset4)

myset4.discard(2)
myset4.discard(5)
print(myset4)

myset4.add(3)
print(myset4.pop())
print(myset4)

print(myset5)

# for loop
print("{:=^52}".format(" for loop "))

for i in myset:
    print(i)

if 1 in myset:
    print("YES")
else:
    print("NO")


# Union set
print(f'{" Union set " :=^52}')
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

print(f'{" Intersection set " :=^52}')
i = odds.intersection(evens)
i2 = odds.intersection(primes)
i3 = evens.intersection(primes)
print(i)
print(i2)
print(i3)

# Different
print(f'{" Different " :=^52}')

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

diff2 = setB.difference(setA)
print(diff2)

print("{:=^52}".format(" symmetric_difference "))
diff3 = setA.symmetric_difference(setB)
print(diff3)

print("{:=^52}".format(" update "))
setA.update(setB)
print(setA)

print("{:=^52}".format(" intersection_update "))
setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3, 10, 11, 12}
setC.intersection_update(setD)
print(setC)

print("{:=^52}".format(" difference_update "))
setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3, 10, 11, 12}
setC.difference_update(setD)
print(setC)

print("{:=^52}".format(" symmetric_difference_update "))
setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3, 10, 11, 12}
setC.symmetric_difference_update(setD)
print(setC)

print("{:=^52}".format(" issubset "))
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
print(setC.issubset(setD))
print(setD.issubset(setC))

print("{:=^52}".format(" issuperset "))
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
print(setC.issuperset(setD))
print(setD.issuperset(setC))

print("{:=^52}".format(" isdisjoint "))
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
setE = {7, 8, 9}
print(setC.isdisjoint(setD))
print(setD.isdisjoint(setE))

# Clone a Set
print("{:=^52}".format(" Clone a Set "))
setF =  {1, 2, 3, 4, 5, 6}
setH = setF
setH.add(7)

print(setH)
print(setF)

print("{:=^52}".format(" Copy "))
setF =  {1, 2, 3, 4, 5, 6}
setH = setF.copy()
setH.add(7)

print(setH)
print(setF)

print("{:=^52}".format(" set new Set "))
setF =  {1, 2, 3, 4, 5, 6}
setH = set(setF)
setH.add(7)

print(setH)
print(setF)