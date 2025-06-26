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


def save_csv(filepath: str, df: pd.DataFrame):
    """
    Save panda DataFrame to file
    """
    df.to_csv(filepath)
    return filepath
