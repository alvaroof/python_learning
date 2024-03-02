# -*- coding: utf-8 -*-
"""Test for ``_add_lags`` function."""

import pandas as pd
import pytest

from python_training.m2_external_libraries._preprocess import _add_lags


def test_add_lags(df_with_daily_returns, lag_days):
    lagged_df = _add_lags(df_with_daily_returns, lag_days)

    for i in range(1, lag_days + 1):
        assert f"Close_lag_{i}" in lagged_df.columns

    for i in range(1, lag_days + 1):
        expected_lag = df_with_daily_returns["Close"].shift(i)
        pd.testing.assert_series_equal(lagged_df[f"Close_lag_{i}"], expected_lag, check_names=False)


def test_add_lags_missing_close_column(df_with_daily_returns):
    df_modified = df_with_daily_returns.drop(columns=["Close"])

    with pytest.raises(
        ValueError, match="DataFrame must contain a 'Close' column for lag feature calculations."
    ):
        _add_lags(df_modified, lag_days=5)


def test_add_lags_invalid_lag_days(df_with_daily_returns):
    with pytest.raises(ValueError, match="'lag_days' must be a positive integer."):
        _add_lags(df_with_daily_returns, lag_days=-1)
