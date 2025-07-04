import pandas as pd
from pandas.errors import ParserError
import re


def read_csv(filepath: str) -> pd.DataFrame:
    """
    Read CSV file and return a panda DataFrame
    Catch ParserError. Try to have ParseError in pytest
    """
    try:
        return pd.read_csv(filepath, sep=',')
    except ParserError:
        raise ParserError("ParserError")


def save_csv(filepath: str, df: pd.DataFrame):
    """
    Save panda DataFrame to file
    """
    df.to_csv(filepath)
    return filepath


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


def serie_lastFiveyears(df: pd.DataFrame, seriename: str) -> pd.DataFrame:
    """
    Conversion String -> Date time Object
    If None -> Nat
    Return DataFrame with Lines where Colum["Date"] > date.today - 5 years
    """
    if seriename not in df.columns:
        raise KeyError(f"Column '{seriename}' not found")
    df_copy = df.copy()
    df_copy[seriename] = pd.to_datetime(df_copy[seriename], errors='coerce')
    date_limite = pd.Timestamp.today() - pd.DateOffset(years=5)
    df_copy = df_copy[df_copy[seriename] > date_limite]
    return df_copy


def serie_substitute(df: pd.DataFrame, seriename: str) -> pd.DataFrame:
    """
    Replace whitespace by '_' in the specified column seriename.
    KeyError if seriename is not found.
    NaN and non-string values are left untouched.
    """
    if seriename not in df.columns:
        raise KeyError(f"Column '{seriename}' not found")

    df_copy = df.copy()
    df_copy[seriename] = df_copy[seriename].map(
        lambda val: re.sub(r'\s', '_', val) if isinstance(val, str) else val,
        na_action='ignore'
    )
    return df_copy
