import logging


logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s : %(levelname)s : %(message)s",
)
file_handler = logging.FileHandler("dca_bot.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
