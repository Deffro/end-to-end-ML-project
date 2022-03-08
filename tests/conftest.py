import pytest

from src.config.core import config
from src.processing.data_manager import load_dataset


@pytest.fixture()
def all_data():
    return load_dataset(file_name=config.app_config.training_data_file)
