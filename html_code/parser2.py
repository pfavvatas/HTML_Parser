# https://www.askpython.com/python-modules/htmlparser-in-python
from html.parser import HTMLParser
 
class Parse(HTMLParser):
    def __init__(self):
    #Since Python 3, we need to call the __init__() function 
    #of the parent class
        super().__init__()
        self.reset()
 
    #Defining what the methods should output when called by HTMLParser.
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for a in attrs:
            print("Attributes of the tag: ", a)
 
    def handle_data(self, data):
        print("Here's the data: ", data)
 
    def handle_endtag(self, tag):
        print("End tag: ", tag)