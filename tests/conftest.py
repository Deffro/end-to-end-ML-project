import pytest

from src.config.core import config
from src.processing.data_manager import load_dataset


@pytest.fixture()
def train_data():
    return load_dataset(file_name=config.app_config.training_data_file)


@pytest.fixture()
def test_data():
    return load_dataset(file_name=config.app_config.test_data_file)
