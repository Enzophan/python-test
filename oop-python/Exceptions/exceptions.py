# Errors and Exceptions

try:
    a = 5 / 1
    b = a + 4

except ZeroDivisionError as e:
    print("Step 1: ", e)
except TypeError as e:
    print("Step 2: ", e)
except Exception as e:
    print("Step 3: ", e)
else:
    print("Everything is fine")
finally:
    print("clearning up...")


print(f'{"ValueTooHighError" :=^52}')


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("value too small", x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
