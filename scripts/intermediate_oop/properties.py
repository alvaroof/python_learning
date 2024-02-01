# -*- coding: utf-8 -*-
"""Property exercises."""
import math


class Circle:
    """Circle with radius, area, etc."""

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def area(self):
        area = math.pi * self.radius**2
        return area

    @property
    def diameter(self):
        diameter = self.radius * 2
        return diameter

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


class Vector:
    """Class representing a 3 dimensional vector."""


class Person:
    """Person with first and last name."""
