from substitution import read_csv, \
    serie_substitute, save_csv
import pytest
import pandas as pd


def test_serie_substitute():
    """
    Dataframe input -> serie_substitute --> Dataframe output
    Comparaison input-ouput.
    Check if input dataframe has not changed.

    """
    df = pd.DataFrame({
        'Location': ['Sonoma NYC', 'Chez moi et chez elle', None, ''],
    })
    result = serie_substitute(df, 'Location')
    expected = pd.DataFrame({
        'Location': ['Sonoma_NYC', 'Chez_moi_et_chez_elle', None, ''],
    })
    pd.testing.assert_frame_equal(result, expected)
    assert df.loc[0, 'Location'] == 'Sonoma NYC'


def test_serie_substitute_non_string():
    """
    Column is String -> substitution
    Column not string -> ignore action, no substitution
    """
    df = pd.DataFrame({
        'Location': ['Sonoma NYC', 123, None, 4.56, 'Chez moi  et  chez elle']
    })
    result = serie_substitute(df, 'Location')
    expected = pd.DataFrame({
        'Location': ['Sonoma_NYC', 123, None, 4.56, 'Chez_moi__et__chez_elle']
    })
    pd.testing.assert_frame_equal(result, expected)


def test_serie_substitute_keyerror():
    """
    Search column name not in DataFrame.
    serie_substitute catches KeyError. 
    """
    df = pd.DataFrame(
        {'nimportequoua': ["Sonoma_Lol", 0.0002]}
         )
    with pytest.raises(KeyError, match="Column 'name' not found"):
        serie_substitute(df, 'name')
