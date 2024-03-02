# -*- coding: utf-8 -*-
"""Configuration file for pytest."""
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def df():
    return pd.DataFrame(
        {
            "Date": ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05"],
            "Open": [100, 101, 100, 103, 104],
            "High": [101, 102, 101, 104, 105],
            "Low": [99, 100, 99, 102, 103],
            "Close": [100.5, 101.5, 100.5, 103.5, 104.5],
            "Adj Close": [100, 101, 100, 103, 104],
            "Volume": [1000, 1100, 1200, 1300, 1400],
        }
    )


@pytest.fixture
def df_with_daily_returns(df):
    df["Daily Returns"] = [np.nan, 0.01, -0.01, 0.03, 0.01]
    return df


@pytest.fixture
def start_date():
    return "2020-01-02"


@pytest.fixture
def end_date():
    return "2020-01-04"


@pytest.fixture
def window():
    return 3


@pytest.fixture
def lag_days():
    return 3
