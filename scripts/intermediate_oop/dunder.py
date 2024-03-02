# -*- coding: utf-8 -*-
"""Dunder exercises."""


class ReverseView:
    """Lazily operate on a sequence in reverse."""
    def __init__(self, list):
        self.original_list = list
        self.reversed_list = list[::-1]
        self.current = self.reversed_list[0]
        self.high = self.reversed_list[len(self.reversed_list)-1]
        
    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration

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
