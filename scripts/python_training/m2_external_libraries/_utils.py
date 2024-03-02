# -*- coding: utf-8 -*-
from loguru import logger


class db_connector:
    def __init__(self) -> None:
        pass

    def read_from_db(self):
        """This function is a placeholder for database reading functionality. It's not implemented
        yet and is intended to be mocked during testing to return a DataFrame with stock price data.

        :returns: None. Placeholder return value. When mocked, this should return a pd.DataFrame.
        """
        logger.warning(
            "This function is not implemented yet. For testing purposes, try mocking the read from db with data from the assets folder."
        )
