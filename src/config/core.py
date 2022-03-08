from pathlib import Path
from typing import Dict, List, Sequence

from pydantic import BaseModel
from strictyaml import YAML, load

PACKAGE_ROOT = Path('../').resolve()
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class ModelConfig(BaseModel):
    target: str
    var_to_drop: str
    cat_vars_replace_na_with_string_missing: List[str]
    ca_vars_replace_na_with_frequent: List[str]
    num_vars: List[str]
    num_vars_yeo_johnson: List[str]
    cat_vars_ordinal: List[str]
    cat_vars_ordinal_arbitrary: List[str]
    cat_vars_onehot: List[str]
    cat_vars_count_frequency: List[str]
    experience_var: List[str]
    experience_map: Dict[str, int]
    last_new_job_var: List[str]
    last_new_job_map: Dict[str, int]
    company_size_var: List[str]
    company_size_map: Dict[str, int]
    test_size: float
    random_state: int


class Config(BaseModel):
    """Master config object."""

    model_config: ModelConfig


def find_config_file() -> Path:
    """Locate the configuration file."""

    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config not found at {CONFIG_FILE_PATH}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        model_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()
