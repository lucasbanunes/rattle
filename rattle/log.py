"""
This code was done after being inspired by this video by mcoding:
https://www.youtube.com/watch?v=9L77QExPmI0&t=81s
"""

from typing import Dict, override, Callable
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
    """
    Custom JSON formatter for logging and it can be customized
    to include additional fields with fmt_keys.
    The JSON message will always include the timestamp and the message and when
    the log level is ERROR it will include the exception information
    from record.exc_info.
    """
    def __init__(self,
                 fmt_keys: Dict[str, str] = None,
                 datefmt: str = None):
        """

        Parameters
        ----------
        fmt_keys : Dict[str, str], optional
            (key, value) pairs for the extra (json_key, record_key) mapping,
            by default None
        datefmt : str, optional
            Format of the timestamp key, by default isoformat when None
        """
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
        if record.levelno == logging.ERROR:
            message_dict["exception"] = record.exc_info
        return json.dumps(message_dict)


def log_execution(func: Callable,
                  log_func: Callable[[str]] = logging.info,
                  start_log: bool = True,
                  end_log: bool = False) -> Callable:
    """
    Decorator to log the execution of a function

    Parameters
    ----------
    func : Callable
        Function to be decorated
    log_func : Callable[[str]], optional
        Logging function to call, by default logging.info
    start_log : bool, optional
        If true logs the execution start, by default True
    end_log : bool, optional
        If true logs the execution end, by default True
    Returns
    -------
    Callable
        Decorated function
    """
    def wrapper(*args, **kwargs):
        if start_log:
            log_func(f"Starting execution of {func.__name__}")
        result = func(*args, **kwargs)
        if end_log:
            log_func(f"Execution of {func.__name__} completed")
        return result
    return wrapper
