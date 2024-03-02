# -*- coding: utf-8 -*-
"""Dunder exercises."""

class ReverseView:
    """Lazily operate on a sequence in reverse."""
    def __init__(self, sequence):
        self._sequence = sequence

    def __getitem__(self, index): # If it were a dictionary we would use 'key' instead
        return self._sequence[-index-1]
    
    def __str__(self):
        return f'{self._sequence[::-1]}'
    
    def __len__(self):
        return len(self._sequence)
    
class NotImplemented(BaseException):
    pass

class Comparator:
    """Object that is equal to a very small range of numbers."""


class RomanNumeral:
    """Class for treating Roman Numerals like numbers."""


class Timer:
    """Utility for timing the execution of code."""


class FancyDict:
    """Dictioray-like class supporting attribute lookups."""


class reloopable:
    """Iterable which resets a file each time it's looped over."""
