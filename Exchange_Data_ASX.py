from Exchange_Data import Exchange_Data
from arcticDB import arcticDB
from configReader_ASX import configReader_ASX
from global_helpers import *
import pandas as pd
import os
class Exchange_Data_ASX(Exchange_Data):

# this class is responsible for CRUD operations of ASX data from arcticDB
# """"""
# This class will be responsible for loading of asx data through csv files
# to load the data into the database, arcticdb dependent object will be used
# """"""


    def __init__(self,arctic):
        self.config_details = _get_config_details()
        self.header = _get_config("header_fields")
        self.files_root = _get_config("asx_root")
        self.files_loc = _get_config("asx_csv_location")
        self.arctic = arctic
        pass


    # def get_price_data_all(self,combined_file_name):
    #     abs_path=get_abs_path(self.files_root)
    #     csv_file_location = get_file_path(abs_path,self.files_loc)

    def get_price_data_by_symbol(self,symbol):
        abs_path = get_abs_path(self.files_root)
        file_name = get_file_name_from_equity_code(symbol)
        csv_file_location = get_file_path(abs_path, self.files_loc)
        file_path = csv_file_location+"\\"+file_name
        #get the header field configuraiton
        header_fields = configReader_ASX.get_setting("header_fields")
        #create a dataframe from csv file with the header fields
        print("processing filename",file_name)
        df=pd.DataFrame()
        df=pd.read_csv(file_path,header=0,names=self.header)
        # remove the symbol column from the dataframe
        df.drop(['Symbol'], axis=1, inplace=True)
        return(df)

    def get_all_symbols(self):
        #read the location that contains all the data and extract all the symbols
        #directory path
        csv_files_location = get_file_path(self.files_root, self.files_loc)
        symbol_list = []
        for root, dir, files in os.walk(csv_files_location):
            for file in files:
                if file.endswith(".csv"):
                    symbol_list.append(file.split(".")[0])
        return(symbol_list)

    def read_price_by_symbol(self,symbol):
        df=self.arctic.read_collection(symbol=symbol)
        return(df)


    def update_db_by_symbol(self,dataframe,symbol):
        self.arctic.update_collection(dataframe=dataframe,symbol=symbol)

    def get_symbol_version(self,symbol):
        self.arctic.get_symbol_version(symbol=symbol)










def _get_config_details():
    return (configReader_ASX.get_setting_all())

def _get_config(property):
    return(configReader_ASX.get_setting(property))

