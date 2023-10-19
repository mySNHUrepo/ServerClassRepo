from pymongo import MongoClient
from bson.objectid import ObjectId

class CRUD(object):
    """ CRUD operations for MongoDB """

    def __init__(self, USER='aacuser', PASS='aacPass', HOST='nv-desktop-services.apporto.com', PORT=32080, DB='AAC', COL='animals'):
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a new document into the collection."""
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error occurred:", e)
                return False
        else:
            print("Data not provided")
            return False

    def read(self, query):
        """Query documents from the collection."""
        try:
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print("Error occurred:", e)
            return []

    def update(self, query, data):
        """Update document(s) in the collection."""
        try:
            result = self.collection.update_many(query, {"$set": data})
            return result.modified_count
        except Exception as e:
            print("Error occurred:", e)
            return 0

    def delete(self, query):
        """Delete document(s) from the collection."""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Error occurred:", e)
            return 0
