import pandas as pd
from arctic import Arctic
class arcticDB():

    def __init__(self,arcserver,collection):
        self.conn = Arctic(arcserver)
        self.collection = collection
        self.library = self.conn[collection]
        _initialize_arctic_collection(self.conn,collection)

    def get_connection(self):
        return self.conn

    def access_collection(self,collection):
        pass

    def update_collection(self,dataframe,symbol):
        self.library.write(symbol,dataframe)

    def read_collection(self,symbol,version=None):
        df=pd.DataFrame()
        df=self.library.read(symbol).data
        return(df)

    def create_collection(self):
        #no need for this method, as initialization is enough
        pass

    def delete_collection(self):
        # this will be delete implementation
        pass









def _initialize_arctic_collection(connection,collection):
    connection.initialize_library(collection)



