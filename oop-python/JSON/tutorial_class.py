import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 28)


# Way 1
print(f'{"Way 1" :=^52}')
def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJson = json.dumps(user, default=encode_user)
print(userJson)

# Way 2
print(f'{"Way 2" :=^52}')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJson = json.dumps(user, cls=UserEncoder)
print(userJson)
print(type(userJson))

# Way 3
print(f'{"Way 3" :=^52}')
print(UserEncoder().encode(user))

user = json.loads(userJson)
print(user)
print(type(user))
print(user['name'])

print(f'{"Get key in dict" :=^52}')
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict

user = json.loads(userJson, object_hook=decode_user)
print(user.name)
