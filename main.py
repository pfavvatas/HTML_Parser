import os, sys

def main(argv):
    print('main')
    #print(argv)
    from html_code.html import html_init_parser as parser
    parser(argv)

if __name__ == '__main__':
  main(sys.argv[1:])
