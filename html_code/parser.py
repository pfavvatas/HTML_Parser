from bs4 import BeautifulSoup
import logging
from logs.log_setup import *
import sys

# Set up the logging configuration
setup_logging()
# Create a logger for the module
logger = logging.getLogger(__name__)

def create_html_object(soup):
    # Create a dictionary to hold information about the HTML element
    html_object = {}
    
    # Add information about the tag name and attributes
    # if soup.name is not None and soup.name != '[document]':
    html_object['tag_name'] = soup.name
    html_object['attributes'] = soup.attrs
    
    # Recursively add information about all child elements
    if len(list(soup.children)) > 0:
        html_object['children'] = []
        for child in soup.children:
            if child.name is not None:
                child_object = create_html_object(child)
                html_object['children'].append(child_object)
    else:
        html_object['content'] = soup.string
    
    return html_object

def parse_html(html_string):
    logger.debug(f"Function {parse_html.__name__} is running")

    soup = BeautifulSoup(html_string, 'html.parser')    
    # Create the nested dictionary object from the BeautifulSoup object
    html_object = create_html_object(soup)

    # Print the dictionary object
    logger.debug(html_object)
    
    return html_object
