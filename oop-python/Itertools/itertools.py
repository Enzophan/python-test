# https://www.youtube.com/watch?v=3ecISAkioPc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=7
# itertools: product, permutations, combinations, accumulate, groupby

from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
    count,
    cycle,
    repeat,
)

a = [1, 2]
b = [3, 4]

print(f'{"product" :=^52}')
prod = product(a, b)
prod_2 = product(a, b, repeat=2)
print(list(prod))
print(list(prod_2))

print(f'{"permutations" :=^52}')
a = [1, 2, 5]
perm = permutations(a)
perm_2 = permutations(a, 2)
print(list(perm))
print(list(perm_2))

print(f'{"combinations" :=^52}')
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

print(f'{"accumulate" :=^52}')
a = [1, 2, 5, 3, 4]
print(a)
import operator

accu = accumulate(a)
print(list(accu))

accu_mul = accumulate(a, func=operator.mul)
print(list(accu_mul))

accu_max = accumulate(a, func=max)
print(list(accu_max))

print(f'{"groupby" :=^52}')


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

group_obj_two = groupby(a, key=lambda x: x < 3)
for key, value in group_obj_two:
    print(key, list(value))

persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]

group_obj_per = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj_per:
    print(key, list(value))

print(f'{"count, cycle, repeat" :=^52}')

for i in count(10):
    print(i)
    if i == 15:
        break

c = [1, 2, 3]
# for i in cycle(c):
#     print(i)
    

# for i in repeat(1):
#     print(i)
