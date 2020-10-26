import os

def get_abs_path(path):
    return(os.path.abspath(path))

def get_file_path(path,filename):
    filepath = path  + filename
    return(filepath)

def get_file_name_from_equity_code(code):
    filename = code+".csv"
    return(filename)