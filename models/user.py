#!/usr/bin/python3
<<<<<<< HEAD
"""Module user class which inherites from base"""


from models.base_model import BaseModel as b

class User(b):
    """init the class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
=======
"""class User that inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> g-feature
