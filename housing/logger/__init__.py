import logging
from datetime import datetime
import os

LOG_DIR = "housing_logs" #directory name

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}" #capturing current time stamp

LOG_FILE_NAME = f'log_{CURRENT_TIME_STAMP}.log' #log file name

os.makedirs(LOG_DIR,exist_ok=True) #creating directory, also checks if it is already present(if yes then it continues with the same).

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME) #getting log file path

#writing log file at log file location with a good format
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)
