import os, sys
import logging
from logs.log_setup import *

# Set up the logging configuration
setup_logging()
# Create a logger for the module
logger = logging.getLogger(__name__)

def main(argv):
    logger.debug(f"Function {main.__name__} is running with arguments {argv}")

    from html_code.html import html_init_parser as parser
    parser(argv)

if __name__ == '__main__':
  logger.info("Program has started")
  main(sys.argv[1:])
