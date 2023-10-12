import pandas as pd
import pytest

from app.ml import model


def test_load_model():
    assert model.load_model(), "Pickle file not found"


def test_empty_args():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        model.predict(df)
