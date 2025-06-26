import pandas as pd
from pandas.errors import ParserError


def read_csv(filepath: str) -> pd.DataFrame:
    """
    Read CSV file and return a panda DataFrame
    Catch ParserError. Try to have ParseError in pytest
    """
    try:
        return pd.read_csv(filepath, sep=',')
    except ParserError:
        raise ParserError("ParserError")


def serie_conversion(df: pd.DataFrame, seriename: str) -> pd.DataFrame:
    """
    Metric conversion column in hectare - 1 hectare = 2,4710 Acres
    KeyError if seriename is not found. NaN and string values are left
    untouched. Pandas detects numbers.
    """
    print(df.columns.to_list())
    if seriename not in df.columns:
        raise KeyError(f"Column '{seriename}' not found")
    df_copy = df.copy()
    df_copy[seriename] = df_copy[seriename].map(
        lambda x: round(x/2.4710, 2) if isinstance(x, (int, float)) else x,
        na_action='ignore')
    return df_copy


def save_csv(filepath: str, df: pd.DataFrame):
    """
    Save panda DataFrame to file
    """
    df.to_csv(filepath)
    return filepath
