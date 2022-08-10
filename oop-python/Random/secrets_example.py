import secrets

a = secrets.randbelow(10)
print(a)

b = secrets.randbits(4)
print(b)

mylist = list("ABCDEFGH")
print(f'{"secrets.choice" :=^52}')
c = secrets.choice(mylist)
print(c)