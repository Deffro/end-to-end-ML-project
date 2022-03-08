from typing import List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class Mapper(BaseEstimator, TransformerMixin):
    """Categorical variable mapper."""

    def __init__(self, variables: List[str], mappings: dict):

        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.mappings = mappings

    def fit(self, x: pd.DataFrame, y: pd.Series = None):
        # fit statement to be in line with the sklearn pipeline
        return self

    def transform(self, x: pd.DataFrame) -> pd.DataFrame:
        x = x.copy()
        for feature in self.variables:
            x[feature] = x[feature].map(self.mappings)

        return x
