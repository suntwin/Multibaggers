
from arctic import Arctic
class arcticDB():

    def __init__(self,arcserver):
        self.conn = Arctic(arcserver)
        self.arcserver = arcserver

    def get_connection(self):
        return self.conn

    def access_collection(self,collection):
        pass


