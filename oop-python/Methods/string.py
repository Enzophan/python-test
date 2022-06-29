my_string = "   I'm a programmer "

print(my_string)

print(my_string[1:5])
print(my_string[:])
print(my_string[::2])
print(my_string[::-1])

my_string = my_string.strip()
print(my_string)
print(my_string.upper())
print(my_string.lower())

print(my_string.startswith("I'm"))
print(my_string.endswith("I'm"))
print(my_string.find("mm"))
print(my_string.count("a"))

my_string = my_string.replace("programmer", "doctor")
print(my_string)
my_list = my_string.split()
print(my_list)
new_string = " ".join(my_list)
print(new_string)

print(f'{" Bad " :=^52}')
from timeit import default_timer as timer
from tracemalloc import stop

my_list = ["a"] * 6000

start = timer()
my_string_two = ""
for i in my_list:
    my_string_two += i
stop = timer()
print(stop - start)
# print(my_string_two)

print(f'{" Good " :=^52}')
startTwo = timer()
my_string_two = "".join(my_list)
stopTwo = timer()
print(stopTwo - startTwo)
# print(my_string_two)

print(f'{" string concatenation " :=^52}')
var = ("Kent",)
my_string_three = "the variable is %s" % var
print(my_string_three)

print(f'{" number interger concatenation " :=^52}')
num = 10.12345899
my_string_four = "the variable is %d" % num
print(my_string_four)

print(f'{" number floar concatenation " :=^52}')
my_string_five = "the variable is %.2f" % num
print(my_string_five)
print("the variable is %f" % num)

print(f'{"concatenation by .format()" :=^52}')
print("the variable is {}".format(num))
print("the variable is {:.2f}".format(num))
num2 = 19
print("the variable is {:.2f} and {}".format(num, num2))

print(f'{"concatenation by f-String" :=^52}')
print(f"the variable is {num * 2} and {num2}")
