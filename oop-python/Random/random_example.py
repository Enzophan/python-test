import random

a = random.randint(1, 10)
print(a)
b = random.normalvariate(0, 1)
print(b)

mylist = list("ABCDEFGH")
print(f'{"random.choice" :=^52}')
c = random.choice(mylist)
print(c)
print(f'{"random.sample" :=^52}')
print(random.sample(mylist, 3))
print(f'{"random.choices" :=^52}')
print(random.choices(mylist, k=3))

print(f'{"random.shuffle" :=^52}')
random.shuffle(mylist)
print(mylist)

print(f'{"random.seed" :=^52}')
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))