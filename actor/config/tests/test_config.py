"""Test the config module"""
import os
import unittest
from common.config import Config
from actor.config import APP_NAME, APP_DESCRIPTION, config_entries

# The expected values for parameters used via env and/or CLI parameter
test_set = dict(
    LOG_LEVEL="debug",
    LOG_FORMAT="text",
    MESSENGER_URL="localhost:4222",
    MESSENGER_CLIENT_ID="some-other-client-id",
)


def assert_with_defaults(test_case, config):
    """Assert the config parameters against the default values"""
    print("\nassert with defaults")
    for config_entry in config_entries:
        test_case.assertEqual(config.__dict__[config_entry.name], config_entry.default)


def assert_with_expected(test_case, config, ref):
    """Assert the config parameters against the expected values"""
    for prop_name in ref:
        test_case.assertEqual(str(config.__dict__[prop_name]), str(ref[prop_name]))


class ConfigTestCase(unittest.TestCase):
    """The config test cases"""

    def test_config_via_apply_parameters(self) -> None:
        """Test the apply_parameters to config"""
        config = Config(APP_NAME, APP_DESCRIPTION, config_entries)
        config.apply_parameters(test_set)
        assert_with_expected(self, config, test_set)

    def test_config_default_and_via_env(self) -> None:
        """Test the config via env variables"""
        config = Config(APP_NAME, APP_DESCRIPTION, config_entries)
        assert_with_defaults(self, config)

        # setup the environment
        os.environ.update(test_set)
        config = Config(APP_NAME, APP_DESCRIPTION, config_entries)
        assert_with_expected(self, config, test_set)

    def test_config_via_argv(self) -> None:
        """Test the config via parsing the CLI arguments"""
        config = Config(APP_NAME, APP_DESCRIPTION, config_entries)
        config.apply_cli_args(
            [
                "-l",
                test_set["LOG_LEVEL"],
                "-f",
                test_set["LOG_FORMAT"],
                "-u",
                test_set["MESSENGER_URL"],
                "-i",
                test_set["MESSENGER_CLIENT_ID"],
            ]
        ),
        assert_with_expected(self, config, test_set)
