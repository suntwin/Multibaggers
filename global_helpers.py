import os

def get_abs_path(path):
    return(os.path.abspath(path))

def get_file_path(path,filename):
    filepath = path  + filename
    return(filepath)