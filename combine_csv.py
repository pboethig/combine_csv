import os
import pandas as pd
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(BASE_DIR,'data')
CACHE_DIR = os.path.join(BASE_DIR,'cache')
os.listdir(DATA_DIR)
try:
    os.mkdir(CACHE_DIR)
except:
    pass
my_dataframes=[]
for filename in os.listdir(DATA_DIR):
        csv_path = os.path.join(DATA_DIR, filename)
        this_df = pd.read_csv(csv_path)
        this_df['file_name']=filename
        my_dataframes.append(this_df)
my_entire_dataframe=pd.concat(my_dataframes)
my_entire_dataframe.head()
my_entire_dataframe.tail()
dataset = os.path.join(CACHE_DIR, 'export.csv')
my_entire_dataframe.to_csv(dataset)
print(f"Export File is written to {CACHE_DIR}/export.csv")