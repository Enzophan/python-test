import copy

print(f'{" Copy " :=^52}')
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
# cpy = org.copy()
# cpy = list(org)
# cpy = org[:]
cpy[0] = -10

print(org)
print(cpy)

print(f'{" Deep copy " :=^52}')
org_two = [[1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy_two = copy.deepcopy(org_two)
cpy_two[0][1] = -10

print(org_two)
print(cpy_two)