import logging

def setup_logging():
    logging.basicConfig(filename='logs/app.log', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')