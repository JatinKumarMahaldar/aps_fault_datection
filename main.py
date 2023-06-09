'''import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")'''


from sensor.logger import logging
from sensor.exception import SensorException
import sys
import os


def test_logger_and_exception():
     try:
          logging.info("start testing test_logger_and_exception")
          result = 30/0
          print(result)
          logging.info("stop testing test_logger_and_exception")
     except Exception as e:
          logging.info(e)
          raise SensorException(e , sys)
          



if __name__ == "__main__":
    try:
        get_collection_as_dataframe(database_name = "aps", collection_name="sensor")
    except Exception as e:
        print(e)