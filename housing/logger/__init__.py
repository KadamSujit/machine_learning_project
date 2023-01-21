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
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO)


def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]
