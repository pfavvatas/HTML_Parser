from bs4 import BeautifulSoup
import logging
from logs.log_setup import *
import sys

# Set up the logging configuration
setup_logging()
# Create a logger for the module
logger = logging.getLogger(__name__) 

def create_html_object(soup, index=0, last_index = 0):
    # Create a dictionary to hold information about the HTML element
    html_object = {}

    html_object['index'] = index

    last_index = str(last_index) + "." + str(index)

    html_object['id'] = last_index
    
    # Add information about the tag name and attributes
    # if soup.name is not None and soup.name != '[document]':
    html_object['tag_name'] = soup.name
    html_object['attributes'] = soup.attrs
    
    # Recursively add information about all child elements
    if len(list(soup.children)) > 0:
        html_object['children'] = []
        for child in soup.children:
            if child.name is not None:
                child_object = create_html_object(child, index, last_index)
                index = index + 1
                html_object['children'].append(child_object)
    else:
        html_object['content'] = soup.string
    return html_object

def parse_html(html_string):
    logger.debug(f"Function {parse_html.__name__} is running")

    soup = BeautifulSoup(html_string, 'html.parser')    
    # Create the nested dictionary object from the BeautifulSoup object
    html_object = create_html_object(soup)
    # print_tree_ids(html_object)

    # Print the dictionary object
    logger.debug(html_object)
    
    return html_object

def parse_html_2(data):
    logger.debug(f"Function {parse_html_2.__name__} is running")

    
    print_tree_ids(data)

    node = data
    # Get the list of IDs of all nodes in the tree
    # id_list = node.get_all_ids()
    # print(id_list)

    # print(get_table_ids(data))
    print(get_table_tag_names(data))

    # Print the dictionary object
    logger.debug(data)
    
    return data

def print_tree_ids(obj, level=0):  
    if 'index' in obj:
        print('  ' * level + str(obj['index']) + " - " + str(obj['tag_name']) + " - " + str(obj['id']))
    if 'children' in obj:
        for child in obj['children']:
            print_tree_ids(child, level + 1)

def get_table_ids(obj):  
    ids = [obj['id']]
    if 'children' in obj:
        for child in obj['children']:
            ids += get_table_ids(child)
    return ids

def get_table_tag_names(obj):  
    tag_name = [obj['tag_name']]
    if 'children' in obj:
        for child in obj['children']:
            tag_name += get_table_tag_names(child)
    return tag_name
