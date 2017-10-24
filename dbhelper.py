# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:25:58 2017

@author: 5004756
"""

import pymongo
from bson.objectid import ObjectId

DATABASE = "waitercaller"

class DBHelper:
    
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client[DATABASE]
    
    #### User method s################
    # Get the user through email
    def get_user(self, email):
        return self.db.users.find_one({"email":email})
    
    # add a new user
    def add_user(self, email, salt, hashed):
        self.db.users.insert({"email":email, "salt":salt, "hashed": hashed})
    
    #### Table methods ##################
    # add a new table
    def add_table(self, number, owner):
        new_id = self.db.tables.insert({"number": number, "owner":owner})
        return new_id
    
    # update new id
    def update_table(self, _id, url):
        self.db.tables.update({"_id": _id}, {"$set":{"url":url}})
        
    # get tables of specified owner
    def get_tables(self, owner_id):
        return list(self.db.tables.find({"owner":owner_id}))
    
    # get a table with specified id
    def get_table(self, table_id):
        return self.db.tables.find_one({"_id": ObjectId(table_id)})
    
    # delete selected table
    def delete_table(self, table_id):
        self.db.tables.remove({"_id": ObjectId(table_id)})
        
    #### Request methods ##################
    #add a request
    def add_request(self, table_id, time):
        table = self.get_table(table_id)
        try:
            self.db.requests.insert({"owner": table['owner'], "table_number": table['number'], "table_id": table_id, "time":time})
            return True
        except pymongo.errors.DuplicateKeyError:
            return False
    # get requests of owner
    def get_requests(self, owner_id):
        return list(self.db.requests.find({"owner": owner_id}))
    
    # delete specified request
    def delete_request(self, request_id):
        self.db.requests.remove({"_id": ObjectId(request_id)})
        
        
        
        