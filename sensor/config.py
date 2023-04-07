import pymongo
import pandas as pd 
import json
from dataclasses import dataclass
import os
#providing the mongo db url to connect the python with mongodb 

@dataclass

class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGODB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_ACCESS_SECRET_KEY")


    env_var = EnvironmentVariable()
    mongo_client = pymongo.mongo_client(env_var.mongo_db_url)