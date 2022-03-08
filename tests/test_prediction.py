from src.config.core import config
import numpy as np
from src.predict import make_prediction


def test_make_prediction(all_data):
    expected_first_10_predictions = [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]

    result = make_prediction(input_data=all_data)
    predictions = result.get("predictions")

    assert predictions[:10] == expected_first_10_predictions
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
