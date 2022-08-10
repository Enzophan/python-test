# https://www.youtube.com/watch?v=FXUUSfJO_J4&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=14
from curses import wrapper

def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper

# Way 1
# def print_name():
#     print('TEST')
# print_name = start_end_decorator(print_name)

# Way 2
@start_end_decorator
def print_name():
    print('TEST')


print_name()