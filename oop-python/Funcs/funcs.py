def foo(a, b, *args, **kwargs):
    print(a, b)

    print(f'{" *args " :=^52}')
    for arg in args:
        print(arg)

    print(f'{" **kwargs " :=^52}')
    for key in kwargs:
        print(key, kwargs[key])


print(f'{" Func 1 " :=^52}')
foo(1, 2, 3, 4, 5, six=6, seven=7)
print(f'{" Func 2 " :=^52}')
foo(1, 2, 3, 4, 5, 7)

print(f'{" Func 3 " :=^52}')


def bar(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]
bar(*my_list)

my_tuple = (1, 2, 3)
bar(*my_tuple)

my_dict = {"a": 1, "b": 2, "c": 3}
bar(**my_dict)

print(f'{" Calculation " :=^52}')
zeros = "AB" * 10
print(zeros)

# numbers = [1, 2, 3, 4, 5, 6, 7]
numbers = (1, 2, 3, 4, 5, 6, 7)
# *beginning, last = numbers
# beginning, *last = numbers
beginning, *middle, prelast ,last = numbers
print(beginning)
print(middle)
print(prelast)
print(last)
