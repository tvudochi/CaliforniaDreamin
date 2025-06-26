import pytest
import pandas as pd
from lastFiveyears import serie_lastFiveyears


def test_serie_lastFiveyears():
    """
    Input DataFrame has only one line where date > date.today - 5 years
    -> serie_lastFiveyears -> Output DataFrame has only one valid line.
    """
    today = pd.Timestamp.today()
    five_years_ago = today - pd.DateOffset(years=5)

    df = pd.DataFrame({
        "Date": [
            today.strftime("%Y-%m-%d"),                          # OK
            (five_years_ago - pd.Timedelta(days=1)).isoformat(), # Too old
            "not a date",                                        # Not a date
            None                                                 # None => NaT
        ],
    })

    result = serie_lastFiveyears(df, "Date")

    assert len(result) == 1


def test_serie_lastFiveyears_missing_column():
    df = pd.DataFrame({
        "blablalbala": ["2020-01-01"]
    })
    with pytest.raises(KeyError, match="Column 'Date' not found"):
        serie_lastFiveyears(df, "Date")
