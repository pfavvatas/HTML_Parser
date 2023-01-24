import os, sys
import urllib.request

def get_url_html_data(href=None):
    #Import HTML from a URL
    print('href: ',href)
    url = urllib.request.urlopen(href)
    html = url.read().decode()
    url.close()
    return html

def get_file_html_data(file=None):
    #Import HTML from a URL
    print('file: ',file)
    with open(file, 'r') as file:
        data = file.read()
    return data