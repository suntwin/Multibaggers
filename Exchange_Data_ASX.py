from Exchange_Data import Exchange_Data
from iPrice_Formatter import iPrice_Formatter
from configReader_ASX import configReader_ASX
from global_helpers import *
class Exchange_Data_ASX(Exchange_Data,iPrice_Formatter):
    def __init__(self):
        self.config_details = _get_config_details()
        self.header = _get_config("header_fields")
        self.files_root = _get_config("asx_root")
        self.files_loc = _get_config("asx_csv_location")
        pass

    def read_price_all(self):
        abs_path=get_abs_path(self.files_root)
        csv_file_location = get_file_path(abs_path,self.files_loc)

        pass







def _get_config_details():
    return (configReader_ASX.get_setting_all())

def _get_config(property):
    return(configReader_ASX.get_setting(property))

