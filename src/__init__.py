from src.config.core import PACKAGE_ROOT, config

with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()