# -*- coding: utf-8 -*-
from unittest.mock import patch

import pandas as pd
import pytest

from python_training.m2_external_libraries import preprocess


@pytest.fixture
def stocks_parquet():
    return pd.read_parquet("tests/assets/stocks_data.parquet")


@patch("python_training.m2_external_libraries._utils.db_connector.read_from_db")
def test_preprocess(mock_read_from_db, start_date, end_date, window, lag_days):
    mock_read_from_db.return_value = pd.read_parquet("tests/assets/stocks_data.parquet")
    processed_df = preprocess(start_date, end_date, window, lag_days)

    assert not processed_df.empty
    assert f"MA_{window}" in processed_df.columns
    assert "Volatility" in processed_df.columns
    for i in range(1, lag_days + 1):
        assert f"Close_lag_{i}" in processed_df.columns

    assert processed_df.index.min() >= pd.to_datetime(start_date)
    assert processed_df.index.max() <= pd.to_datetime(end_date)
