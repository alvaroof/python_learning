# -*- coding: utf-8 -*-
"""MODULE 5: Best practices.

TASK 1: This task is to practice the basic concepts learnt in the fifth module, found here:
  <link to the pylosophy book repo's chapter of Best Practices>

In this script you will find several snippets of code. Some of them are properly coded,
but others are not. This doesn't mean that they wouldn't work, but they can be
improved in several ways. Some code snippets are in other scripts, because they use specific imports.
"""

def example_1(num_1, num_2):
    """Given two numbers, return true if the first one is bigger than the second one.

    :param num_1: First number.
    :param num_2: Second number.
    """
    return num_1 > num_2


def example_2(num):
    """Convert a number from 1 to 5 into a vowel.

    :param num: Number to convert.
    """
    match num:
        case 1:
            return "a"
        case 2:
            return "e"
        case 3:
            return "i"
        case 4:
            return "o"
        case 5:
            return "u"
        case _:
            print("Sorry, invalid number.")
            return 0


def example_3():
    f = open("file.txt")
    try:
        f.read()
    finally:
        f.close()
