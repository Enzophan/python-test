# lambda arguments: expression

from functools import reduce


add10 = lambda x: x + 10
print(add10(5))


def add10_func(x):
    return x + 10


mult = lambda x, y: x * y
print(mult(5, 2))


print(f'{"List" :=^52}')
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
points2D_sorted_lambda = sorted(points2D, key=lambda x: x[1])
points2D_sorted_lambda_sum = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D)
print(points2D_sorted)
print(points2D_sorted_lambda)
print(points2D_sorted_lambda_sum)


print(f'{"map(func, seq)" :=^52}')
a = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2, a))
c = [x * 2 for x in a]
print(a)
print(b)
print(c)

print(f'{"filter(func, seq)" :=^52}')
d = list(filter(lambda x: x % 2 == 0, a))
print(d)
e = [x for x in a if x % 2 == 0]
print(e)

print(f'{"reduce(func, seq)" :=^52}')
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
