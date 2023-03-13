"""
It contains all the code related to logging (any execution happenings and track it into some file)

"""

import logging
import os
from datetime import datetime


# setting up how my log file should be created its formatting

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# path for the log file

logs_path= os.path.join(os.getcwd(),"logs",LOG_FILE)
# checks if there is a file exist but keep on appending it
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# setting the configuration for logging

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# # test if our logger is working
# if __name__ == "__main__":
#     logging.info('Logging has started')