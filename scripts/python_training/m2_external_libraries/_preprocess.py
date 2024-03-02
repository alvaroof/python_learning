# -*- coding: utf-8 -*-
"""Functions for testing exercises.

This module is designed to perform various manipulations and analyses on stock price data.
The data is expected to be in a pandas DataFrame with the following columns:

- Date: The date of the stock data, in 'YYYY-MM-DD' format.
- Open: The opening price of the stock for the day.
- High: The highest price of the stock for the day.
- Low: The lowest price of the stock for the day.
- Close: The closing price of the stock for the day.
- Adj Close: The adjusted closing price of the stock for the day (adjusted for splits and dividends).
- Volume: The number of shares traded during the day.

DataFrame example:

    Date        Open    High    Low     Close   Adj Close   Volume
    2020-01-01  100     110     95      105     105         10000
    2020-01-02  105     115     100     110     110         15000
    ...

These functions are designed to prepare stock price data for analysis and modeling.
They enable users to clean and transform the data, extract meaningful features, and ensure the data is
in a suitable format for various analytical tasks.
"""

from typing import Union

import pandas as pd

from ._utils import db_connector


def preprocess(
    start_date: Union[str, pd.Timestamp],
    end_date: Union[str, pd.Timestamp],
    window: int = 20,
    lag_days: int = 5,
):
    """Applies a series of preprocessing steps to stock price data.

    This function integrates several preprocessing steps: initial data preparation and normalization,
    technical indicator enhancement, and the addition of lag features. It's designed to prepare stock
    price data for further analysis or modeling.

    :param df: The input DataFrame containing stock price data.
    :param start_date: The start date for filtering the data, in 'YYYY-MM-DD' format.
    :param end_date: The end date for filtering the data, in 'YYYY-MM-DD' format.
    :param window: The window size for calculating moving averages and volatility. Defaults to 20.
    :param lag_days: The number of days to create lag features for. Defaults to 5.

    :returns: The processed DataFrame, ready for analysis or modeling, with normalized dates,
      filtered by the specified date range, enhanced with technical indicators, and augmented with lag features.
    """
    df = db_connector().read_from_db()

    if df is None:
        return None

    return (
        df.pipe(_prepare_and_normalize_data, start_date=start_date, end_date=end_date)
        .pipe(_enhance_with_technical_indicators, window=window)
        .pipe(_add_lags, lag_days=lag_days)
    )


def _prepare_and_normalize_data(
    df: pd.DataFrame, start_date: Union[str, pd.Timestamp], end_date: Union[str, pd.Timestamp]
):
    """Prepares and normalizes stock price data for analysis.

    This function standardizes the date format, filters the dataset based on a specified date range,
    generates additional date-related features, calculates daily returns, and ensures that the dataset
    has no missing dates within the specified range by forward filling missing values. This comprehensive
    preprocessing step is crucial for subsequent financial analysis and modeling tasks.

    :param df: DataFrame with stock price data, expecting columns 'Date' and 'Adj Close'.
    :param start_date: String representing the start date in 'YYYY-MM-DD' format.
    :param end_date: String representing the end date in 'YYYY-MM-DD' format.

    :return: A DataFrame that has been processed to include only the specified date range,
      with added 'Month' and 'DayOfWeek' features, daily returns calculated, and missing dates
      forward-filled. The DataFrame is indexed by the 'Date' column.

    :raises: ValueError: If the input DataFrame does not contain a 'Date' column or if the 'Date' column
      cannot be converted to datetime format. Also raised if the specified start_date or end_date
      are not in the correct format.
    """
    if "Date" not in df.columns:
        raise ValueError("DataFrame must contain a 'Date' column.")
    try:
        df["Date"] = pd.to_datetime(df["Date"])
    except ValueError as e:
        raise ValueError(
            "Error converting 'Date' column to datetime. Ensure the dates are in a correct format."
        ) from e

    # Filter Date Range
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # Generate Date Features
    df["Month"] = df["Date"].dt.month
    df["DayOfWeek"] = df["Date"].dt.dayofweek

    # Calculate Daily Returns
    df["Daily Returns"] = df["Adj Close"].pct_change()

    # Fill Missing Dates (forward fill for simplicity)
    df = df.set_index("Date").resample("D").ffill()

    return df


def _enhance_with_technical_indicators(df: pd.DataFrame, window: int = 20):
    """Enriches a DataFrame with key technical indicators to aid in financial analysis.

    This function calculates and appends several technical indicators to the input DataFrame,
    specifically a moving average and volatility measure. These indicators are widely used in
    stock market analysis to understand price trends and market volatility over a specified
    window of time. Additionally, the function ensures that the necessary prerequisites for
    calculation are met, such as the presence of required columns.

    :param df: DataFrame after initial preprocessing, with 'Date' and 'Close' columns.
    :param window: Integer representing the window size for the moving average.

    :return: The original DataFrame augmented with two new columns:
        - 'MA_{window}': The moving average of the 'Close' prices over the specified window.
        - 'Volatility': The rolling standard deviation of 'Daily Returns', representing price
          volatility over the same window.

    :raises:
        - ValueError: If the input DataFrame lacks the required 'Close' or 'Daily Returns' columns,
        or if the 'window' parameter is not a positive integer.
        - RuntimeError: If an unexpected error occurs during the calculation of technical indicators.
    """
    # Validate required columns
    required_columns = ["Close", "Daily Returns"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(
            f"DataFrame is missing required columns for technical indicator calculations: {', '.join(missing_columns)}"
        )

    # Validate window size
    if not isinstance(window, int) or window <= 0:
        raise ValueError("'window' must be a positive integer.")

    try:
        # Add Moving Average
        df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
        # Calculate Volatility (rolling standard deviation of daily returns)
        df["Volatility"] = df["Daily Returns"].rolling(window=window).std()
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating technical indicators: {e}")

    return df


def _add_lags(df: pd.DataFrame, lag_days: int = 5):
    """Enhances a DataFrame by adding lagged features for the 'Close' price column.

    This function creates new columns in the DataFrame, each representing the 'Close' price
    shifted by a number of days specified by the 'lag_days' parameter. These lagged features
    are useful for time series analysis and forecasting models, as they allow the model to
    consider historical price movements.

    :param df: DataFrame with stock price data.
    :param lag_days: Number of days to lag features by.

    :return: A DataFrame identical to the input but with additional columns for each
      lagged feature. The names of these new columns follow the pattern 'Close_lag_X', where
      X is the number of days the 'Close' price is lagged by.

    :raises: ValueError: If the input DataFrame does not contain a 'Close' column or if the 'lag_days'
      parameter is not a positive integer.
    """
    # Validate 'Close' column presence
    if "Close" not in df.columns:
        raise ValueError("DataFrame must contain a 'Close' column for lag feature calculations.")

    # Validate lag_days parameter
    if not isinstance(lag_days, int) or lag_days <= 0:
        raise ValueError("'lag_days' must be a positive integer.")

    try:
        # Create Lag Features for 'Close' Price
        for i in range(1, lag_days + 1):
            df[f"Close_lag_{i}"] = df["Close"].shift(i)
    except Exception as e:
        # Catching a broad exception to handle unexpected errors during lag feature creation
        raise RuntimeError(f"An error occurred while adding lag features: {e}")

    return df
