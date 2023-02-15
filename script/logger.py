import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from timeit import default_timer as timer


class Logger:
    __slot__ = ['start', 'end']

    def __init__(self):
        self.start = timer()
        prod = os.getenv('ENVIRONMENT', 'production') == 'production'
        logging.basicConfig(
            level=logging.INFO if prod else logging.DEBUG,
            format='[%(asctime)s]\t[%(levelname)s]\t%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                TimedRotatingFileHandler('./logs/app.log', when='midnight', backupCount=10),
                logging.StreamHandler(sys.stdout)
            ]
        )

    def debug(self, message):
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)

    def done(self):
        self.end = timer()
        logging.info(f'Runtime: {self.end - self.start:,.2f} seconds')
