import os, sys
from urllib.parse import urlparse
import logging
from logs.log_setup import *

# Set up the logging configuration
setup_logging()
# Create a logger for the module
logger = logging.getLogger(__name__)

def get_list(filename=None):
    #print(filename)
    return get_file_data(filename)

def get_file_data(filename=None):
    lines = []
    # https://stackoverflow.com/questions/3925614/how-do-you-read-a-file-into-a-list-in-python
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
            # print(line)
    return lines

def is_valid_url(url):
    logger.debug(f"Function {is_valid_url.__name__} is running with arguments {url}")
    """
    Check if the given string is a valid URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def is_valid_file_path(path):
    logger.debug(f"Function {is_valid_file_path.__name__} is running with arguments {path}")
    """
    Check if the given string is a valid file path.

    Args:
        path (str): The file path to check.

    Returns:
        bool: True if the path is valid, False otherwise.
    """
    try:
        # Check if the file exists
        return os.path.isfile(path)
    except TypeError:
        return False
    
def is_valid_url_v2(url):
    logger.debug(f"Function {is_valid_url_v2.__name__} is running with arguments {url}")
    """
    Version: 2
    Check if the given string is a valid URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    regex = re.compile(
        r'^https?://'  # Match http:// or https://
        r'(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # Match domain name
        r'(:\d{1,5})?'  # Match port number if present
        r'(/([a-zA-Z0-9\-\._\?\,\:\;\'\/\+\#\&\%\$\=~])*)*'  # Match path if present
        r'(\?[a-zA-Z0-9\-\._\?\,\:\;\'\/\+\#\&\%\$\=~]*)?'  # Match query string if present
        r'(#([a-zA-Z0-9\-\._\?\,\:\;\'\/\+\#\&\%\$\=~])*)?'  # Match fragment identifier if present
        r'$')
    return bool(regex.match(url))