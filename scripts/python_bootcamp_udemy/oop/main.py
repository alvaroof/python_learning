# -*- coding: utf-8 -*-
"""
Note: you may need to ``apt install python3-tk``

How to implement OOP in python.

First we need to know how to model a class. Think about what it ``has`` and what it ``does``. These will be its attributes and its methods.
An object is just a way of combining some piece of data and some functionality (this is the *encapsulation* property). The properties are
Abstraction, Encapsulation, Inheritance and Polymorphism.

Many real objects and agents can be modelled using this framework. For example, a waiter in a restaurant can be modelled having as attributes whether
is carrying a plate or not, and also which tables is waiting. As methods, we could have something like take_order() and carry_order().

``Class`` is the blueprint. The different copies of this blueprint are called ``instances``.
"""

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

table = ColorTable(theme=Themes.OCEAN)

print(table)
# table = PrettyTable()

table.header = False
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charizard"])
table.add_column("Id", [25, 35, 100])
table.add_column("Type", ["Electric", "Water", "Fire, Flying"])

print(table)
print(table.border)
print(table.header)
