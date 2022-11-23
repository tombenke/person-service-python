"""Configuration parameters and data"""
from common.logger.logger import get_format_choices, get_level_choices
from common.config import ConfigEntry, CliEntry

APP_NAME = "person-service-python"
APP_DESCRIPTION = """A sample easer REST API endpoint implementation in Python"""


config_entries = [
    ConfigEntry(
        name="MESSENGER_URL",
        help_text="The URL of the messenger cluster",
        default="nats://localhost:4222",
        cli=CliEntry(short_flag="-u", name="--messenger-url"),
    ),
    ConfigEntry(
        name="MESSENGER_CLIENT_ID",
        help_text="The client-id of messenger",
        default="person-service-python-impl",
        cli=CliEntry(short_flag="-i", name="--messenger-client-id"),
    ),
    ConfigEntry(
        name="LOG_LEVEL",
        help_text=f"Log level {get_level_choices()}",
        default="info",
        cli=CliEntry(short_flag="-l", name="--log-level", choices=get_level_choices()),
    ),
    ConfigEntry(
        name="LOG_FORMAT",
        help_text=f"The format of the log messages {get_format_choices()}",
        default="text",
        cli=CliEntry(
            short_flag="-f", name="--log-format", choices=get_format_choices()
        ),
    ),
    ConfigEntry(
        name="DUMP_CONFIG",
        help_text="Dump the actual configuration parameters of the application",
        default=False,
        cli=CliEntry(
            short_flag="-d", name="--dump-config", entry_type=bool, action="store_true"
        ),
    ),
]
