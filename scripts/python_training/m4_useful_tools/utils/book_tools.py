# -*- coding: utf-8 -*-
"""Utils for Module 4: Useful tools."""
import pandas as pd


def insert_book_info_to_frame(frame: pd.DataFrame, book_info: dict) -> pd.DataFrame:
    """Insert book information into a dataframe.

    :param frame: Data frame to insert book info.
    :param book_info: Dictionary with book information.
    """
    return frame.append(book_info, ignore_index=True)
