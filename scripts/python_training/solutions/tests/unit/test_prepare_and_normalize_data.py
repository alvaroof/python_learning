# -*- coding: utf-8 -*-
"""Test for ``_prepare_and_normalize_data`` function."""
import numpy as np
import pandas as pd
import pytest

from python_training.m2_external_libraries._preprocess import _prepare_and_normalize_data


def test_prepare_and_normalize_data(df, start_date, end_date):
    processed_df = _prepare_and_normalize_data(df, start_date, end_date)
    returns = processed_df["Daily Returns"].round(3).to_list()

    assert processed_df.index[0] == pd.to_datetime(start_date)
    assert processed_df.index[-1] == pd.to_datetime(end_date)

    assert "Month" in processed_df.columns
    assert "DayOfWeek" in processed_df.columns
    assert "Daily Returns" in processed_df.columns
    assert np.isnan(returns[0])
    assert returns[1:] == [-0.01, 0.03]


def test_prepare_and_normalize_data_missing_date_column(df, start_date, end_date):
    df = df.drop(columns=["Date"])

    with pytest.raises(ValueError, match="DataFrame must contain a 'Date' column."):
        _prepare_and_normalize_data(df, start_date, end_date)


def test_prepare_and_normalize_data_invalid_date_format(df, start_date, end_date):
    df["Date"] = ["not a date", "neither this", "2020-01-03", "2020-01-04", "2020-01-05"]

    with pytest.raises(ValueError, match="Error converting 'Date' column to datetime."):
        _prepare_and_normalize_data(df, start_date, end_date)
