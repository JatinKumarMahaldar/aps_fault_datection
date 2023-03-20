import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
#collect the above two lline of code from main file


DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME ="APS"
COLLECTION_NAME="SENSORS"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns:{df.shape}")

#drop index from dataframe
df.reset_index(drop = True , inplace = True)

#converting the above dataframe into a json file 
json_records=list(json.loads( df.T.to_json()).values())
print(json_records[0])

#inserting JSON recordes  in mongo db 
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)   