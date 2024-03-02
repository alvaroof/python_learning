# -*- coding: utf-8 -*-
"""Test for ``_enhance_with_technical_indicators`` function."""
import pandas as pd
import pytest

from python_training.m2_external_libraries._preprocess import _enhance_with_technical_indicators


def test_enhance_with_technical_indicators(df_with_daily_returns, window):
    enhanced_df = _enhance_with_technical_indicators(df_with_daily_returns, window)
    expected_ma = df_with_daily_returns["Close"].rolling(window=window).mean().round(3)
    expected_volatility = (
        df_with_daily_returns["Daily Returns"].rolling(window=window).std().round(3)
    )

    assert f"MA_{window}" in enhanced_df.columns
    assert "Volatility" in enhanced_df.columns
    pd.testing.assert_series_equal(
        enhanced_df[f"MA_{window}"].round(3), expected_ma, check_names=False
    )
    pd.testing.assert_series_equal(
        enhanced_df["Volatility"].round(3), expected_volatility, check_names=False
    )


def test_enhance_with_technical_indicators_missing_columns(df_with_daily_returns, window):
    df_modified = df_with_daily_returns.drop(columns=["Close"])

    with pytest.raises(
        ValueError,
        match="DataFrame is missing required columns for technical indicator calculations",
    ):
        _enhance_with_technical_indicators(df_modified, window)


def test_enhance_with_technical_indicators_invalid_window(df_with_daily_returns):
    with pytest.raises(ValueError, match="'window' must be a positive integer."):
        _enhance_with_technical_indicators(df_with_daily_returns, window=-1)
