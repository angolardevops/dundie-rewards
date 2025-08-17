import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s "
    "l:%{lineno}d - f:%{filename}s:  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_logger(logfile="dundie.log"):
    """Get a logger with the specified name."""
    fh = handlers.RotatingFileHandler(
        "dundie.log",
        maxBytes=300,  # 10 ** 6,  # 1 MB
        backupCount=10,
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)
    log.addHandler(fh)

    return log
