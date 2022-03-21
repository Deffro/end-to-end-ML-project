import pandas as pd

from src.config.core import config


def test_column_types(train_data):
    # Check if data is DataFrame
    assert isinstance(train_data, pd.DataFrame)
    cat_vars = [
        f
        for f in train_data.columns
        if f
        not in (
            config.model_config.num_vars
            + [config.model_config.target]
            + [config.model_config.var_to_drop]
        )
    ]
    # Check column types
    for f in cat_vars:
        assert train_data[f].dtype == "O"

    assert train_data["training_hours"].dtype == "int64"
    assert train_data["city_development_index"].dtype == "float64"


def test_number_of_columns(train_data):
    assert train_data.drop([config.model_config.target], axis=1).shape[1] == 12
