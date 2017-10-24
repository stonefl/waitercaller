# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:16:44 2017

@author: 5004756
"""

class User:
    def __init__(self, email):
        self.email = email
        
    def get_id(self):
        return self.email
    
    def is_active(self):
        return True
    
    def isanonymous(self):
        return False
    
    def is_authenticated(self):
        return True