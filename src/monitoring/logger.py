# import logging
#
# logging.basicConfig(filename='data/logs/app.log', level=logging.INFO)
#
# def log_event(event):
#     logging.info(event)


import logging
import os

LOGS_DIR = os.path.join('data', 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOGS_DIR, 'app.log')

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_event(event):
    logging.info(event)
