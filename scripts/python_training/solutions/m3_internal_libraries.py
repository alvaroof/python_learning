# -*- coding: utf-8 -*-
"""Solutions for the task of module 3: Internal libraries."""
import pandas as pd
from nvs_sql import SqlRepository, SqlRepositoryError
from nvs_tk import Extractor
from nvs_tk import validation as val
from nvs_tk.errors import ExtractorError

from python_training import M3_PATH


class TaskExtractor(Extractor):
    """Extractor designed for the task of module 3."""

    _QUERY_FILE = M3_PATH / "query.sql"

    COLUMNS = frozenset(
        {
            "drug_id",
            "ims_id",
            "country",
            "molecule",
        }
    )

    def __init__(self, repo: SqlRepository) -> None:
        self._repo = repo

    def get(self) -> pd.DataFrame:
        """Get the data."""
        try:
            return self._repo.get(
                self._QUERY_FILE,
            )

        except SqlRepositoryError as exc:
            raise ExtractorError("Extractor was unable to retrieve data from DB.") from exc

    def validate(self, data: pd.DataFrame) -> None:
        """Validate the data."""
        val.validate_not_empty(data)
        val.validate_correct_columns(data, self.COLUMNS)
        val.validate_no_duplicates(data)

    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean the data."""
        return data
