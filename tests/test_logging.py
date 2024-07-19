from rattle import log as rlog
import logging
import logging.config

logging.config.dictConfig(rlog.DEFAULT_LOGGING_CONFIG)

logging.info("This is an info message")
logging.debug("This is a debug message")
logging.error("This is an error message")
logging.critical("This is a critical message")
logging.warning("This is a warning message")
logging.exception("This is an exception message")
