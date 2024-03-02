from functions import call
from functions import call_later
from functions import exclude
from functions import call_logger
from functions import call_again
from functions import only_once


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

greet_now()
# Function started
# Hello
# Function returned

names = []
response, names_as_str = call_again(str, names)
print(response)
# '[]'
names.append("Diane")
print(names_as_str())
# "['Diane']"


def do_something(x, y):
    print(f"doing something with {x} and {y}")
    return x * 2 + y ** 2
do_something_once = only_once(do_something)
print(do_something_once(1, 2))
# doing something with 1 and 2
# 6

try:
    do_something_once(1, 2)
except ValueError as e:
    print(e)