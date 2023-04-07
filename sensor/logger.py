import logging
from datetime import datetime
import os


LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H-%M-%S')}.log"
LOG_FILE_DIRECTORY = os.path.join(os.getcwd(),"logs")

#make directory if not present 
os.makedirs(LOG_FILE_DIRECTORY,exist_ok=True)   

LOG_FILE_PATH = os.path.join(LOG_FILE_DIRECTORY,LOG_FILE_NAME)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d | %(name)s | %(levelname)s | %(message)s",
    level= logging.INFO
)