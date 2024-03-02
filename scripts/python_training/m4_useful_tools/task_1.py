# -*- coding: utf-8 -*-
"""Task 1 of Module 4: Useful tools."""
from datetime import datetime

import pandas as pd
from loguru import logger

from python_training.m4_useful_tools.utils.book_tools import insert_book_info_to_frame


def main() -> None:
    """Get info from book."""
    programming_book = Book("Python Programming", "Jane Doe", 300, 2015)
    logger.info(programming_book.book_info())

    conelly_book = Book("Black Ice", "Michael Conelly", 400, 209)
    library = pd.DataFrame(columns=["title", "author", "years_since_publication"])
    library = insert_book_info_to_frame(library, conelly_book.book_info())
    logger.info(library)


class Book:
    """Class Book."""

    def __init__(self, title: str, author: str, pages: int, year_of_publication: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year_of_publication = year_of_publication

    def book_info(self) -> dict:
        """Extract the year_since_publication into a method using refactoring."""
        current_year = datetime.now().year
        years_since_publication = current_year - self.year_of_publication
        return {
            "title": self.title,
            "author": self.author,
            "years_since_publication": years_since_publication,
        }


if __name__ == "__main__":
    main()
