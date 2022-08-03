import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%m/%d/%Y %H:%M:%S",
# )

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is a error message")
# logging.critical("This is a critical message")

# import helper

# ########################################################
# logger = logging.getLogger(__name__)

# # Create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler("Logging/file.log")

# # Level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("This is a warning message")
# logger.error("This is a error message")

# ########################################################

import logging.config

logging.config.fileConfig("Logging/logging.conf")
logger = logging.getLogger("simpleExample")
logger.debug("This is a debug message")

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logger.error(e, exc_info=True)
