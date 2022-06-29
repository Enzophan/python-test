from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

print(f'{"Counter" :=^52}')
a = "aaaaabbbcccddd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(2))
print(my_counter.most_common(2)[0][1])
print(list(my_counter.elements()))

print(f'{"namedtuple" :=^52}')
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

print(f'{"OrderedDict" :=^52}')
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['b'] = 2
print(ordered_dict)
print(ordered_dict['d'])

print(f'{"defaultdict" :=^52}')
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['b'])
print(d['c'])

print(f'{"deque" :=^52}')
c = deque()
c.append(1)
c.append(2)
c.appendleft(3)
print(c)
c.pop()
print(c)
c.extend([4,5,6,9])
print(c)
c.rotate(-1)
print(c)
c.clear()
print(c)