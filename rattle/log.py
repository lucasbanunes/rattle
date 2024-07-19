"""
This code was done after being inspired by this video by mcoding:
https://www.youtube.com/watch?v=9L77QExPmI0&t=81s
"""

from typing import Dict, override
import json
import logging
import datetime as dt

DEFAULT_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(module)s"
            " | %(lineno)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "json": {
            "()": "rattle.log.JSONFormatter",
            "fmt_keys": {
                "level": "levelname",
                "name": "name",
                "module": "module",
                "lineno": "lineno"
            },
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "json",
            "stream": "ext://sys.stdout"
        },
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stdout"]
        }
    }
}


class JSONFormatter(logging.Formatter):
    def __init__(self,
                 fmt_keys: Dict[str, str] = None,
                 datefmt: str = None):
        super().__init__(datefmt=datefmt)
        self.datefmt = datefmt
        self.fmt_keys = fmt_keys

    @override
    def format(self, record: logging.LogRecord) -> str:
        if self.datefmt is None:
            message_dict = {
                "timestamp": dt.datetime.fromtimestamp(
                    record.created, tz=dt.timezone.utc
                ).isoformat()
            }
        else:
            message_dict = {
                "timestamp": self.formatTime(record, self.datefmt)
            }
        if self.fmt_keys is not None:
            for name, key in self.fmt_keys.items():
                message_dict[name] = getattr(record, key)
        message_dict["message"] = record.getMessage()
        return json.dumps(message_dict)
