import os, sys
import urllib.request
import logging
from logs.log_setup import *

# Set up the logging configuration
setup_logging()
# Create a logger for the module
logger = logging.getLogger(__name__)

def get_url_html_data(href=None):
    logger.debug(f"Function {get_url_html_data.__name__} is running with arguments {href}")
    #Import HTML from a URL
    logger.debug('href: ' + href)
    url = urllib.request.urlopen(href)
    html = url.read().decode()
    url.close()
    return html

def get_file_html_data(file=None):
    logger.debug(f"Function {get_file_html_data.__name__} is running with arguments {file}")
    #Import HTML from a URL
    #Import HTML from a URL
    logger.debug('file: ' + file)
    with open(file, 'r') as file:
        data = file.read()
    return data