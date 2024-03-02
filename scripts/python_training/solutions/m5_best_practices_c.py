# -*- coding: utf-8 -*-
"""This code snippet is separated from the rest, but is still part of task 1."""

from nvs_tk import Extractor


class TestExtractor(Extractor):
    """Extractor used to retrieve data.

    :param repo: Repository used to retrieve data.
    :param param1: Parameter 1.
    :param param2: Parameter 2.
    """

    _QUERY_FILE = QUERIES_DIR / "file.sql"

    COLUMNS = frozenset(
        {
            "col_a",
            "col_b",
            "col_c",
            "col_d",
        }
    )

    def __init__(self, repo: SqlRepository, param1: None | int, param2: int) -> None:
        self._repo = repo
        self._param1 = param1
        self._param2 = param2

    def get(self) -> pd.DataFrame:
        try:
            return self._repo.get(
                self._QUERY_FILE,
                params=utils.filter_version_id(
                    ("param1", self._param1),
                    ("param2", self._param2),
                ),
            )

        except SqlRepository as exc:
            raise ExtractorError("Extractor was unable to retrieve data from DB.") from exc

    def validate(self, data: pd.DataFrame) -> None:
        val.validate_not_empty(data)
        val.validate_correct_columns(data, self.COLUMNS)
        val.validate_no_duplicates(data)

    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
        return data