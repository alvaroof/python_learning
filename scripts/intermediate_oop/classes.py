# -*- coding: utf-8 -*-
"""Class exercises."""


class BankAccount:
    """Bank account including an account balance."""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, quantity):
        self.balance += quantity

    def withdraw(self, quantity):
        self.balance -= quantity

    def transfer(self, BankAccount, quantity):
        BankAccount.balance += quantity
        self.balance -= quantity

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"

    def __str__(self):
        return f"A Bank Account with balance={self.balance})"


class SuperMap:
    """Data structure for quickly finding objects based on their attributes."""


class MinHeap:
    """Heap-like data structure."""


class Flavor:
    """Flavor of ice cream."""


class Size:
    """Ice cream size."""


class IceCream:
    """Ice cream to be ordered in our ice cream shop."""


class Month:
    """Class representing an entire month."""


class MonthDelta:
    """Class representing the difference between months."""


class Row:
    """Row class that stores all given arguments as attributes."""
