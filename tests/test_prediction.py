import time

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.config.core import config
from src.predict import make_prediction


def test_make_prediction(train_data):

    expected_first_10_predictions = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    result = make_prediction(input_data=train_data)
    predictions = result.get("predictions")

    assert predictions[:10] == expected_first_10_predictions
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)


def test_accuracy_over_threshold(train_data):

    X_train, X_test, y_train, y_test = train_test_split(
        train_data.drop([config.model_config.target], axis=1),
        train_data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )

    result = make_prediction(input_data=X_test)
    predictions = result.get("predictions")

    assert accuracy_score(y_test, predictions) > 0.77


def test_serving_latency(train_data):

    s = time.time()
    for i in range(100):
        make_prediction(input_data=train_data[:1])
    elapsed_time = time.time() - s
    assert elapsed_time < 5
