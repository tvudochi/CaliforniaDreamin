import pandas as pd
import re
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


def save_csv(filepath: str, df: pd.DataFrame):
    """
    Save panda DataFrame to file
    """
    df.to_csv(filepath)
    return filepath
