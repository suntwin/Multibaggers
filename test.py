from arcticDB import arcticDB
from csvUtilities import csvUtilities
from configReader import configReader
arctic_db = arcticDB('127.0.0.1')
import pandas as pd
connection = arctic_db.get_connection()
# connection.initialize_library('asx_eod')

# print(configReader.get_setting('merge_cols'))
# csvUtilities.merge_files(configReader.get_setting('merge_files_path'),"combined.csv")
connection.initialize_library('arctic.asx_eod2')
lib_asx = connection['arctic.asx_eod2']
print(connection.list_libraries())
print("type of lib",type(lib_asx))
data = {'Date': ['20130521', '20130522'], 'Open': [118.711, 118.712],'High': [119.12, 120.23],'Low': [114.11, 113.32],'Close': [117.12, 117.13],'Volume': [121212, 12121212],'Gross': [1187.11, 1187.13],'OpnInt': [0, 100]}
df = pd.DataFrame(data,columns=['Date','Open','High','Low','Close','Volume','Gross','OpnInt'])
lib_asx.write('GBX',df)
read_df = lib_asx.read('GBX',as_of=4).data
print((read_df))
list(lib_asx.list_versions('GBX'))
print(lib_asx.list_symbols())
