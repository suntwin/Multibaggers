from global_helpers import *
import pandas as pd
from configReader import configReader
class csvUtilities:

    @staticmethod
    def merge_files(path,merge_file_name):
        file_path = get_file_path(path,merge_file_name)
        fout = open(file_path, "a")
        for d, dirs, files in os.walk(path):

            for x in files:
                if (x.endswith(".csv") and x != 'combined.csv' and x != 'combined.csv'):
                    file_name = x
                    file_df = path  + file_name
                    print(file_df)
                    df = pd.read_csv(file_df)

                    #frames = [merged_df, df]
                    #merged_df = pd.concat(frames)
                    df.to_csv(file_path,mode='a',header=False,index=False)

