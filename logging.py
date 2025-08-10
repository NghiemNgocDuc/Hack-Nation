import logging, os
_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=_level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
def get_logger(name: str):
    return logging.getLogger(name)
