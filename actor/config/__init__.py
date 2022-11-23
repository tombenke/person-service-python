"""The config module of the application"""
from common.config import Config
from .parameters import (
    APP_NAME,
    APP_DESCRIPTION,
    config_entries,
)

# The configuration object is a module-level singleton
config = Config(APP_NAME, APP_DESCRIPTION, config_entries)
