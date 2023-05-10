import os, time
import logging
from logs.log_setup import *
# from url_code import *
# from url_code.utils import *
# from html_code.parser2 import *
from html_code.parser import *
from html_code.utils import *
from common.utils import *

# Set up the logging configuration
setup_logging()
# Create a logger for the module
logger = logging.getLogger(__name__)

List = []

def html_init_parser(argv):
    logger.debug(f"Function {html_init_parser.__name__} is running with arguments {argv}")

    # urlList = readList(argv[0])
    List = readList(argv[0])

    logger.debug("List: %s", List)
    # from parser import Parse
    for item in List:
        # Parse(url)
        if is_valid_url(item) :
            logger.debug(item + " is a valid url")
            html_data = get_url_html_data(item)
        elif is_valid_file_path(item) :
            logger.debug(item + " is a valid file path")
            html_data = get_file_html_data(item)
        else :
            logger.warning("Invalid item: %s", item)
            continue
        #print(html_data)
        
        try:
            stage1 = parse_html(html_data)
            logger.debug("stage1 " , stage1)
        except Exception as e:
        # By this way we can know about the type of error occurring
            print("The error is: ",e)

        try:
            stage2 = parse_html_2(stage1)
            logger.debug("stage2 " , stage2)
        except Exception as e:
        # By this way we can know about the type of error occurring
            print("The error is: ",e)
        
        
        # Parse(html_data)
        #HTMLParser
        # testParser = Parse()
        # testParser.feed(html_data)  
        # print(testParser)      

def readList(filename=None, **kwargs):
    logger.debug(f"Function {readList.__name__} is running with arguments {filename}")
    return get_list(filename)
    
