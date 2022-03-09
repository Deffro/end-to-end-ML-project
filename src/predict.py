import pandas as pd

from src import __version__ as _version
from src.config.core import config
from src.processing.data_manager import load_pipeline

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
trained_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(input_data) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)

    predictions = trained_pipe.predict(
        X=data.drop([config.model_config.target], axis=1)
    )
    results = {
        "predictions": [pred for pred in predictions],
        "version": _version,
    }

    return results
