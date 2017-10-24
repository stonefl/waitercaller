# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:58:13 2017

@author: 5004756
"""

import hashlib
import os
import base64

class PasswordHelper:
    
    def get_hash(self, plain):
        return hashlib.sha512(plain).hexdigest()
    
    def get_salt(self):
        return base64.b64encode(os.urandom(20))
    
    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected