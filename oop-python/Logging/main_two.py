import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('Logging/time_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("Hello! Logger")
    time.sleep(5)