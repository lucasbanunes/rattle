"""
This code was done after being inspired by this video by mcoding:
https://www.youtube.com/watch?v=9L77QExPmI0&t=81s
"""

DEFAULT_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(module)s"
            " | %(lineno)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "default",
            "filename": "rattle.log",
            "mode": "a"
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stdout"]
        }
    }
}
