# -*- coding: utf-8 -*-
"""Code to test breakpoints.

Test the following kinds of breakpoints within the code:
- Conditional breakpoint.
- Hit Breakpoint.
- Log point.
"""
from loguru import logger


def main() -> None:
    """Execute main function."""
    numbers = list(range(1, 21))
    squared_numbers = calculate_squares(numbers)
    logger.info("Squared Numbers:", squared_numbers)


def calculate_squares(numbers: list) -> list:
    """Find the squares of a list of numbers.

    :param numbers: List of numbers we want to square.
    """
    squared_numbers = []
    for number in numbers:
        squared = "I'm a Bug! 🐞" if number % 4 == 0 else number**2
        squared_numbers.append(squared)
    return squared_numbers


if __name__ == "__main__":
    main()
