# -*- coding: utf-8 -*-
"""Solutions for the task of module 5: Best practices."""

def example_1_corrected(num_1, num_2):
    """Given two numbers, return true if the first one is bigger than the second one.

    :param num_1: First number.
    :param num_2: Second number.
    """
    return num_1 > num_2


def example_2_corrected(num):
    """Convert a number from 1 to 5 into a vowel.

    :param num: Number to convert.
    """
    mapper = {
        1: "a",
        2: "e",
        3: "i",
        4: "o",
        5: "u"
    }

    try:
        return mapper[num]
    except KeyError:
        print("Sorry, invalid number")
        return 0


def example_3_corrected():
    with open("file.txt") as f:
        f.read()
