# -*- coding: utf-8 -*-
"""MODULE 3: Internal Libraries.

TASK 1: This task is to practice the basic concepts learnt in the third module, found here:
  <link to the pylosophy book repo's chapter of OOP and Imperative Programming>

Create a python class that inherits from Extractor (can be found in the nvs-tk) that:
    * Gets information from a database.
    * Validates that the data is not empty.
    * Validates that the data has the correct columns (Found in the sample QUERY).
    * Validates that there are no duplicates.
    * Doesn't manipulate the data, just returns it as is.

You can find the query in this folder.
Assume that the SQL Repository has already been created and
you receive it in the Extractor as a parameter.
"""
import pandas as pd
from nvs_sql import SqlRepository
from nvs_tk import Extractor


class TaskExtractor(Extractor):
    """Extractor designed for the task of module 3."""

    def __init__(self, repo: SqlRepository) -> None:
        """Your code here."""

    def get(self) -> pd.DataFrame:
        """Your code here."""

    def validate(self, data: pd.DataFrame) -> None:
        """Your code here."""

    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """Your code here."""
