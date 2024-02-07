from functions import call
from functions import call_later
from functions import exclude
from functions import call_logger

print(call(int))
# 0

print(call(int, "5"))
# 5

print(call(len, "hello"))
# 5

print(list(call(zip, [1, 2], [3, 4])))
# [(1, 3), (2, 4)]

names = []
append_name = call_later(names.append, "Trey")
append_name()
print(names)
# ['Trey']

append_name()
print(names)
# ['Trey', 'Trey']

call_zip = call_later(zip, [1, 2], [3, 4])

print(list(call_zip()))
# [(1, 3), (2, 4)]


print(exclude(bool, [False, True, False]))
# [False, False]

print(exclude(lambda x: len(x) > 3, ["red", "blue", "green"]))
# ['red']


def greet(): print("Hello")

greet_now = call_logger(greet)

print(greet_now())
# Function started
# Hello
# Function returned