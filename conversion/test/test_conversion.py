import pytest
import pandas as pd
from conversion import serie_conversion


def test_serie_conversion_hectare():
    """
    Dataframe input -> serie_conversion --> Dataframe output
    Comparaison input-ouput.
    Check if input dataframe has not changed.
    """
    df = pd.DataFrame({
        "Area_Burned (Acres)": [14048, 33667, None, "C'est pas un nombre !", 0]
    })

    result = serie_conversion(df, "Area_Burned (Acres)")

    expected = pd.DataFrame({
        "Area_Burned (Acres)": [5685.15, 13624.85, None, "C'est pas un nombre !", 0]
    })

    pd.testing.assert_frame_equal(result, expected)


def test_column_not_found():
    """
    Search column name not in DataFrame.
    serie_conversion catches KeyError.
    """
    df = pd.DataFrame({
        "NotArea": [1, 2, 3]
    })
    with pytest.raises(KeyError, match="Column 'Area' not found"):
        serie_conversion(df, "Area")
