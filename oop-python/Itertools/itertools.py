# https://www.youtube.com/watch?v=3ecISAkioPc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=7
# itertools: product, permutations, combinations, accumulate, groupby

from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
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