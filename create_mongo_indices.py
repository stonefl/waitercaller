# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:22:47 2017

@author: 5004756
"""

import pymongo
client = pymongo.MongoClient()
c = client['waitercaller']
print c.users.create_index("email", unique=True)
print c.requests.create_index("table_id", unique=True)