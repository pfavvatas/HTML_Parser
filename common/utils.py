import os, sys
from urllib.parse import urlparse

def is_valid_url(url):
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