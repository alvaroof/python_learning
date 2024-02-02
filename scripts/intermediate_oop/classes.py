# -*- coding: utf-8 -*-
"""Class exercises."""
import math


class BankAccount:
    """Bank account including an account balance."""

    def __init__(self, balance=0):
        self._balance = balance
        self.transactions = []
        self.transactions.append(("OPEN", balance, balance))

    @property
    def balance(self):
        return self._balance

    def deposit(self, quantity):
        self._balance += quantity
        self.transactions.append(("DEPOSIT", quantity, self._balance))

    def withdraw(self, quantity):
        self._balance -= quantity
        self.transactions.append(("WITHDRAWAL", -quantity, self._balance))

    def transfer(self, other, quantity):
        other._balance += quantity
        self._balance -= quantity

    def __repr__(self):
        return f"BankAccount(balance={self._balance})"

    def __str__(self):
        return f"A Bank Account with balance={self._balance}"


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
