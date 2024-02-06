#!/usr/bin/python3
"""Module user class which inherites from base"""


from models.base_model import BaseModel as b

class User(b):
    """init the class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
