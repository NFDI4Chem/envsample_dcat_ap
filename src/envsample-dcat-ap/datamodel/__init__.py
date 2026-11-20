"""Data model package for envsample_dcat_ap."""

from pathlib import Path
from .envsample-dcat-ap import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "envsample-dcat-ap.yaml"
