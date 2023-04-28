import os, time
from url_code import *
from url_code.utils import *
from html_code.parser import *
from html_code.utils import *
from common.utils import *


List = []

def html_init_parser(argv):
    print('htmlParser')
    # print(argv)
    # urlList = readList(argv[0])
    List = readList(argv[0])

    print(List)
    # from parser import Parse
    for item in List:
        # Parse(url)
        # html_data = get_file_html_data(item)
        if is_valid_url(item) :
            html_data = get_url_html_data(item)
        elif is_valid_file_path(item) :
            html_data = get_file_html_data(item)
        #print(html_data)
        #HTMLParser
        # testParser = Parse()
        # testParser.feed(html_data)        

def readList(filename=None, **kwargs):
    # print(filename)
    return get_list(filename)
    
