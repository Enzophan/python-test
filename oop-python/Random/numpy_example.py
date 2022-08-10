import numpy as np

"""https://numpy.org/install/"""

print(f'{"np.random" :=^52}')

a = np.random.rand(3)
b = np.random.rand(3, 3)
c = np.random.randint(0, 10, 3)
d = np.random.randint(0, 10, (3, 4))

print(a)
print(b)
print(c)
print(d)

print(f'{"np.random.seed" :=^52}')
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

print(f'{"np.array" :=^52}')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

