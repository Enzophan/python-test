# https://www.youtube.com/watch?v=FXUUSfJO_J4&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=14

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwds) :
        self.num_calls +=1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwds)

@CountCalls
def say_hello(name):
    print(f'Hello {name}')


say_hello('May')
say_hello('Mint')