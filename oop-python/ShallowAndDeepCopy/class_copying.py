import copy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 29)
p3 = Person('Joe', 25)
p2 = copy.copy(p1)
p2.age = 33
print(f'{" Copy " :=^52}')
print(p1.age)
print(p2.age)

company = Company(p1,p3)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 58
print(f'{" Deep copy " :=^52}')
print(company.boss.age)
print(company_clone.boss.age)
