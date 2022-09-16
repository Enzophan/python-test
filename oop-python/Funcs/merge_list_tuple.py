my_tuple = (1, 2, 3, 4)
my_list = [5, 6, 7]
my_set = {8, 9, 10}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)


dict_a = {"a": 1, "b": 2, 'e': 7}
dict_b = {"c": 3, "d": 4, 'e': 9}
my_dict = {**dict_a, **dict_b}
print(my_dict)
