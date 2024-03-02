# -*- coding: utf-8 -*-
"""This code snippet is separated from the rest, but is still part of task 1."""

from typing import Union


class NumberContainer:
    """Class NumberContainer."""

    def __init__(self, value: Union[int, float]) -> None:
        self.value = value

    def display_value(self):
        """Display the value of the number."""
        print(f"Current value: {self.value}")
